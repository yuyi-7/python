#!/usr/local/bin/python
#coding=utf-8

#0008 Title: an HTML file, find the inside of the body .


from urllib import request
from bs4 import BeautifulSoup

url = "https://www.google.co.in"
page = request.urlopen(url)

soup = BeautifulSoup(page)
print(soup.body.text(strip=True))