#!/usr/bin/env python
'''
usage: 
	python main.py help -> HELP
	python main.py path 
'''

from os import system as linux
from os.path import exists 
from os import geteuid

import sys
from colors import COLORS 

def project(path):
	linux("git status {0}".format(path))
	
	print(COLORS.blue+"[*]Green file is added locale .git file."+COLORS.black)
	print(COLORS.blue+"[*]Red file is don't added locale .git file."+COLORS.black)
	print(COLORS.magenta+"[*]Do you want contiune? [Default (Y)/(N)] "+COLORS.black)
	ans = raw_input()
	
	if (ans == "y" or ans == "Y") or (len(ans) == 0):
		linux("git add * {0}".format(path))
		linux("git status {0}".format(path))
	else:
		sys.exit()
	
	print(COLORS.magenta+"[*]For pushing file to commit write [Default (Via file upload) hit enter]"+COLORS.black)
	ans = raw_input()
	
	if len(ans) == 0:
		linux("git commit -m \"Via File Upload\"")
	else:
		linux("git commit -m {0}".format(str(ans)))
		
		
def usage():
	print("help")

def root_check():
	if not geteuid() == 0: 
		print (COLORS.red+"[!]Run as root"+COLORS.black)
		sys.exit()

def get_arguments():
	pass

def main():
	linux("clear")
	
	print(COLORS.cyan+"[*]Starting AGPoP (Automatic GitHub Push or Pull ) Program"+COLORS.black)
	PATH=sys.argv[1]
	
	if exists(PATH):
		print(COLORS.green+"[*]Project file is exist."+COLORS.black)
		project(PATH)
	else:
		print(COLORS.red+"[*]File not found."+COLORS.black)
		usage()
		sys.exit()	
		
	

if __name__=="__main__":
	root_check()	
	main()
	
		
	
