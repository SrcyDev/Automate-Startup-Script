# Automate-Startup-Script
Automate Scripts in Python.

## How to use

1. Open a editor and open the script in it.
2. Navigate to line `14` and write the name of your program inside the double quotes of the paranthesis of `command = os.system("")`.
3. The default will be `bash`. Change it to the program name.
4. If you want to use multiple programs, copy the command and paste it.
5. Now execute it. The script should launch the programs specified.
   If it does not do it, then check if it is present in /usr/bin.
6. For automatic launch at System Start, Open terminal.
7. Do `crontab -e` and choose option `1`.
8. Now navigate to the bottom line and write `@reboot <file location>`. For me its `/mnt/sda2`.
9. Press `Ctrl + O` in your keyboard and press `Enter`. Now press `Ctrl + X`.
10. Reboot the system to see the result.   
