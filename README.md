# Automate-Startup-Script
Automate Scripts in Python.

## How to use

## Config
1. Open a editor and open the script in it.
2. Navigate to line `14` and write the name of your program inside the double quotes of the paranthesis of `command = os.system("")`.
3. The default will be `bash`. Change it to the program name.
4. If you want to use multiple programs, copy the command and paste it.
5. Now execute it. The script should launch the programs specified.
   If it does not do it, then check if it is present in /usr/bin.

## For Automatic Startup at System boot.
1. Copy the script to `/usr/bin` or execute `sudo cp -i <script location> /bin`.
2. Open terminal.
. Do `crontab -e` and choose option `1`.
3. Now navigate to the bottom line and write `@reboot python /bin/<script-name.py> &`.
4. Press `Ctrl + O` in your keyboard and press `Enter`. Now press `Ctrl + X`.
5. Reboot the system to see the result.   
