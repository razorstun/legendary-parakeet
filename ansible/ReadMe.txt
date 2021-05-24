Ansible is an open-source configuration management, software provisioning & application deployment toolset created by Michael DeHaan 2012, acccquired by Red hat INC 2015.

Core components of Ansible
-Extensive libraries of modules available
-Ansible executable
-Ansible Playbook
-Ansible Inventories

Docker
-Container offfering that provides OS level Virtualization
-convinent means of bundling software, libraries & configuration data, into a consumable format

==============================================================================================================================

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

==============================================================================================================================

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

==============================================================================================================================

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

- file module
	- ansible all -m file -a 'path=/tmp/test state=touch'
	- ansible all -m file -a 'path=/tmp/test state=file mode=600'

- Copy module - copies a file from local or remote target, to a location on the remote computer - fetch module opposite of copy
	- ansible all -m copy -a 'src=/tmp/x dest=/tmp/x'
	- we can also pass files from remote system to remote system - with the inclusion of the argument remote_source=yes
		- ansible all -m copy -a 'remote_src=yes src=/tmp/x dest=/tmp/y'

- Command module - takes the command name followed by a list of space-delimited arguments
	- ansible all -a 'hostname' -o
	- ansible all -a 'touch /tmp/test creates=/tmp/test' - creates file only if it exists
	- ansible all -a 'rm /tmp/test removes=/tmp/test' - removes file only if it exists

- ansible-doc - use as a man command for all 

==============================================================================================================================

Ansible playbooks 
	- it is a scripting functionality that allows us to perform multiple actions across multiple of system using modules
	- can be written in YAML or JSON

- YAML - data-oriented language - start with --- and end with ... - # for comment - next line should be indented with 2 space
	- | to write multi line string to python and will add /n after each line
	- > for single line for multipleline string and gives .n at the end
	- >- for single line for multipleline string
	- booleans - false, False, FALSE, no, No, NO, off, Off, OFF similarly for ...
	- 	- list1
		- list2
		- list3
		or
		-[list1, list2, list3]
		will be treated as python list
	- we cannot use list and dictionary at the same time but we can have list in dictionaries
	- we can have list of dictionaries with list inside a dictionaries

- Ansible playbooks, breakdown of sections
	- A playbooks contains a list of plays denorted by - and each play contains dictionaries of Hosts, Vars, Tasks, Handlers, Roles
	- ansible-playbook playbookname.yaml to run the playbook
	- there are various target options like become connection gather_facts, user
	- we can check the time taken to run the playbook using time command at the start of the ansible-playbook command
	- we can pass the content directly into the copy command using the content:
	- we can declare a string in vars and pass it to the content: "{{ variable }}"
	- we can also pass the variable in ansible-playbook playbook.yaml -e 'variable="content inside\n"'
		-	---
			# YAML documents begin with the document separator ---
			
			# The minus in YAML this indicates a list item.  The playbook contains a list
			# of plays, with each play being a dictionary
			-
			
			# Hosts: where our play will run and options it will run with
			hosts: linux
			
			# Vars: variables that will apply to the play, on all target systems
			vars:
				motd_centos: "Welcome to CentOS Linux - Ansible Rocks\n"
				motd_ubuntu: "Welcome to Ubuntu Linux - Ansible Rocks\n"
			
			# Tasks: the list of tasks that will be executed within the playbook
			tasks:
				- name: Configure a MOTD (message of the day)
				copy:
					content: "{{ motd_centos }}"
					dest: /etc/motd
				notify: MOTD changed
				when: ansible_distribution == "CentOS"

				- name: Configure a MOTD (message of the day)
				copy:
					content: "{{ motd_ubuntu }}"
					dest: /etc/motd
				notify: MOTD changed
				when: ansible_distribution == "Ubuntu"
			
			# Handlers: the list of handlers that are executed as a notify key from a task
			handlers:
				- name: MOTD changed
				debug:
					msg: The MOTD was changed
			
			# Roles: list of roles to be imported into the play
			
			# Three dots indicate the end of a YAML document
			...

