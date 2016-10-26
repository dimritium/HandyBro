#!/usr/bin/python
#deal with SSLError -->connection private
#deal with ConnectionError --> failed to establish connection
import requests,sys,webbrowser
from selenium import webdriver
import easygui

class bro:

	def login(self):
		url='http://172.16.2.1:1000/login?'
		flag=0
		lisdic=[]
		s='14BCS14'
		for i in range(100):
			lisdic.append({'username':s+str('%02d'%(i)),'password':s+str('%02d'%(i))})
		browser=webdriver.Chrome()
		print 'Connecting...'
		browser.get(url)

		try:
			rs=requests.get('http://www.google.com')
			if '172.16.2' in rs.url: #might return status code 200 even if not authenticated (redirect issue)
				raise Exception
			else:
				print 'Already Connected'
				easygui.msgbox('Connected Enjoy!!','Connection Status..')
				browser.close()
				webbrowser.open('http://www.google.com') #set your homepage
				raise SystemExit

		except Exception as err:
			print err
			print 'Trying more hold on'
			for i in range(1,100):
				browser.get(url)
				user=browser.find_element_by_name('username')
				user.send_keys(lisdic[i]['username'])
				print lisdic[i]['username']
				passw=browser.find_element_by_name('password')
				passw.send_keys(lisdic[i]['password'])
				print lisdic[i]['password']
				passw.submit()
				
				try:
					rs=requests.get('http://www.google.com')
					if '172.16.2' in rs.url:
						print 'Raising exception'
						raise Exception
					else:
						flag=1
						easygui.msgbox('Connected Enjoy!!','Connection Status..')
						browser.close()
						webbrowser.get('http://www.google.com') #set your homepage
						break;
			
				except Exception as err:
					continue;

		if flag==0:
			easygui.msgbox('None key worked')

if __name__=='__main__':
	x=bro()
	x.login()