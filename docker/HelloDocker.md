Docker 1, 2, 3 
Basic Concept
Application
What, Why, How
container, node. image, volumn
compose
Swarm
manager node, worker node

## Docker

[youtube playlist by RaghavPal](https://www.youtube.com/watch?v=wi-MGFhrad0&list=PLhW3qG5bs-L99pQsZ74f-LC-tOEsBp2rK)

- running some simple container
- use Dockerfile to build a custom app
- how to use bind mounts to modify a running container


1. run a single task
- shell script or a custom app

2. Interactively
- connects to the container (similar to SSH)

3. In the background
- for long-running services like websites and databases


## Simple Container

### Simple Task
> docker container run alpine hostname
- alpine : image
    - if not found locally, will pulls from DockerHub
- hostname: execute *hostname* command

Docker keep a container running
    - as long as the process it started inside the container is still running
    - example about "hostname" process is end
    - but the container still exists in the *Exited* state

> docker container ls -all

### Interactive Ubuntu container
>  docker container run --interactive --tty --rm ubuntu bash
* --interactive: ask for a interactive session
* --tty: allocates a pseudo-tty
* --rm: remove container when it's done executing
* ubuntu: image
* bash: command that tell the container to run

- interactive containers are useful when putting together your own image
- you can run a container and verify all steps to run the app
- then capture them in a Dockerfile

### Background Container
> docker container run \
 --detach \
 --name mydb \
 -e MYSQL_ROOT_PASSWORD=my-secret-pw \
 mysql:latest

* --detech: background mode
* --name: name for container
* -e: environment variable
* mysql:latest: image 

> docker container ls
- list running containers

- Docker has build-in commands to checking status of container
> docker container logs mydb
> docker container top mydb

- run a command inside container
- docker container exec
> docker exec -it mydb \
mysql --user=root --password=$MYSQL_ROOT_PASSWORD --version
- can also use to connect the container and start shell 
> docker exec -it mydb sh


## Package and run custome app using Docker

Dockefile
```docker
 FROM nginx:latest

 COPY index.html /usr/share/nginx/html
 COPY linux.png /usr/share/nginx/html

 EXPOSE 80 443     

 CMD ["nginx", "-g", "daemon off;"]
 ```
* FROM: base image
* COPY: copy files form DockerHost to Image
* EXPOSE: ports that the application uses
* CMD: command to run when a container started from the image

- store DockerId
> export DOCKERID=<your docker id>
> echo $DOCKERID

- create new image
>  docker image build --tag $DOCKERID/linux_tweet_app:1.0 .
* --tag CustomName: to give the image a custome name
* . : Dir that Docker use as the build context

- run the container using the image
> docker container run \
 --detach \
 --publish 80:80 \
 --name linux_tweet_app \
 $DOCKERID/linux_tweet_app:1.0

* --detach: backgroud
* --publish: external port[80] will be direct[:] to port[80] in conrainer
* --name
* image

- force remove
> docker container rm --force linux_tweet_app
* --force: remove without shutting it down
- in production maybe can just stop.
> docker container stop [name]


## Modifying a Running website
- bind mount
- mount the source code directory on the local machine into the running container
- any changes made to the files on the host
- immediately reflected in the container
- a file/dir on the host machine is mounted into a container running on the same host

>  docker container run \
 --detach \
 --publish 80:80 \
 --name linux_tweet_app \
 --mount type=bind,source="$(pwd)",target=/usr/share/nginx/html \
 $DOCKERID/linux_tweet_app:1.0

* --mount
    * type=bind
    * source=path in host
    * target=path in container

- change made in bind mount will not store in image
- need to update the image
> docker image build --tag $DOCKERID/linux_tweet_app:2.0 .
- build is fast because it only modified the portion of the image that changed
- not a rebuilding

## Push image to DockerHub
- list your image in dockerhost
> docker image ls -f reference="$DOCKERID/*"
- this image is only stored in DockerHost local repo

- login and publish to registry
> docker login
> docker image push $DOCKERID/linux_tweet_app:1.0
> docker image push $DOCKERID/linux_tweet_app:2.0





## Docker
- container platform 
- make sure all the stack work on any platform and hardware
- like container for shipping industry 
- docker allow software to ship in the form of container
- containers consist of all the libraries and dependencies required for software to run


Dockerfile 
- to create docker image
- docker container = runtime instance of docker image
- can store in DockerHub
- pull to any environment and run

Container vs virture machine
- VM need to run on an OS
- Container just run on top of some lib/bin

Docker Client vc Docker Server (deamon)
together form the Docker Engine

Benefit
- Build app only once
    - DockerFile
- easier for deploy
    - worry less about OS setup
- protability
    - pull and run
- version control
    - docker hub
- isolation
    - not interferes with other application
- Productivity

## Install in linux
- OS 64-bit
- docker manual > docker for linux
- install docker (yum)
> docker --version
> docker info
start docker
> sudo service docker start

> docker images
- list all images
> docker ps
- list all running process
> docker ps -a
- list all process
> docker run [image]
stop docker
> sudo service docker stop
uninstall
> sudo yum uninsatll docker


## Commands
### Basic
> docker version

> docker -v
> docker --version

> docker info

> docker --help
> docker images --help

> docker login

### Images
> dockers images
> dockers pull [image]
> docker rmi [image id]

### Container
> docker ps
> docker run [image]
> docker run -it ubuntu

> docker start [container id]
> docket stop [contianer id]

### System
> docker stats
- check memory usage and CPU ...

> docker sytem df
- check file size

> docket system prune
- remove all stopped container
- remove all dangling images
- remove all build cache

> docker inspect [image]


## Images
Docker images are templates used to create Docker containers

## Container
Containers is a running instance of image
> docker pause [ConatinerName/ID]
> docker unpause [ConatinerName/ID]

> docker top [ConatinerName/ID]
> docker stats [ConatinerName/ID]

> docker attach [ConatinerName/ID]
- go inside the container

> docker kill [ConatinerName/ID]
> docker rm [ConatinerName/ID]

> docker history [ImageName/ID] 


## Jenkins
scan throught


## Docker file
- file with instruction to create image
- automation of Docker image creation

### Step
- create a file named "Dockerfie" 
- add instuction in Dokcerfile
- build dockerfile to create image
- run image to create container

```docker

FROM [image]
FROM scratch

# optional
MAINTAINER name <email>

# cmd to be run
CMD ["echo", "Hello Wrold"]

```
- build the image (with tag) in dir that contain Dockerfile
> docker build . 
> docker build -t tagName .
> docker run [imageID]


## Docker Compose
STEP:
1. install dokcer compose
    - ald install with docker
    > docker-compose -v
    - check for installation
    - check doc for installation
    - or
    > pip install -U docker-compose
2. create docker-compose.yml
```
version: '3'

services:

    web[ServiceName]:
        image: nginx
        port: 8080:80

    database:
        image: redis
```
3. check the validity of file by command
> docker-compose config

4. run docker-compose file
> docker-compose up
- detech mode
> docker-compose up -d

5. stop application
> docker-compose down

### How to scale
> docker-compose up -d --scale database=4
- docker-compose up -d --scale [ServiceName]=NumOfService
 ### Docker Compose
- tool for defining & running multi-container docker application
- yml file (docker-composr.yml)
- start and stop all service in single command
    - docker compose up
    - docker compose down
- can scale up selected services when required


## Docker Volumes
- by default data doesn't persist when the container is killed
- we can do a **bind mount** a local dir
- or mount a **volume** to the container

> docket volume create [name]
> docker volume inspect [name]
> docker volumn prune 

- attach image to a volumes
> docker run --name MyJenkins1
    -v myvol1:/var/jenkins_home
    -p 8080:8080
    -p 50000:50000
    jenkins
- look at the -v, we mount a vol to the container


## Docker Swarm
- is a group of machines that are running Docker 
- and joined into a cluster

- one node as manager
- other as worker
- Orchestarion
    - managing and controling multiple docker container as a singel service
- alternative
    - kubernates
    - apache mesos 


Step
0. Install docker-machine
1. Create docker machines 
    - act as nodes for Docker Swarm
    - one machines as Manager
    - others as Workers
> docker-machine create --driver virtualbox manager1
> docker-machine create --driver hyprev manager1
- repeat the same for workers

2. Check status
- list all machine
> docker-machine ls
- get machine ip
> docker-machine ip [name]

3. SSH Connection to machine
> docker-machine ssh[name]

4. Initialize Docker Swarm
[on Manager Machine]
- with mamanger ip
> docker swarm init --adverise-addr 192.168.99.100

- list all the node (manager and worker)
> docker node ls

5. Join worker to swap
- copy paste from the manager init
or get the command by
> docker swarm join-token worker

- to join as manager
> docker swarm join-token manager

[Manager Node]
> docker node ls
- to verify registration of worker

6. Standard Docker Commands
> docker info
- check for Swarm session
- no of manager, no of nodes

> docker swarm
- check Command available for swarm

7. Run Container on Docker Swarm
[Manager Node]
> docker service create 
    --replicas 3
    -p 80:80
    --name [serviceName]
    nginx
> docker service ls
- can check the running replicas
> docker server ps [serviceName]

8. Scale up or down
[Manager Node]
> docker service scale [serviceName]=[number]

### Inspecting Node
- only able to run on manager node
> docker node inspect [nodename]
> docker node inspect self
> docker node inspect worker1

9. update service 
> docker service update --image nginx:1.14.0 web1[serviceName]

10. shutdown node
> docker node update --availability drain worker1[NodeName]

11. Remove service
> docker service rm [serviceName]

### Swarm
[worker node]
> docker swarm leave

### Machine 
> docker-machine stop worker1
> docker-machine rm worker1