- Ansible playbook variables
	- we can access the child dictionary values by either using {{ dict.dict }} or {{ dict[dict]}}
	- we can access the list inside a dictionary using {{ dict.0 }} or {{ dict[0]}}
	- we can declare the list as inline or we can also declare inline dictionaries using - dict:
													[1,2,3,4]
													{key: value}
	- we can also pass a external variable file
	- we can prompt user for variable input
		- vars_prompt:
			- name: username
			  private: False
	- we cannot the pricate flag to true for asking for values such as passwords
	- we can also access the hostvars
		- ---
		-
		
		# Hosts: where our play will run and options it will run with
		hosts: centos1
		gather_facts: True
		
		# Vars: variables that will apply to the play, on all target systems

		# Tasks: the list of tasks that will be executed within the playbook
		tasks:
			- name: Test hostvars with an ansible fact and collect ansible_port, dot notation
			debug:
				msg: "{{ hostvars[ansible_hostname].ansible_port }}"

			- name: Test hostvars with an ansible fact and collect ansible_port, dict notation
			debug:
				msg: "{{ hostvars[ansible_hostname]['ansible_port'] }}"
		
		# Three dots indicate the end of a YAML document
		...
	- we can set the default if the hostvars does not exist - msg: "{{ hostvars[ansible_hostname].ansible_port | default('22') }}"
	- we can pass the extra variable as - -e {extra_vars: extra_vars}
	- we can also pass the entire avriable file as - -e @extra_va_file.yaml or json

Ansible gather
	- we can get the desired facts by passing the filter parameter with setup module - ansible centos1 -m setup -a 'filter=ansible_memfree_mb'
	- we can create our own facts that is not included in the setup module
		- by default expects to use /etc/ansible/facts.d
		- we can place our fact executable file under facts.d and then reload the setup file by setup: and get the custom facts
		- if we do not have the root user we can create ~/facts.d directory oneach host and add the facts executable inside that folder
			- then we can refresh the setup module using setup: /home/ansible/facts.data
			- get the custom facts

Jinja Templating
	- ansible uses jinja - it is a templating language
	- if, elseif, else
		- msg: >
				{% if ansible_hostname == "ubuntu-c" -%}
					This is  ubuntu-c
				{% elif ansible_hostname == "centos1" -%}
					This is centos1
				{% else -%}
					This is good old {{ ansible_hostname }}
				{% endif %}
		- we can check if a variable is defined and also set a variable
			- {% set example_variable = 'defined'%}
			  {% if example_variable is defined -%}
					defined
			  {% else -%}
					not defined
			  {% endif %}
		- we can use for loop in jinja to loop through each entry or in range and also 
			- {% for entry in ansible_interfaces -%}
				Interface entry {{ loop.index }} = {{ entry }}
			  {% endfor%}
			- {% for entry in range(1,11) -%}
				{{ entry }}
			  {% endfor%}
			- {% for entry in range(10,1,-1) -%}
			  	{% if entry == 5 -%}
				  {% break %}
				{% if entry is odd -%}
				  {% continue %}
				{% endif %}
				{{ entry }}
			  {% endfor%}
		- we can use ansible jinja2 filter - {{list | min }}, max, unique, differennce(list), random, urlsplit('hostname')
		- we can also use template engine to get our desired output - dest: "/tmp/{{ ansible_hostname}}_template.out"

==============================================================================================================================

Ansible Playbooks, Creating and Executing

- we can use yum, apt package to install package on remote system
- package module can be used for multiple os 
- uri module to run a particular url
- we can use th etemplate module to pass a file with using jinja templating 

Ansible  Playbook Deep Dive

- set_fact - dynamically add or change fact during execution
	- set_fact:
		our_fact: Ansible_Rocks
		ansible_distribution: "{{ ansible_distribution | upper}}"
	  when: ansible_distribution == "CentOS"

- pause - allow us to pause the playbook execution for certain period or until a specific prompt is acknowledged
	-  pause:
		seconds: 10
	- 	pause:
			prompt: please check or press enter to continue
	
