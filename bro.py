#!/usr/bin/python
from packages.brow import Brow
import sys

if __name__=='__main__':
	obj=Brow()
	
	try:
		if sys.argv[1]==None:
			pass
	except:
		Brow.login(obj)
	
	if sys.argv[1]=='sea':
		Brow.multiSearch(obj,''.join(sys.argv[2:]))