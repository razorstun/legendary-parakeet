Linux file System
- linux file system is in tree Structures
- top is / root directory
    - home directory holds home directory for regular user
    - /bin - Stores Common Linux user command binaries
    - /boot - everything that requires for booing the system - bootable linux kernal and bootloader config files
    - /dev - files representing devices
    - /etc - Administrative Configuration files
    - /media - unlike /dev, /media is usually where removable media are mounted
    - /lib - directory contains kernel modules and those shared library images (the C programming code library) needed to boot the system and run the commands in the root filesystem, ie. by binaries in /bin and /sbin
    - /mnt - A place to mount external devices
    - /misc - A directory used to sometime unmount filesystem on request
    - /opt - directory structure used to store additional software
    - /proc - information about system resources
    - /root - the home folder for root user similar to administrator on windows
    - /sbin - contains Administrative commands binaries for the root user
    - /tmp - contains temp files used by running application
    - /usr - contains files pertaining to the user
    - /var - contains directories of variables data that could be used by various application

- ~ shows path to the current user home directory
- . .. are dir in each folder where . represent current directory and .. the parent directory

File extensions in linux
- file command tells us what kind of file we are dealing with - file filename.extension
- linux does not determine the file depending on the extension, instead it reads the header of each file

- to check multiple directory contents at once - ls directroy1/ directory2/ directory3/

Wildcards
- * - matches any piece of text - ls D*
- ? - matches for single character - ?.text
- [] - matches one place with the given options - ls file[0-9].txt - ls file[A-Z].txt - ls file[0-9][A-Z][a-z1234].txt
- globbing means using wildcards for file search

Creating files and folders
- touch - create a new blank files
- echo "sachin" > myname.txt - to redirect content in files
- mkdir -p bla/things/shablam - create the entirepath
- mkdir happy birthday creates 2 files - rather use mkdir "happy birthday"
- brace expansion - mkdir {JAN,FEB}_{2021..2023} - mkdir {JAN,FEB}_{2021..2023}/file{1..100} - ls {JAN,FEB}_{2021..2023}
- 

Delete files and folders
- rm -ri folder
- rmdir folder name - only deletes empty folder

Copy move and rename 

- cp file /destination - cp -r for folder
- mv oldfolder/ newfolder - to rename a folder 
    - mv ~/Documents/newfolder/ ./jackpot

Nano
- write out - search with backwards and case sensitive - spell checker - jump to line ctl+shift_underscore - undo\redo - get current position

Locate command
- locate pathname - locate -i pathname (caseinsesitive) - locate --limit 4 pathname (to limit the no of results) - locate -S (to get the database information where the files are saved)
    - mlocate database is updated once a day - locate --existing/-e path (to check if fils exist) - locate --follow path 
    - sudo updatedb to update mlocate database

FIND
- execute soffistegated search on the file System
- find from the current directory or the path if we provide
- find . -maxdepth 2 - find . -maxdepth 2 -type f/D
- find . -maxdepth 2 -name "patern"
- find . -maxdepth 2 -iname "patern"
- sudo find / -type f -size +100k -o -size +5M | wc -l
- sudo find / -type f -size +100k -o -size +5M -exec cp {} ~/Desktop/copy_here
- sudo find / -type f -size +100k -o -size +5M -name "filename"

VIEW files
- tac reads the whole file in reverse
- cat is used to concatenate files
- rev is used to reverse each line of a file
- less are the pager command in linux that helps us to page through
- head allows us to have a look at starting few lines of the file and tail is opposite - cat file[0-1].txt | head -n 5   -  head -n 20 filepath

sort 
- sort filename 
- reverse sort - sort -r filename - sort filename | tac
- to sort by the value of the whole no we give - sort -n filename - sort -nr filename
- to so only once for dublicate values - sort -u filename
- sort using keydef - ls -l /etc | head -n 20 | sort -k 5nr - sorting based on the dec files sizes - highest to lowest
- ls -lh /etc | head -n 20 | sort -k 5hr - sort by human readable data
- ls -lh /etc | head -n 20 | sort -k 5M

Searching file content
- GREP - it will search for whatever input we give it for lines that contain that particular piece of text that we will tell it to search for
- grep e hello.txt
- grep -c e hello.txt - to get the number of lines containing e in text file hello.txt
- grep -i word textfile - insensitive
- grep -v e hello.txt - not containing everything
- grep -i "e" file1 file2
-ls -F | grep -v "/"

File archiving and compression
- archiving files in linux comprise of two step - 1 making a tarball(it acts as a wrapper and holds all files in one place) - 2 compressing tarball
- tar -cvf ourarchive.tar *.txt - c(lets the tar command know that we want to create a new archive) - v(tell tar that we want feedback) - f(let the tar command accepts file) 
- tar -tf ourarchive.tar to read the tar file
- tar -xvf ourarchive.tar
- compression happens using compression algorithm
    -gzip - faster but has less compression power
    -bzip2 - compress file to more smaller size but takes time
- gzip ourarchive.tar - changes happens inplace - gunzip ourarchive.tar
- bzip2 ourarchive.tar - changes happens inplace - bunzip2 ourarchive.tar
- zip ourthing.zip file1 file2 file3
- tar -cvzf ourarchive.tar.gz file1 file2 file3 - to create tar and compress at the same time - z means using gzip compression algo
- tar -cvjf ourarchive.tar.bz2 file1 file2 file3 - to create tar and compress at the same time - j means using bzip compression algo
- tar -xvzf ourarchive.tar.gz
- tar -xvjf ourarchive.tar.gz

