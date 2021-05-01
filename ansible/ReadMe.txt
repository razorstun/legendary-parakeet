Ansible is an open-source configuration management, software provisioning & application deployment toolset created by Michael DeHaan 2012, acccquired by Red hat INC 2015.

Core components of Ansible
-Extensivce libraries of modules available
-Ansible ececutable
-Ansible Playbook
-Ansible Inventories

Docker
-Container offfering that provides OS level Virtualization
-convinent means of bundling software, libraries & configuration data, into a consumable format

Lab Enviroment

Reference Linux OS: Ubuntu

-Install Docker
	Download get docker installation script: curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh get-docker.sh
	Add the user to docker group: sudo usermod -aG docker username
	Pull the docker-compose: sudo curl -L "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	Apply executable permissions to the binary: sudo chmod +x /usr/local/bin/docker-compose
	Test the installation: docker-compose --version
	
-Install Ansible Lab
	Please refer https://github.com/spurin/diveintoansible-lab/blob/master/README.md to create the lab/blob/master/README
	
SSH
SSH connectivity overview between two hosts
	-SSH session is requested
	-both the server exchange the SSH protocol version they support, if they are both compatable they both agree, otherwise no connection
	-key exchange information is shared
	-both negotiate session key using Diffie-Helman algorithm creating a symmetric key
	-encrypted session is established

ssh key is stored in '~/.ssh/known_hosts' and can be viewd by ls -a
There are two fingerprint for each connection because during ssh session establishment it captures fingerprint for both IP & hostname
to manually generate ssh key: ssh-keygen -H -F hostname/ipaddress

-To overcome entering password during each ssh session we can use private and public key concept.
	generate pub/pri key on control host 'ssh-keygen'
	it will bydefault generated at .ssh/ as id_rsa for private key & id_rsa.pub for public key
	copy the public key to the target hosts 'ssh-copy-id targetHostName@servername'
	To copy public key  on multiple host install sshpass 'sudo apt install sshpass'
		-store password in text file 'echo passsword > password.txt'
		-for user in ansibleUserName root
			do
				for os in hostname1 hostname2
				do
					for instance in  1 2 3 n
					do	
						sshpass -f passsword.txt ssh-copy-id -o StrickHostKeyChecking=no ${user}@{os}{instance}
					Done
				Done
			Done
	
Ansible Architecture and Design

Ansible configuration files
	Ansible refers to configuration files based on prioirity location
		/etc/ansible/ansible.cfg (Typically provided through packaged or system installation of Ansible)
		~/.ansible.cfg
		./ansible.cfg
		ANSIBLE_CONFIG
		
Ansible Inventories
	
	-Host file is a text file that contains list of target hosts
	-ping all target host inside hostfile and skip hostKeyChecking prompt: ANSIBLE_HOST_KEY_CHECKING=False ansible all -m ping
		or we can set the ANSIBLE_HOST_KEY_CHECKING=False as defaults in ansible.cfg file
	-To get the output printed as one line for each host add -o at the end of the ansible executable: ansible ubuntu -m ping -o
	-To list host	
		single: ansible hostname --list-hosts
		group: ansible groupname --list-hosts
		all: ansible all --list-hosts
	-we can use while card to run specific hosts: ansible ~centos.* -m ping 
	-to login host as root user we can set host as: 'hostname ansible_user=root' in hosts file
	-to check the user we have logged in target hosts we can use the command module and pass id as argument
		ansible all -m command -a 'id' -o
	-id command : https://www.geeksforgeeks.org/id-command-in-linux-with-examples/#:~:text=id%20command%20in%20Linux%20is,name%20and%20real%20user%20id.
	-in real scenerio we rather login as user and then give the sudo privilege to it: 'hostname ansible_become=true ansible_become_pass=password'
	-As standard sshd deamon runs on port 22, but we can configure the sshd on other port on target machine
		then change the host file as: 'hostname ansible_port=portNumber' or 'hostname:portNumber'
	-you can use command: "ansible hostname -m command -a 'grep Port /etc/ssh/sshd_config' -o" to confirm the target sshd deamon port
	-we can add the control host in inventory by 
		[control]
		controlHostName ansible_connection=local
	-we can define ranges for hostname in inventory if they share similarity
		[groupname]
		hostname[startRange:endRange]
	-we can mitigate the duplication of variables by defining the groupvars for same hosts	
		[group1]
		hostname[1:2]
		hostname3:portNumber
		[group1:vars]
		ansible_user=root
	-we can group similar group in inventories
		[group1]
		hostname1
		[group2]
		hostname2
		[group3:children]
		group1
		group2
	-we can also pass .yaml file for inventory
		---
		control:
			hosts:
				controlHostName:
					ansible_connevtion=local
		centos:
			hosts:
				hostname:
					ansible_port=2222
				hostname[2:3]
			vars:
				ansible_user=root
		...
	-we can also pass .yaml file for inventory
	-we can use -e to overwrite the variable in inventories
		ansible all -m ping -e 'ansible_port=22' -o

Ansible modules

-Setup module - the module is automatically executed, when using playbooks to gather useful information as variables, about remote targets.

-With ansible 2.10, the fully qualified name is ansible.builtin.Setup

- To run setup module: 
	Ansible hostname -m Setup





