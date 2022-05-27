######################################## WELCOME TO AUTOMATION SCRIPT############################################################
## This is a template for your automating script. You can use this to execute things automatically by launching it in startup. ##
## This is made and tested for Linux. This may work but I can not gurrantee it.                                                ##
## I will appreciate any help. I hope you will enjoy it.                                                                       ##
################################################################################################################################# 

## Enter your commands here like command = os.system("<program name>")
## Copy and paste this if you want to use multiple programs.
## Make sure they are present in /usr/bin or are added to path.
## Else it would not work.
## Dont forget to put double quotes ("")
## The default is "bash" for testing purposes

def cmd():
	command = os.system()



## Dont edit this unless you know what are you doing

print('''
░█████╗░██╗░░░██╗████████╗░█████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
███████║██║░░░██║░░░██║░░░██║░░██║██╔████╔██║███████║░░░██║░░░██║██║░░██║██╔██╗██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██║██║╚████║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

░██████╗░█████╗░██████╗░██╗██████╗░████████╗
██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝
╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░
░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░
██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░ ''')


import os
import time
import sys


## This runs one time only. In order to use it again the next function is defined.
## I was not able to loop it. I will gladly accept any help about this.

print("\u001b[36mDo you want to execute the script ?")
startup_prompt = input("\u001b[32mconfirm\u001b[31m> ").lower()

def restart_script():
	print("\u001b[36mDo you want to execute the script ?")
	startup_prompt = input("\u001b[32mconfirm\u001b[31m> ").lower()

## Loading Text

def loading_text():
	print("\u001b[31mLoading...")
	for i in range(0, 100):
       		time.sleep(0.01)
        	sys.stdout.write(u"\u001b[500D" + str(i + 1) + "%")
        	sys.stdout.flush()
	print

## Input
## This checks for any possible input to prevent errors.
## This done if you somehow misclick or put a wrong name 
## which can lead to errors of some kind.
## Use the no-confirm script if you do not want this.

if startup_prompt == "yes" or startup_prompt == "ye" or startup_prompt == "y":
	print("\u001b[33mStarting...")
	loading_text()
	print("\n")
	cmd()
	print("\n\u001b[32mDone.... ")
	print("\u001b[32mOperation Succesful\u001b[0m")
elif startup_prompt == "no" or startup_prompt == "n":
	print("\u001b[31mExiting...\u001b[0m")
	quit()
else:
	print("\u001b[31mInvalid. Try again.\u001b[0m")
	restart_script()
#### END SCREEN ####
print('''
████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
''')
#### END ####