- wait_for
	- wait_for:
		port: 80

- Assemble - allows configuration files to be broken into segments and concaenated to form a designation file
	-  assemble:
		src: conf.d
		dest: sshd_config

- add_host - allows us to dynamically add host while running the playbook
	- 	---
		# YAML documents begin with the document separator ---

		# The minus in YAML this indicates a list item.  The playbook contains a list
		# of plays, with each play being a dictionary
		-

		# Hosts: where our play will run and options it will run with
		hosts: ubuntu-c

		# Tasks: the list of tasks that will be executed within the play, this section
		# can also be used for pre and post tasks
		tasks:
			- name: Add centos1 to adhoc_group
			add_host:
				name: centos1
				groups: adhoc_group1, adhoc_group2

		# The minus in YAML this indicates a list item.  The playbook contains a list
		# of plays, with each play being a dictionary
		-

		# Hosts: where our play will run and options it will run with
		hosts: adhoc_group1

		# Tasks: the list of tasks that will be executed within the play, this section
		# can also be used for pre and post tasks
		tasks:
			- name: Ping all in adhoc_group1
			ping:

		# Three dots indicate the end of a YAML document
		...
	
- group_by - add hosts to group based on a key
	-	---
		# YAML documents begin with the document separator ---

		# The minus in YAML this indicates a list item.  The playbook contains a list
		# of plays, with each play being a dictionary
		-

		# Hosts: where our play will run and options it will run with
		hosts: all

		# Tasks: the list of tasks that will be executed within the play, this section
		# can also be used for pre and post tasks
		tasks:
			- name: Create group based on ansible_distribution
			group_by:
				key: "custom_{{ ansible_distribution | lower }}"

		# The minus in YAML this indicates a list item.  The playbook contains a list
		# of plays, with each play being a dictionary
		-

		# Hosts: where our play will run and options it will run with
		hosts: custom_centos

		# Tasks: the list of tasks that will be executed within the play, this section
		# can also be used for pre and post tasks
		tasks:
			- name: Ping all in custom_centos
			ping:

		# Three dots indicate the end of a YAML document
		...

- fetch - capture files from remote hosts

==============================================================================================================================

Dynamic Inventories

- Dynamic Inventory Key Requirements
	- Needs to be an executable file that can be executed from the command line
	- accept the command line options --list and --host hostname
	- returns a JSON encoded dictionary of inventory content when used with --list
	- returns a basic JSON encoded dictionary structure for --host hostname

- command module is the default module used when no module is passed

Register and when

- we can use register module to register context when executing a command
- 	---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-

	# Hosts: where our play will run and options it will run with
	hosts: linux

	# Tasks: the list of tasks that will be executed within the play, this section
	# can also be used for pre and post tasks
	tasks:
		- name: Exploring register
		command: hostname -s
		register: hostname_output

		- name: Show hostname_output
		debug:
			var: hostname_output.stdout

	# Three dots indicate the end of a YAML document
	...
- 	---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-

	# Hosts: where our play will run and options it will run with
	hosts: linux

	# Tasks: the list of tasks that will be executed within the play, this section
	# can also be used for pre and post tasks
	tasks:
		- name: Exploring register
		command: hostname -s
		when: ( ansible_distribution == "CentOS" and ansible_distribution_major_version == "8" | int >= 8 ) or
				( ansible_distribution == "Ubuntu" and ansible_distribution_major_version == "20" | int >= 8 )

	# Three dots indicate the end of a YAML document
	...
- 	---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-

	# Hosts: where our play will run and options it will run with
	hosts: linux

	# Tasks: the list of tasks that will be executed within the play, this section
	# can also be used for pre and post tasks
	tasks:
		- name: Exploring register
		command: hostname -s
		when: 
			- ansible_distribution == "CentOS" 
			- ansible_distribution_major_version | int >= 8
		register: command_register

		- name: Install patch when changed
		yum:
			name: patch
			state: present
		when: command_register.changed                     command_register is changed    or opposite      command_register is skipped
	# Three dots indicate the end of a YAML document
	...

Looping

