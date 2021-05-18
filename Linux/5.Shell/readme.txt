Linux
- A Linux distribution/flavor/distro is the linux kernal and a collection of software that together creates an OS
- Centos is a REDHAT Linux derivative thats completely free
- A shell is a command line interpreter and a progeam that accepts your commands and executes those commands
- $ at prompt means you are loggedin as a normal user - whereas # means you are loggedin as a root user
- permissions are categorzed as - u user, g group, o others, a all
- file and directory permissions -rw-r--r--, first - is the type,  rw- user/file owner, r-- group, r-- others
- chmod - ugoa - +-= - rwx - chmod u+rwx, g-x filename
- octal and binary permission notation - 0 1 10 11 100 101 110 111/0-7
- chgrp groupname filename - to change the group on the file
- umask is used by system calls that creates files to modify the permissions created on newly created files and directories - default is 0002
- wildcards - [!aeiou]* to not include first word as aeio or u - naed character classes [[:alpla:]],alnum,digit,lower,space,upper - to add wildcards as pattern \*
- comparing files - diff sdiff vimdiff
- copying files over network using SCP or SFTP - ftp is not secure - scp filename username@remoteServerName:directorypath - smpt servername
- Enviroment variable is a key:value pair that affects working of various application - printenv to check all EV or printenv EV name to see specific - to create a enviroment variable export VAR="value" - to remove the Ev unset variablename
- to list the running process - ps command - ps -e for all process - ps -f to show in full list format - ps -u usename - ps -p pid display inforation for sprcific pid
- only ps gives the session that are only attached to my current session - ps -e --forest to see the process in tree format
- pstree to list the process in tree format
- top to look at the process in interactive way - kill command to kill the process
    - command & - & at the end of the command send the command running in the background
    - jobs command to send a foreground process in the backgroud
    - jobs %1 to look into the specific bg running jobs
    - fg to bring the job in foreground - fg %1 - or simply proovide the job number - %1 
    - to look at jobs - jobs %% for the current job - job %+ for the next job - job %- for the previous job
    - kill %1 to klill job 1
    - kill -l to get a list of all the signal that a kill can pass - bydefault kill passes signal 15 SIGTERM - kill -kill or kill 9 to kill a hard job
- su username to get become the newuser and pass our enviroment variable to interactive
    - su - username become new user but do not pass our enviroment variable
    - to run a command as another user - su -c 'command' - username
    - sudo -u username command
    - sudo su - switch to superuser account
    - sudo su -    with root enviroment
    - sudo su - username     switch to the username account
    - We can change the sudo configuration using command visudo in path /etc/sudoers

BOOT process
- BIOS  - Basic input output system
        - it is a special type of firmware that is used while booting the system, first piece of software suuwhile booting the computer on
        - it OS independent
        - Primary purpose is check the hardware and execute the bootloader
        - Performs the POST
        - BIOS contains the list of bootable devices - searches that list for the bootable devices
        - once the boot device is found the bios will run the bootloader
        - bootloader can be LLO(linux loader) or GRUB(grand unified bootloader)
        - primary purpose of the bootloder is to start the OS
        - initrd - initial RAM disk -temorary filesystem that is loaded into the memory from the disk
        - it contains the helpers and modules required to load the permanent OS file system
        - INITRD will have the kernal module to mount the logical volume as the root file system
        - /boot contains the files required to boot Linux as initrd - kernal - boot loader configuration
        - Kernal Ring Buffer - contains message from the linux Kernal - dmesg - var/log/dmesg
        - RUNLEVELS - linux uses runlevels to determine what process and services to start
            - 0 to shutdown,1 single uesr mode.Used for maintenance,2-5 Multi user mode,6 reboot
            - traditionally runlevels are controlled by initial
        - Systemd - uses targets instead of runlevels
        - To change runlevels or targets use telinit 5 or systemctl isolate graphical.target resp

Logging
- Linux uses syslog standards to for message Logging
- Syslog uses facilities and severities to categorze messages
- each message is labeled with facilities codes and severity levels
- facilities are used to indicate what type of program or what part of the system the message originated from
- each facilities include a number and keyword accociated with it
- severity code are 0-7 with 0 as emergencyand least 7 as debug - each code explains the severity and keyword associated with it
- Syslog servers - these servers process messages based on the rules - syslogd, rsyslog, syslog-ng
    - configuration for the rsyslog can be found in /etc/rsyslog.configuration
