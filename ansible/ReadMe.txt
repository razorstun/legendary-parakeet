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
	
	coming....