- 	---
	# YAML documents begin with the document separator ---
	
	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-
	
	# Hosts: where our play will run and options it will run with
	hosts: linux
	
	# Tasks: the list of tasks that will be executed within the playbook
	tasks:
		- name: Creating user
		user:
			name: "{{ item }}"
		with_items: 
			- james
			- hayley
			- lily
			- anwen
	
	# Three dots indicate the end of a YAML document
	...
-	---
	# YAML documents begin with the document separator ---
	
	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-
	
	# Hosts: where our play will run and options it will run with
	hosts: linux
	
	# Tasks: the list of tasks that will be executed within the playbook
	tasks:
		- name: Removing user
		user:
			name: "{{ item.key }}"
			comment: "{{ item.value.full_name }}"
			state: absent
		with_dict: 
			james: 
				full_name: James Spurin
			hayley: 
				full_name: Hayley Spurin
			lily: 
				full_name: Lily Spurin
			anwen:
				full_name: Anwen Spurin
	
	# Three dots indicate the end of a YAML document
	...
-	---
	# YAML documents begin with the document separator ---
	
	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-
	
	# Hosts: where our play will run and options it will run with
	hosts: linux
	
	# Tasks: the list of tasks that will be executed within the playbook
	tasks:
		- name: Creating user
		user:
			name: "{{ item.1 }}"
			comment: "{{ item.1 | title }} {{ item.0.surname }}"
			password: "{{ lookup('password', '/dev/null length=15 chars=ascii_letters,digits,hexdigits,punctuation') | password_hash('sha512') }}"
		with_subelements: 
			- 
			- surname: Spurin
				members:
				- james
				- hayley
				- lily
				- anwen
			- surname: Darlington
				members:
				- freya
			- surname: Jalba
				members:
				- ana
			- surname: Angne
				members:
				- abhishek
			- surname: Mahmood
				members:
				- sara
			- members
	
	# Three dots indicate the end of a YAML document
	...
-	---
	# YAML documents begin with the document separator ---
	
	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-
	
	# Hosts: where our play will run and options it will run with
	hosts: linux
	
	# Tasks: the list of tasks that will be executed within the playbook
	tasks:
		- name: Creating user directories
		file:
			dest: "/home/{{ item.0 }}/{{ item.1 }}"
			owner: "{{ item.0 }}"
			group: "{{ item.0 }}"
			state: directory
		with_nested:
			- [ james, hayley, freya, lily, anwen, ana, abhishek, sara ]
			- [ photos, movies, documents ]
	
	# Three dots indicate the end of a YAML document
	...
- ---
		# YAML documents begin with the document separator ---

		# The minus in YAML this indicates a list item.  The playbook contains a list
		# of plays, with each play being a dictionary
		-

		# Hosts: where our play will run and options it will run with
		hosts: linux

		# Tasks: the list of tasks that will be executed within the play, this section
		# can also be used for pre and post tasks
		tasks:
			- name: Exploring register
			command: hostname -s
			register: hostname_output

			- name: Show hostname_output
			debug:
				var: hostname_output

		# Three dots indicate the end of a YAML document
		...
		-	---
		# YAML documents begin with the document separator ---
		
		# The minus in YAML this indicates a list item.  The playbook contains a list
		# of plays, with each play being a dictionary
		-
		
		# Hosts: where our play will run and options it will run with
		hosts: linux
		
		# Tasks: the list of tasks that will be executed within the playbook
		tasks:
			- name: Create authorized key
			authorized_key:
				user: james
				key: "{{ item }}"
			with_file:
				- /home/ansible/.ssh/id_rsa.pub

		# Three dots indicate the end of a YAML document
		...
-	---
	# YAML documents begin with the document separator ---
	
	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-
	
	# Hosts: where our play will run and options it will run with
	hosts: linux
	
	# Tasks: the list of tasks that will be executed within the playbook
	tasks:
		- name: Create sequence directories
		file:
			dest: "/home/james/sequence_{{ item }}"
			state: directory
		with_sequence: start=0 end=100 stride=10

	# Three dots indicate the end of a YAML document
	...
