# -*- coding:utf-8 -*-

import pandas as pd
import math,csv,random
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

base_elo = 1600
team_elos = {}
team_stats = {}
x = []
y = []
folder = '/home/yuyi/下载/data'

def initialize_data(Mstat,Ostat,Tstat):
	new_Mstat = Mstat.drop(['Rk','Arena'],axis = 1)
	new_Ostat = Ostat.drop(['Rk','G','MP'],axis=1)
	new_Tstat = Tstat.drop(['Rk','G','MP'],axis=1)

	team_stats1 = pd.merge(new_Mstat,new_Ostat,how='left',on='Team')
	team_stats1 = pd.merge(team_stats1,new_Tstat,how='left',on='Team')
	return team_stats1.set_index('Team',inplace=False,drop=True)

def get_elo(team):
	try:
		return team_elos[team]
	except:
		team_elos[team] = base_elo
		return team_elos[team]

def calc_elo(win_team,lose_team):
	winner_rank = get_elo(win_team)
	loser_rank = get_elo(lose_team)

	rank_diff = winner_rank - loser_rank
	exp = (rank_diff * -1)/400

	odds = 1/(1 + math.pow(10,exp))

	if winner_rank < 2100:
		k=32

	elif winner_rank >= 2100 and winner_rank < 2400:
		k=24

	else:
		k=16

	new_winner_rank = round(winner_rank + (k* (1 - odds)))
	new_rank_diff = new_winner_rank - winner_rank
	new_loser_rank = loser_rank - new_rank_diff

	return new_winner_rank,new_loser_rank

def build_dataSet(all_data):
	print('Building data set..')
	x = []
	skip = 0
	
	for index,row in all_data.iterrows():
		Wteam = row['WTeam']
		Lteam = row['LTeam']

		team1_elo = get_elo(Wteam)
		team2_elo = get_elo(Lteam)

		if row['WLoc'] == 'H':
			team1_elo += 100
		else:
			team2_elo += 100

		team1_features = [team1_elo]
		team2_features = [team2_elo]

		for key,value in team_stats.loc[Wteam].iteritems():
			team1_features.append(value)
		for key,value in team_stats.loc[Lteam].iteritems():
			team2_features.append(value)

		if random.random() > 0.5:
			x.append(team1_features + team2_features)
			y.append(0)

		else:
			x.append(team2_features + team1_features)
			y.append(1)

		if skip == 0:
			print x
			skip = 1

		new_winner_rank,new_loser_rank = calc_elo(Wteam,Lteam)
		team_elos[Wteam] = new_winner_rank
		team_elos[Lteam] = new_loser_rank
	return np.nan_to_num(x),y

if __name__ == '__main__':
	Mstat = pd.read_csv(folder + '/15-16Miscellaneous_Stat.csv')
	Ostat = pd.read_csv(folder + '/15-16Opponent_Per_Game_Stat.csv')
	Tstat = pd.read_csv(folder + '/15-16Team_Per_Game_Stat.csv')

	team_stats = initialize_data(Mstat,Ostat,Tstat)

	result_data = pd.read_csv(folder + '/2015-2016_result.csv')
	x,y = build_dataSet(result_data)

	print('Fitting on %d game samples..' % len(x))
	mode1 = linear_model.LogisticRegression()
	mode1.fit(x,y)

	print 'Doing cross-validation..'
	print cross_val_score(mode1,x,y,cv=10,scoring='accuracy',n_jobs=-1).mean()