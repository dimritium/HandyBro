#!/usr/bin/python
#deal with SSLError -->connection private
#deal with ConnectionError --> failed to establish connection
import requests,sys,webbrowser,bs4
from selenium import webdriver
import easygui
from fake_useragent import UserAgent

class Brow:

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
			rs_sec=requests.get('http://www.fb.com')
			soup=bs4.BeautifulSoup(rs_sec.text,'html.parser')
			if '172.16.2' in rs.url or 'class="blocked"' in str(soup): #might return status code 200 even if not authenticated (redirect issue)
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
					rs_sec=requests.get('http://www.fb.com')
					soup=bs4.BeautifulSoup(rs_sec.text,'html.parser')
					if '172.16.2' in rs.url and 'class="blocked"' in str(soup):
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

	def multiSearch(self,args):
		print ('Googling...')
		ua=UserAgent()
		headers=ua.chrome
		print headers
		res=requests.get('http://www.google.com/search?q='+' '.join(sys.argv[1:]),headers=headers)
		res.raise_for_status()
		soup=bs4.BeautifulSoup(res.text,'lxml')
		linkElems=soup.select('.r a')
		numOpen=min(5,len(linkElems))
		for i in range(numOpen):
			webbrowser.open('http://google.com'+linkElems[i].get('href'))

	

if __name__=='__main__':
	x=bro()
	if sys.argv[1]=="log":
		x.login()
	if sys.argv[1]=='sea':
		x.multiSearch(''.join(sys.argv[2:]))
