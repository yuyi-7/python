from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def vote(name,password):
	browser = webdriver.Firefox()
	browser.get('https://www.yiban.cn/login?go=http%3A%2F%2Fwww.yiban.cn%2F')
	print('成功进入易班登录界面')
	browser.implicitly_wait(10)
	_name = browser.find_element_by_id('account-txt')
	_name.send_keys(name)
	_password = browser.find_element_by_id('password-txt')
	_password.send_keys(password)
	print('已输入账号和密码')
	_password.send_keys(Keys.RETURN)
	time.sleep(2)
	#try:
	elem = browser.find_element_by_xpath("//a[@class='gray-btn login-btn-weakpsd']")
	elem.click()
	browser.implicitly_wait(10)
	#Exception:
	#	pass
	#finally:
	voice = browser.find_element_by_xpath("//a[@href='http://voice.yiban.cn/']")
	voice.click()
	browser.implicitly_wait(10)
	print('进入校园好声音页面')
	#windows = browser.window_handles
#	browser.switch_to.window(windows[-1])
#	print('切换窗口')
	time.sleep(10)
	browser.implicitly_wait(10)
	xihua = browser.find_element_by_link_text('西华大学')
	
	time.sleep(5)
	xihua.click()
	print('找到西华大学')
	browser.implicitly_wait(10)
	#browser.switch_to.window(windows[-1])
	last = browser.find_element_by_xpath("//div[@class='vote_me']")
	last.click()
	browser.implicitly_wait(10)
	print('已投票')

if __name__ == '__main__':
	name = input('请输入易班账号：')
	password = input('请输入密码：')
	vote(name, password)