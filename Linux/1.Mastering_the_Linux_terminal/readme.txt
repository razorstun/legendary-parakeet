Basic terminal
- opening terminal shortcut - ctr+alt+t
- run the command in history at specific index - !8
- clear the histroy - history -c; history -w
- the command are just the text but when we press enter the text is intepreted by a computer program called shell
- terminal is like a middleware/window that takes the command and sends it to shell to intepret

Command structue
- commandName options inputs
- shell path - echo $PATH
- foreach command command shell checks for the command in aech path in the filepath
- which cal - to find where the command is stored
- input is called as operand
- we can chain the operand together
- longnames operand are proceeded by -- - date --universal
- command are case sensitive

Manual Structures
- User Commands
- System Calls
- C Library Functions
- Devices and special files
- File Format and Conventions
- Games
- Miscellaneous
- System Administrations

Reading the man pages
- man -k commandname
- in man page if some thing is inside [] it is optional
- anything inside <> is mandatory
- ... means we can pass multiple argument
- | means either operand can be used
- --help for command with no manual pages
- -l for long format is supported by many Commands

Command I/o
- A command can take 2 types of input standard 0Input/Command Argumests and give two types of output S 1Output/2S Error
- data streams can be flowed and piped together but the command line argument is static
- S Output/S Error are bydefault attached to termil window & S input tied to keyboard
- cat com is used to concatenate or stick together multiple different files
- 1> to redirect the output data stream. cat 1> abc.text
- 1>> to appending to a file is equal to >>
- to use both - cat 1>>file1 2>>file2
- to take the standard input from file cat 0< filename equavalent to <
- to use both in conjuction cat 0< file1 1> file2
- everything in linux is treated as a file, even each terminal, we can take input from one terminal and output to other terminal by getting the location of the terminal2 by tty command, it shows the location of the terminal
    - cat 1> terminal2Location
- to connect standard o to standard i of another we use pipe
- date | cut --delimiter " " --fields 1 > filename
- advance pipelines using tee and xargs
- tee allows us to pass the data in two direction\ take data snapshot - date | tee filename | cut --delimiter " " --fields 1 > filename
- some command does not take input from standard input but as a command line argument for that we use xargs
    - date | xargs echo

Aliases
- nickname for the pipelines
- create .bash_aliases in home directory. . makes the file hidden
- add alias - alias myname='echo "Sachin Negi"'
- reboot terminal and run myname


