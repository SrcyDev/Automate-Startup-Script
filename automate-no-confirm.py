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
	command = os.system("bash")



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

def loading_text():
	print("\u001b[32mLoading...\u001b[0m")
	for i in range(0, 100):
       		time.sleep(0.1)
        	sys.stdout.write("\u001b[32D" + str(i + 1) + "%")
        	sys.stdout.flush()
	print


loading_text()
print("\n")
cmd()

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
