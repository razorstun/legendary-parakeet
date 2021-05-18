Creating bash script
- nano our_script.sh
- we add shabang #! /bin/bash on the first line - #! tells the linux that do not read this file as a text file instead to intepret it as a script
- we run the bash file with - bash filename.sh
- /dev/n$ - is a place on the linux system called the bit bucket that deletes everything that it recieves
- its a standard that we create a bin folder in our home directory and save our bash script there
    - to make the bash file run as a command from the terminal we can use chmod
    - chmod is the command in linux that can be used to change the permissionn on the file
    - chmod -x bashScriptExecutable
    - to make the command available globally we can add PATH="$PATH:$HOME/bin" at the end of the .bashrc file in our home directory

cron
- is a commandline based program that is used to schedule takes
- each user has a crontab that is a text file that lists which command/task will be run by the user and also lists the schedule 
- crontab -e to open the crontab
- min hours DOM MON DOW command
- 0,15,30 or */15 > run evry 15 min
- */3
- 59 23 * JAN,DEC SUN