- Logging rules consist of the two fields - Selector field and Action field
    - Caching and nonCaching
    - caching can be used if the path starts with a hypen - mail.info -/var/log/mail.info
    - you may lose some messages while using caching mode while system crash, but it improves the I/O performance
    - we can add a log message using logger - logger -p mail.info -t mailtest "Test"
        - p means facility and severity pair
        - t to tag
        - we can check the log at /var/log/ - /var/log/mail.log
    - we can use logrotate to rotate compress or move the log files, so the log file does not eat up much space in your system
    - /etc/logrotate.conf 

Disk Management
- Disks can be divided into parts called partitions
- Partitions allow you to seperate data
- Partitioning schemes
    - OS Application User Swap
    - OS User home directories
- MBR - Master Boot Record - is a boot sector at the beginning of a storage device
    - Logical table reciding in the MBR contains information on how the logical partitions are organized on the disk
    - MBR can only address address space upto 2TB
    - it allows only upto 4 primary partitions
    - extended partitions can be used to create further logical partitions
- GPT - GUID Partitions table - GUID(Global unique identifier)
    - it replaces the MBR partitions schemes
    - supports upto 128 partitions
    - supports upto 9.4ZB
Mount Points
- a directory used to access the data ona partitions
- at the very least there will be one partitions mounted at /
- fdisk utility is used to create and modify partitions on the disk\
- fdisk -l to get all disk

- we can create the partitions using the fdisk partitionname
- after creating the patitions we need to format the partitions into file system so that linux can use it
- mkfs can be used to format a partition - mkfs -t TYPE DEVICE or mkfs.TYPE DEVICE
- to mount a device use the mount command - mount DEVICE TARGETDEVICE
- df command shows the mount Points
- manually mounting a FS from commandline does not make it persists between reboots
    - add entry in the /etc/fstab file
- to unmount use umount command - unmount DEVICE
- /etc/fstab contains what device get mounted and where on boot - each entry is made up of 6 fields - device, mount point, file system type, mount options,dump, fsck order

LVM - logical volume manager adds a layer of abstraction between the storage devices and the file system placed on those storage devices
- 1 Layer of abstraction is the Physical Volumes
- 2 Volume group - Pool of storage
- 3 logical volumes - created using volume group
- lvmdiskscan - shows all the storage decvices that have the ability to be used with LVM
- pvcreate storagedevicename - initializes the disk to be used by LVM
    - pvs to list the PV
    - vgcreate vg_app /dev/sdb
    - vgs to view the volume group
    - lvcreate -L 20G -n lv_data vg_app
    - we can then format vg_app using mkfs -t ext4 /dev/vg_app/lv_data
    - then we can create a mount point - /data - mount /dev/vg_app/lv_data /data
    - we can add PV to a volume group by vgextend vg_app /dev/storagedevicename
    - similarly lvextend -L +5G -r /dev/vg_app/lv_data
    - if we forgot to give -r the LV will will increase but the Filesystem will remain as it is - we can use resize2fs LVpath to resize it again
    - we can mirroe the logical volumes by lvcreate -L 50M -m1 -n mirrorlv datavg
    - now how to remove
        - unmount /secrets
        - lvremove /dev/vg_safe/lv_secrets
        - vgreduce vg_safe /dev/sde
        - pvremove /dev/sde
        - vgremove vg_safe
        - pvmove /dev/sdb /dev/sde

User Management
- All user information is stored in /etc/passwd file
- first entry is the root account - root:x:0:0:root:/root:/bin/bin
- 1username:2password:3UID:4GID:5comments:6home_dir:7shell
- passwords are stored in /etc/shadow
- encrypted passwords are stored in /etc/shadow and is only readable by root
- newgroup command to change group
- comments fields also called GECKO field
- The shell will be executed when a user logs in - a list of available shells are in /etc/shells - to prevent interctive use of an account, use /usr/sbin/nologin or /bin/false as the shell
- useradd -c "Sachin Negi" -m -s /bin/bash sachin - passwd sachin
- useradd -c "Eddie Harris" -m -s /bin/bash -g sales -G projectx eharris - passwd eharris
- useradd -c "Apache Web Server User" -d /opt/apache -r -s /usr/sbin/nologin apache
    - when using the -m option the home directory for the account is created and the content of /etc/skel are copied to the home directory - it tipically contains shell configuration files
