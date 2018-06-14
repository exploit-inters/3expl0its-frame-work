#!/usr/bin/env python2
#Welcome to 3xpl0its.py

'''
imports
'''

import os
import random
from sys import *
from time import *
from time import gmtime, strftime
import datetime
from subprocess import call
from subprocess import Popen


def home():

	'''
	def's
	'''
	
class color:
	
	HEADER = '\033[95m'
	IMPORTANT = '\33[35m'
	NOTICE = '\033[33m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	RED = '\033[91m'
	END = '\033[0m'
	UNDERLINE = '\033[4m'
	LOGGING = '\33[34m'
	
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.LOGGING]
random.shuffle(color_random)
	
logo = color_random[0] + '''
                                        ___                  ___                  
                                       (   )           .-.  (   )                 
           .--.    ___  ___     .-..    | |     .-.   ( __)  | |_         .--.    
         /     \  (   )(   )   /    \   | |   /    \  (''") (   __)     /  _  \   
        (___)`. |  | |  | |   ' .-,  ;  | |  |  .-. ;  | |   | |       . .' `. ;  
           .-' /    \ `' /    | |  . |  | |  | |  | |  | |   | | ___   | '   | |  
           '. \     / ,. \    | |  | |  | |  | |  | |  | |   | |(   )  _\_`.(___) 
         ___ \ '   ' .  ; .   | |  | |  | |  | |  | |  | |   | | | |  (   ). '.   
        (   ) ; |  | |  | |   | |  ' |  | |  | '  | |  | |   | ' | |   | |  `\ |  
         \ `-'  /  | |  | |   | `-'  '  | |  '  `-' /  | |   ' `-' ;   ; '._,' '  
          ',__.'  (___)(___)  | \__.'  (___)  `.__,'  (___)   `.__.     '.___.'   
                              | |                                                 
                             (___)                        V: 1.3      
        ___________________________________________________________________________		
                        Made by: Zachary Knox  |  AkA: CRO-thehacker		
	''' + color.END
	
def clearscr():
		os.system('cls')
		
clearscr()

expl0itsmenu = color_random[1] + '''
           [0]	Update
	   [1]	Install
	   [2]	Help Menu
	   [3]	GitHub
	   [4]	README
	   [5]	Exploits Installed
	   [6]	Start 3xpl0its.py
	  [99]	Exit
	   ''' + color.END
	   
def Exit():
		print("Have a good day!")
		exit
		exit

		
ExploitsInstalled = color.RED + '''
[*] Running test

[+]	/Exploits/DNS/
[+]	/Exploits/Router/
[+]	/Exploits/UDP/rootkits/
[+]	/Exploits/TCP/rootkits/
[+]	/Exploits/REV-shell/
[+]	/Exploits/BOT/botnets/ *
[+~]	/Exploits/BOT/botnets/Mari/
[+~]	/Exploits/BOT/botnets/ETC./
[+]	/Exploits/SQL-injection/
[+]	/Exploits/XXS/
[+]	/Exploits/Frame-work/ *
[+~]	/Exploits/Frame-work/MSF
[+~]	/Exploits/Frame-work/RouterSplite/
[+]	/Exploits/UDK/

[*] Test done!

	''' + color.END

def GitHub():
	print("YOU ARE ABOUT TO TRANSFORD TO github.com/CRO-THEHACKER. ARE YOU SURE? [1/0]")
	Choice = raw_input("1/0: ")
	if Choice == 1:
		print(Choice)
		tansgithub()
	elif Choice == 0:
		home()
		
def tansgithub():
	print("Going to github.com/CRO-THEHACKER...")
	os.system('https://www.github.com/CRO-THEHACKER')
	
def Update3xpl0its():
	print('\n')
	print('Starting Updates...')
	os.system('git clone github.com/CRO-THEHACKER/3xpl0its.git')

def ReInstall3xpl0its():
	print("\n")
	print("Re-Installing 3xpl0its.git")
	os.system('sudo apt-get install -y git')
	os.system('sudo apt-get install -y nmap')
	os.system('git clone github.com/CRO-THEHACKER/3xpl0its.git')

	
def HelpMenu():
	print('''
	
	Sorry - the helpMenu is not available...
	
	''')
	
	
def Start3xpl0itsPY():
	Popen('python 3xpl0its.py')
	
'''
Shell stuff
'''

print(logo)
print(expl0itsmenu)

Shell = input("3expl0it > ")
if Shell == 0:
	Update3xpl0its()
elif Shell == 1:
	ReInstall3xpl0its()
elif Shell == 2:
	HelpMenu()
elif Shell == 3:
	GitHub()
elif Shell == 4:
	READMEmenu()
elif Shell == 5:
	print(ExploitsInstalled)
elif Shell == 6:
	Start3xpl0itsPY()
elif Shell == 99:
	Exit()
elif Shell == "\r" or Shell == "\n" or Shell == "" or Shell == " ":
	Shell = input("3expl0it > ")