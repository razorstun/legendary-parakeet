Why Docker
- released in 2013 by a company called host cloud 
- new restructured company Docker Inc
- Mainframe to PC - Baremetal to Virtual - Datacenter to Cloud - Host to Container(Serverless)
- https://landscape.cncf.io/


Docker basics ad install nginx
- docker info - most config values of engine
- docker version  verified cli can talk to engine
- Starting a NGINX web server
    - docker container run --publish 80:80 --detach --name webhost nginx
        - this will first let docker to find the nginx docker image locally, if not then pull the image from docker hub
        - create a container with name webhost run a process with nginx imge inside the container
        - publish will expose out local port 80 to conatiner port 80
        - detach will run the container in background
    - docker conatiner ls 
    - docker container stop firstFewNumberOfContainerID
    - docker container logs webhost - check logs on a container
    - docker container top webhost - check process running on a container
    - docker container rm $(docker container ls -aq) - to remove all stopped containers
    - docker system prune -af --volumes - removes all docker images
    - docker image ls - to get all local image

Containers vs VMs
- Container are just a process

- docker container top -process list in one container
- docker container inspect - details of one container config
- docker container stats - details od recources metrics

- docker cli is great substitute for adding ssh to containers
    - docker container run -it --name ubuntu ubuntu 
    - docker container start -ai ubuntu
    - docker container exec -it mysql bash
- alpine is the smallest linux distribution with apk as PM

========================================================================================================

Docker Network defaults

- each container connected to a private VN "bridge"
- each VN routes through NAT firewall on host IP

- docker network ls - show networks
- docker network inspect networkid - inspect a network
- docker network create --driver - attch a network to container
- docker network connect
- docker network disconnect

- docker bridge is the default network that bridges through the NAT firewall to the physical network the host is connected to
- host VN is a special network that skips VN of docker and directly attaches the container to the host interface
- none interface is the interface that is not attaches to anything

DNS naming in docker 
- docker uses container name as hostname to talk to each other but we can also set aliases

- we can use --rm command with docker container to create a container, test and destroys asa we exit
- we can set --net-alias for docker container with same name and achieve a LB

==========================================================================================================

image

- App binaries and dependicies and metadata about the image data and how to run the image
- An image is an ordered collection of root filesystem changes and the corresponding execution parameters for use within a container runtime

Docker hub

image layers

- docker image history imageName
- docker image inspect imageName

Docker tagging ad pushing to docker hub
- we change tag of existing image by - docker image tag tagnae newtagname
- docker login to login to docker hub
- the credentials ge stored in ~/.docker/config.json
- docker push/pull imagename - to push/pull images to and from dockerhub
- we can create a private/public repo on our docker hub account

Docker file basics

Creating docker file
- FROM - to specify a minimal linux distribution or FROM scratch to start with an empty container
- ENV - set optional EV that ca be used later in docker file
- RUN - optional command to run at shell inside container at build time
    - we can use ln to forward request and error logs to docker log collector
- WORKDIR - change the WD in Docker file
- EXPOSE - expose ports on docker virtual virtual network
- CMD - run this command when container is launched

Build docker image
- docker image build -t tagname dockerfilelocation

======================================================================================================

Container Lifetime and Persistant data

- Container are usually immutable and ephemeral
- to overcome problem in persistent data docker have two ways volume and bind mounts
- Volumes - creates a special locations outside the container union file system that stores unique data 
    - we can then mount these as a filepath to a new container
- Bind Mounts - sharing or mounting of host directory or file into a container

- Images like mysql have a VOLUME field mentioned in it that tells the docker to create a a seperate volume to store the persistent data while creating the container
- the new volume actually lives on a special location on host and is mounted on the container
- docker container inspect mysql
- docker volume ls
- bydefault docker volumes contains only unique id so we cannot differentiate them based on their past usuability
- so we use names volumes
    - docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql
- docker volume create - to create a volume ahead of time

- Bind mount is mapping of host file or directory into a container file or directory
- docker container run -d --name nginx -p 80:80 -v directoryfullpathonhost:containerpath

======================================================================================================

Docker Compose

-   version:

    services:
        servicename:
            image:
            command:
            enviroment:
            volumes:
        Servicename2:
    
    volumes:

    network:

Docker-compose cli

- docker-compose up
- docker-compose down
- docker-compose down -v

- we have to specify named valumes at the bottom of docker compose file if the volumes are empty

-We can also build image directly in docker compose
-   version: '2'

    # based off compose-sample-2, only we build nginx.conf into image
    # uses sample HTML static site from https://startbootstrap.com/themes/agency/

    services:
    proxy:
        build:
        context: .
        dockerfile: nginx.Dockerfile
        ports:
        - '80:80'
    web:
        image: httpd
        volumes:
        - ./html:/usr/local/apache2/htdocs/

==========================================================================================================

DOCKER SWARM

- it is a server clustering solution that brings together different OS or host or nodes into a single managable unit that we can then orchestrate the lifecycyle of containers
- Manager-worker concept
- Manager Node are the one that controls the structure and working of working nodes
- Each manager nodes has seperate component attched to itself like API, Orchestrator, Allocator, Scheduler, Dispatcher
- Workers connects to dispatcher to check on assigned tasks and executed the tasks assigned to it

- docker swarm init -to start the swarm
    - Root Signing Certificae created for our swarm
    - create special certificate for the first manager
    - Join token are created

    - RAFT database created to store root CA, confg and secrets

- docker service create alpine ping 8.8.8.8 - to create a service
    - docker service ls
    - docker service ps service_name
- docker service update service_name --replicas 3 - to scale the service

- docker swarm --join-token manager/worker

Routing mesh
- Routes ingress(incoming) packets for a service to proper tasks
    - conainer to container in a overlay network
    - external traffice incoming to published ports

Stacks of services in docker swarm: production grade compose

- stack accept compose files for production swarms
- docker stack deploy
- docker stack deploy -c compose_file.yaml appname

Secret Storage - easiest "secure" solution for storing secrets in swarm
    - Username and password
    - TLS certificate and keys
    - SSH keys
- Swarm RAFT database is encrypted on disk
- only stored on disk on manager nodes
- default is manager and workers "controls plane" is TLS + Mutual Auth

- docker secret create secret_name secret_file or we can take the value from std_input
- we can pass the secret as --secret secret_name and use the variable

- we can pass the secret in stack file
    -   secrets:
            plsql_user:
                file: ./filepath
    -   secrets:
            plsql_user:
                external: true

Service Updates
- docker service scale web=5
- docker service update --image nginx:1.13.6 web
- docker service update --publish-rm 8088 --publish-add 9090:80
- docker service update --force web

Docker Healthchecks
- Docker engine will exec's the command in the container
- it expects exit 0 or exit 1
- three container state: starting, healthy, unhealthy

-in dockerfile
-   HEALTHCHECK --interval=5s --timeout=3s \
    CMD pg_isready -U postgres || exit 1

-in Compose/stackFile
- services:
    web:
        image: nginx
        healthcheck:
            test:["CMD","curl","-f","http://localhost"]
            interval: 1m30s
            timeout: 10s
            retries: 3
            start_period: 1m

Container image registries