- useradd -c "MySQL Server" -d /opt/mysql -u 97 -r -s /usr/sbin/nologin mysql
- userdel eharris - userdel -r grant - -r deletes the user home directory
- usermod to update the user
- /etc/group - sales:x:1001:john,mary - groupadd -g 2500 web - group db - (groupmod -g GID -n GROUP) - 

Networking
- TCP/IP - is responsible for maintaining the session so that two devices can share data with each others
    - IP sends data from one device to another over network
    - For a device to communicate properly over a network it needs
        - IP address
        - Subnet mask
        - broadcast address
        - Ip address consist of two parts network address(what network the host belongs to) and the host address(the specific device the data needs to sends to)
        - class a IP address  - first octet - 1.0 -> 127 - 255.0.0.0
            - B 128.0 -> 191.255 - 255.255.0.0
            - C 192.0.0 -> 233.255.255 - 255.255.255.0
        - A broadcast address is a special address used to send data to all host over given address 
        - CIDR - it allows networks to be subdivided regardless of their traditional class
        - Ranges of ipaddress reserved to be used in private space - replaces
            - A 1.0.0.0-127.255.255.255 - 10.0.0.0-10.255.255.255
            - B 128.0.0.0-191.255.255.255 - 172.16.0.0-172.31.255.255
            - C 192.0.0.0-233.255.255.255 - 192.168.0.0-192.168.255.255
- ip addr to get our ip and the list of all the ip used in our system
    - lo - loopback device - a special virtual network interface that a linux system uses to communicate to itself 127.0.0.1
    - eth0 - actual hhdware device
    - DNS primary purpose is to translate humanreadable names into ipaddresses and reverse
    - FQDN - it contains the subdomain domain name and the top level domain name
    - TLD - .com .net .org
    - subdomain - webprod01.ny.us.mycompany.com
    - hostname - hostname -f
    - we can temporiraly change the hostname of a system - hostname webprod01 - but to make this persistant over reboot - /etc/hostname
    - we can use host or dig to resolve DNS names
    - /etc/hosts file contains lists of ipaddress and the hostname
    - we can change the /etc/nsswitch.conf file to change the order the ipaddress is resolved
- Network Ports identify the servies on a host
    - When a service starts starts it binds itself to a Ports
    - 1-1023 are well known Ports
    - 22 SSH, 25 SMTP, 80 HTTP, 143 IMAP, 389 LDAP, 443 HTTPS
    - we can edit /etc/services to map port name to port numbers
    - DHCP
    - To bring the network interface up and down we can use ifup and ifdown
- Network troubleshooting
    - ping comand sends 1 or more icmp packets to the host we provide to reply - ping -c COUNT host
    - traceroute -n google.com
    - tracepath -n google.com
    - netstat commands can be used to collect wide variety of network information
    - tcp dump is a packet sniffing troubleshooting
    - telnet to initiate a tcp connection to a host on specific port

- Special modules
    - Setuid - set User ID upon execution 
        - there is s bit in owner permission of the /usr/bin/passwwd file because it need the root user permission for /etc/passwd
        - chmod 4755/u+s /path/to/file - to remove - chmod 0755/u-s /path/to/file
    - Setgid - it allows file to execute using the group priviledge of the file rather ththe users group privilidge
        - chmod 2755/g+s /path/to/file - to remove - chmod 0755/g-s /path/to/file
    - Sticky - Use on a directory to only allow the owner of the file/directory to delete it
        - chmod 1755/o+t /path/to/file - to remove - chmod 0755/o-t /path/to/file
    - we can use the tripwire to check the file integrity

- Scripting
    -   mu_variable = "SACHIN"
    -   if []
        then
            command
        elif
            command
        else
            command
        fi
    -   for Variable_name in item_1 item_n
        do
            command1
            command2
        done
    -   PICTURES = $ (ls (*jpg))
        DATE=$ (date +%F)

        for PICTURE in PICTURE
        do  
            echo "Renaming ${PICTURES} to ${DATE}-${PICTURES}"
            mv ${PICTURE} ${DATE}-${PICTURES}
        done
    -   taking input - read -p "PROMPT" variable
- !! is event designator refering to the most recent command in shell history
- !u - to run the previous command starts with u 


    
