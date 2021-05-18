The GNU Project
- Linux is just the one of the piece of whole our_script
- Sep 1983 - Richard Stallman announces GNU Project
- JAN 1984 - Stallman quits MIT to work on GNU full time

free software - 4 freedom
    - to run program as you wish
    - to study how the program works, and change it(access to source code is a pre condition)
    - to redistribute
    - to distribute the copies of the modified versions to others(access to source code is a pre condition)

GNU public licence(GPL) - licence that provides the user with these 4 freedom

1991 - GNU Almost Complete the OS noly one part was missing - that was the kernal - kernal is responsible for allocating the resources on the computer hardware that is required by the software running - is is an interface between the hardware and the OS software
    - 1991 - Linus Torwals - invented a unix like kernal called the Linux - Linus released Linux Kernal under GPL v2.0
    - uname is get linux config
    - all the commands were provided by the linux
    - all the GNU commands can be find under coreutils  package and the linux kernal under linux-libre

Comping software from the source code
- download latest stable source code from GNU.org
- unzip the tar
- go to the extracted folder inside src - edit the c file for the particular command
- install gcc to compile the newly edited command
- run bash configure to configure the c file as per our architectur
- it generates makesfile - in order to run the make file install make
- run make
- sudo make install
- revert to the changes
- make && sudo make install

Repositories
- ubuntu has 4 Repositories - MAIN, Universe, Restricted, Multiverse
- check codename for our distribution - lsb_release -a
- APT
    - apt-cache search packagename - to search the package
    - apt-cache show packagename - to get the details of the package
    - /var/lib/apt/lists
    - list in the cache get there by the servers on the internet
    - sudo apt-get update - to update the cache
    - sudo apt-get upgrade - to update all the packages on the system
    - sudo apt-get install packagename - to install any package
    - sudo nano /etc/apt/sources.list - in order to make changes in the source code of the packages we have to make changes of to the {} file and uncomment all deb-sec line
        - it activates the ability of our packagemanager to dowmload the sources of the packages
        - then run sudo apt-get update
        - to download the source code we have to install one more package - sudo apt-get install dpkg-dev - sudo apt-get source packagename
    - sudo apt-get remove packagename - but the configuration files that comes with the packages remains - use this only if you have to install this package in future
        - sudo apt-get purge packagename
        - sudo apt-get autoremove - it automatically removes any dangling dependicies that are not required
        - whenever we install a package the copy of the package is stored  locally on the system beacause of the 2 step process at
            - /var/cache/apt/archive
            - sudo apt-get clean
            - sudo apt-get autoclean -checks the pages that are no longer can be downloaded and removes that 

