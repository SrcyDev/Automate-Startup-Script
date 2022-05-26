######################################## WELCOME TO AUTOMATION SCRIPT############################################################
## This is a template for your automating script. You can use this to execute things automatically by launching it in startup. ##
## This is made and tested for Linux. This may work but I can not gurrantee it.                                                ##
## I will appreciate any help. I hope you will enjoy it.                                                                       ##
################################################################################################################################# 

#### START SCREEN ####
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

## This is where your command is executed.
## Use this like "command = os.system("<file>")
## Add multiple lines for multiple files you want to execute


def cmd():
	command = os.system("") # Enter your command(s) here

## Input
## This checks for any possible input to prevent errors. 
if startup_prompt == "yes" or startup_prompt == "ye" or startup_prompt == "y":
	print("\u001b[33mStarting...")
	loading_text()
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
