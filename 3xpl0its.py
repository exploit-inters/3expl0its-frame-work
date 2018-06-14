#!/usr/bin/python
#Welcome to 3xpl0its.py

'''
imports
'''

import sys
import os
import random
import telnetlib
from time import *

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
		                   Code Name:  RED BLOOD
	''' + color.END
	
def clearscr():
		os.system('cls')
		
clearscr()

expl0itsmenu = color_random[1] + '''
           [0]	Set Exploit Host
	   [1]	Set Router Exploit Host
	   [2]	Set Exploit Host Port
	   [3]	Set Router Exploit Port
	   [4]	List currunt Exploits in DB
	   [5]	print Set Var's
	   [6]	More
	  [98]	Reload & clear screen
	  [99]	Exit
	   ''' + color.END
	   
def Exit():
	print("Have a good day!")
	exit


def RHOST():
	print("\n")
	RHOST = raw_input("IP: ")

def RRHOST():	
	print("\n")
	RRHOST = raw_input("Router Exteral IP: ")
		
def RHOSTPORT():
	print("\n")
	print("Defalt Port: 80")
	RHOSTPORT = raw_input("Port: ")
	
def RRHOSTPORT():
	print("\n")
	print("Defalt Port: 80")
	RRHOSTPORT = raw_input("Port: ")
	
RHOSTPORT = 80
RRHOSTPORT = 80

def Home():
	clearscr()
	print(logo)
	print(expl0itsmenu)
	
def printvars():
	print("\n")
	print('Router IP: ')
	print('Router Port: ')
	print('Host IP: ')
	print('Host Port: ') 
	
'''
code
'''

print(logo)
print(expl0itsmenu)

while 1 <= 3:
	Shell = input("3expl0it > ")
	if Shell == 0:
		RHOST()
	elif Shell == 1:
		RRHOST()
	elif Shell == 2:
		RHOSTPORT()
	elif Shell == 3:
		RRHOSTPORT() 
	elif Shell == 4:
		ListDB()
	elif Shell == 5:
		printvars()
	elif Shell == 6:
		menu2()
	elif Shell == 98:
		Home()
	elif Shell == 99:
		Exit()
	elif Shell == "\r" or Shell == "\n" or Shell == "" or Shell == " ":
		Home()
	