-	---
	# YAML documents begin with the document separator ---
	
	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-
	
	# Hosts: where our play will run and options it will run with
	hosts: linux
	
	# Tasks: the list of tasks that will be executed within the playbook
	tasks:
		- name: Create random directory
		file:
			dest: "/home/james/{{ item }}"
			state: directory
		with_random_choice:
			- "google"
			- "facebook"
			- "microsoft"
			- "apple"

	# Three dots indicate the end of a YAML document
	...
-	---
	# YAML documents begin with the document separator ---
	
	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-
	
	# Hosts: where our play will run and options it will run with
	hosts: linux
	
	# Tasks: the list of tasks that will be executed within the playbook
	tasks:
		- name: Run a script until we hit 10
		script: random.sh
		register: result
		retries: 100
		until: result.stdout.find("10") != -1
		# n.b. the default delay is 5 seconds
		delay: 1

	# Three dots indicate the end of a YAML document
	...

Asynchronous Jobs

-	---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-

	# Hosts: where our play will run and options it will run with
	hosts: linux

	# Vars: variables that will apply to the play, on all target systems
	vars:
		jobids: []

	# Tasks: the list of tasks that will be executed within the play, this section
	# can also be used for pre and post tasks
	tasks:
		- name: Task 1
		command: /bin/sleep 5
		async: 10
		poll: 0
		register: result1

		- name: Task 2
		command: /bin/sleep 5
		async: 10
		poll: 0
		register: result2

		- name: Task 3
		command: /bin/sleep 5
		async: 10
		poll: 0
		register: result3

		- name: Task 4
		command: /bin/sleep 30
		async: 60
		poll: 0
		register: result4

		- name: Task 5
		command: /bin/sleep 5
		async: 10
		poll: 0
		register: result5

		- name: Task 6
		command: /bin/sleep 5
		async: 10
		poll: 0
		register: result6

		- name: Capture Job IDs
		set_fact:
			jobids: >
					{% if item.ansible_job_id is defined -%}
					{{ jobids + [item.ansible_job_id] }}
					{% else -%}
					{{ jobids }}
					{% endif %}
		with_items: "{{ [ result1, result2, result3, result4, result5, result6 ] }}"

		- name: Show Job IDs
		debug:
			var: jobids

		- name: 'Wait for Job IDs'
		async_status:
			jid: "{{ item }}"
		with_items: "{{ jobids }}"
		register: jobs_result
		until: jobs_result.finished
		retries: 30

	# Three dots indicate the end of a YAML document
	...
-	for updating on varios system we use serial
-	---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-

	# Hosts: where our play will run and options it will run with
	hosts: linux
	gather_facts: false
	serial: 
		- 1                     - 16%						- free
		- 2						- 34%
		- 3						- 50%

	# Tasks: the list of tasks that will be executed within the play, this section
	# can also be used for pre and post tasks
	tasks:
		- name: Task 1
		command: /bin/sleep 1

		- name: Task 2
		command: /bin/sleep 1

		- name: Task 3
		command: /bin/sleep 1

		- name: Task 4
		command: /bin/sleep 1

		- name: Task 5
		command: /bin/sleep 1

		- name: Task 6
		command: /bin/sleep 1

	# Three dots indicate the end of a YAML document
	...

Task delegation -  

Magic variables
-	---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-

	# Hosts: where our play will run and options it will run with
	hosts: all

	# Tasks: the list of tasks that will be executed within the play, this section
	# can also be used for pre and post tasks
	tasks:
		- name: Using template, create a remote file that contains all variables available to the play
		template:
			src: templates/dump_variables
			dest: /tmp/ansible_variables

		- name: Fetch the templated file with all variables, back to the control host
		fetch:
			src: /tmp/ansible_variables
			dest: "captured_variables/{{ ansible_hostname }}"
			flat: yes

		- name: Clean up left over files
		file: 
			name: /tmp/ansible_variables
			state: absent

	# Three dots indicate the end of a YAML document
	...

