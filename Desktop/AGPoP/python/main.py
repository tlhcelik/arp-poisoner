#!/usr/bin/env python
'''
usage: 
	python main.py help -> HELP
	python main.py path 
'''

from os import system as linux
from os.path import exists 
from os import geteuid
from os import getcwd as pwd
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
	
	current_path = copy_files(path)
	print(COLORS.magenta+"[*]For pushing file to commit write [Default (Add files via upload) hit enter]"+COLORS.black)
	ans = raw_input()

	if len(ans) == 0:
		linux("git commit -m \"Add files via upload\" {0}".format(current_path))
	else:
		linux("git commit -m {0} {1}".format(str(ans),current_path))
	
	print(COLORS.blue+"[*]Write to GitHub repo URL [ https://github.com/username/repo_name.git ]."+COLORS.black)
	url = raw_input()
	
	if(len(url) != 0):
		add_url(url)

	print(COLORS.blue+"[*]Write to branch [ Default master ]."+COLORS.black)
	branch = raw_input()
	print(COLORS.blue+"[*]Wait a second ..."+COLORS.black)
	
	if(len(branch) == 0):
		branch = "master"
		linux("git pull origin {0}".format(str(branch))) #a1
	else:
		linux("git pull origin {0}".format(str(branch))) #a2

	print(COLORS.green+"[*]Everything is okey."+COLORS.black)
	print(COLORS.blue+"[*]Do you push repo [Default (Y)/(N)]."+COLORS.black)
	ans = raw_input()
	
	if len(ans) == 0:
		push_project(branch,url,current_path)
		sys.exit() # Program finish
	else:
		sys.exit()

def copy_files(path):
	current_path = pwd()
	try:
		linux("cp -rf {0} {1}".format(path,current_path))
		return current_path
	except:
		sys.exit()
		
def push_project(branch,url,path):
	try:
		linux("git push origin {0}".format(str(branch)))
		print(COLORS.green+"[*]File's uploaded."+COLORS.black)
		print(COLORS.green+"[*]Goto project: "+url+""+COLORS.black)
		sys.exit()
	except:
		print(COLORS.red+"[!]Push Error. Try Againing!"+COLORS.black)
		try:
			linux("git push origin {0} --force".format(str(branch)))
			print(COLORS.green+"[*]File's uploaded."+COLORS.black)
			print(COLORS.green+"[*]Goto project: "+url+""+COLORS.black)
		except:
			print(COLORS.red+"[!]Push Error. Exiting!"+COLORS.black)
			print(COLORS.red+"[!]Manual try code : \n!"+COLORS.black)
			print(COLORS.blue+"[!]git push origin <branch> --force"+COLORS.black)
			sys.exit()
				
def add_url(url):
	try:	
		linux("git remote add origin {0}".format(url))
		print(COLORS.green+"[*]Remote GitHub repo added."+COLORS.black)
		
	except:
		print(COLORS.red+"[!]URL Error. Try Again!"+COLORS.black)
		add_url(path)
	pass	
		
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
	
		
	
