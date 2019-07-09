Docker 1, 2, 3 
Basic Concept
Application
What, Why, How
container, node. image

## Docker

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