- Blocks -  allow us to group number of tasks into single groups
-	---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-

	# Hosts: where our play will run and options it will run with
	hosts: linux

	# Tasks: the list of tasks that will be executed within the play, this section
	# can also be used for pre and post tasks
	tasks:

		- name: Install patch and python-dns
		block:
			- name: Install patch
			package:
				name: patch

			- name: Install python-dnspython
			package:
				name: python-dnspython

		rescue:
			- name: Rollback patch
			package:
				name: patch
				state: absent

			- name: Rollback python-dnspython
			package:
				name: python-dnspython
				state: absent

		always:
			- debug:
				msg: This always runs, regardless

	# Three dots indicate the end of a YAML document
	...

Vault - E/D Variables - E/D files - Re-Encrypting Data - Using Multiple vaults  
- ansible_vault encrypt_string --ask-vault-pass --name 'ansible_become_pass' 'password'
- ansible-vault encrypt filename
- ansible-vault decrypt filename
- ansible-vault rekey filename
- ansible-vault view filename
- 	echo vaultpassword2 > password_file
	ansible-vault view --vault-password-file password_file external_vault.yaml
- ansible-vault encrypt --vault-id vars@prompt external_vault_vars.yaml
- ansible-vault encrypt-string --vault-id ssh@prompt  --name 'ansible_become_pass' 'password'
- ansible-playbook --vault-id vars@prompt --vault-id ssh@prompt vault_playbook.yaml
- we can also encrypt the entire playbook and pass playbook@prompt while running

=============================================================================================================

Structuring Ansible Playbooks

- we can use include_tasks and import_tasks to add playbooks to playbooks
- import_tasks are static and processed as the playbooks are parsed
- include_tasks are dynamic and processed at the playbooks execution
- ---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	-

	# Hosts: where our play will run and options it will run with
	hosts: centos1

	# Tasks: the list of tasks that will be executed within the play, this section
	# can also be used for pre and post tasks
	tasks:

		- debug:
			msg: ===================== Testing include_tasks =====================

		# include_tasks is dynamic
		#
		# The when statement is executed once, if the condition is met, all
		# tasks are executed
		- include_tasks: include_tasks.yaml
		when: include_tasks_var is not defined

		- debug:
			msg: ===================== Testing import_tasks ======================

		# import_tasks is static
		#
		# Each task that in the include will be independently executed against
		# the when condition
		- import_tasks: import_tasks.yaml
		when: import_tasks_var is not defined

	# Three dots indicate the end of a YAML document
	...

Tags - aliases for a tasks
- 	tasks:
		tag-name 
- 	ansible-playbook playbook_name --tags "tag1-name,yag2-name"      - we can use tags to run a specific tasks from a playbook	
- 	ansible-playbook playbook_name --skip-tags "tag1-name,yag2-name" 
- 	we can also add tags to entire playbooks
-	tags: always makes sure that the task runs even if it is not called
-	tags: tagged only run tasks that are tagged
- 	tags: untagged
-	tags: all

Roles - allow us to structure and group our playbook taska into associated components into a role for ease of consumption
- Role-name
	- README.md
	- defaults
		- main.yml 
	- files
	- handlers
		- main.yml
	- meta
		- main.yml
	- tasks
		- main.yml
	- templates
	- tests
		- inventory
		- test.yml
	- vars
		- main.yml
- we can use (ansible-galaxy init rolename) to create a skeleton of roles
- 	---
	# YAML documents begin with the document separator ---

	# The minus in YAML this indicates a list item.  The playbook contains a list
	# of plays, with each play being a dictionary
	#
	-

	# Hosts: where our play will run and options it will run with
	hosts: linux
	
	# Roles: list of roles to be imported into the play 
	roles:
		- nginx
		- { role: webapp, target_dir: "{%- if ansible_distribution == 'CentOS' -%}/usr/share/nginx/html{%- elif ansible_distribution == 'Ubuntu' -%}/var/www/html{%- endif %}" }

	# Three dots indicate the end of a YAML document
	...
-	we can add dependicies fr role using dependicies: -role name

=======================================================================================================

AWS with ANSIBLE

