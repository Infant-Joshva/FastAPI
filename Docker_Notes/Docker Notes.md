Docker Introduction:

---

* Problem we faced before the docker, 

  * works only on my computer
  * System setup
* How docker will solve this problem?. By using the  container method, what it will do?. 
* It will docker image-(this is like list to create a docker-container, like grocery list to make Biriyani) to store everything which was used to run our application to run on another computer, by this way docker solve this problem



\---------------------------------------------------------------



Docker Commands:

---

* Use this command to check the docker is installed or not: ***docker --version*** 
* To build or run the docker container we want a docker images, so use this command to check is there any images available on our system: ***docker images***
* docker file(refer docker file section to known about this file) is used to build the docker image, use this comment to build the image using docker file, "-t" is used to give a name to our images, "." means current dir, this is the place used to mention where the docker file is located : ***docker build -t imagename .***
* Using this image we can create a container, this is the command to create a container: ***docker run -p 8080 : 8080 imagename***
* That "8080" number is called as port first number is local machine(host) port and 2nd is container port, then "imagename" means mention the image you want to run. 
* How do i known if a container is created? use this command to check that. PS means process status: ***docker ps***
* Ok now we want to share this images to our co worker, now how it will be happen? by using the docker hub. docker hub is like a google drive, here we can create repository and save(push) our images 
* ok now how other user will access this image? first we want to login our docker: ***docker login***
* we want to mention the repo name to store our file, so by using this command we can store that: ***docker tag imagename reponame/imagename***

  * if you run that above command it will create a new tag with that image then we can push that tag into our docker hub using this cmd: ***docker push reponame/imagename***

    * this is the tag we got created: "***reponame/imagename"***
* we can give that **tag** to our co-worker and he can pull(download) that tag to get the image by using this cmd: ***docker pull reponame/imagename***



Note: if you run this cmd: "docker images", you can see the "latest" keyword on "Tag" column. it means version, by using this we save our diffrent versions of our project, if we do some logic changes we can mention the version name on our image to avoid the conflict issue, we can do that by this cmd on that version placholder you can mention like "1.0.0", if you not mention anyting it will automatically give the version name as "latest", best practice give a own version: ***docker tag imagename reponame/imagename : version*** 



* if you want to remove the images use this cmd: ***docker rmi imagename:version*** or ***docker rmi imageID***
* To start, stop or remove the container use this command: 

  * Start: ***docker start <containerid>***
  * Stop: ***docker stop <containerid>***
  * Remove: ***docker rm <containerid>***



\----------------------------------------------------------------------

#### Docker Run Command and Port-defenition:



* Docker run command: ***docker run -p host\_port\_number:container\_port\_number --name=container\_name tag***

  * "-p": port is like a address for each application and its like a train track, at a time we can run only one train, this port only decide where our input should goes to

    * 1st one local system port(host) and 2nd is docker container port
  * "--name": this the place we are going to set name for container
  * "tag": this is the tag name we already created with the docker image to store on docker hub





#### Docker Volume:



* If we run our container as usual but suddenly our container was crashed, so we created a new container but our user old history also deleted on that old container, new container dont  have access to that old history
* So, this where the docker volume will comes, this is storage for docker container, our user history wont lose even if our container crashed. 
* how it will done?: we will create a docker volume and link that volume to our container, so if our container will crashed will create a new container and link this link to new container
* Fun fact: this Docker volumes all are saved on your local system that's why this will delete even if you container crashed
* Docker volume create command: ***docker volume create volume\_name***
* To check our volume is created or not: ***docker volume ls***
* To view the location where our all files are saving: ***docker volume inspect volume\_name***
* To mount(link) our volume to our container: ***docker run -p 8080 : 8080 -v volume\_name:/container\_foler\_name imagename:version***

  * *can mount volume only while creating container, cannot mount volume on running container* 





###### Bind Mount vs Volume Mount:



* Volume Mount is only handled by Docker, so we cant access that but we can access that file if we Bind mount
* Bind Mount means mount our local folder directly to docker container, So we can easily access that file 

  * Additional advantes: If we want to store any files on our container, we store that on Bind Mounted folder, so that container can access that file
* Command to create Bind mount: ***docker run -p 8080 : 8080 -v local\_folder:/container\_foler\_name imagename:version***



#### Docker File:



* This is the file used to create a docker image, this is like a grocery list
* This file name always should be "Dockerfile" and it is a case sensitive 'D' must be capital
* In this docker first we want to mention the OS we are going to use for that project. Each OS has different file system that's why we want this OS and we we can build that with base image of each OS, each OS has their own base image
* How to create a image with this base image: Using the 'FROM' key word, use this keyword to mention from which base image you are going to create the image

  * Syntax: <Base image name \& Version>
* How to find this image?. Search on google like "ubuntu docker image" it will show the docker hub, on that hub you will see a lot of version 

  * Syntax: FROM ubuntu:22.04
* Next step mention the tools we used to build, For example the calculator project is build by "Node Js", 
* what ever things you want to install use this "RUN" command to install that tool, dependencies

  * if we want to install the nodeJs we want to give 4-5 lines of code instead of that we can the Nodejs base image to build our file and the fun fact is that image contains Ubuntu also so we can build our image with that base image, For example

    * Syntax: instead of "FROM ubuntu:22.04", we can use "FROM node:20.11.1"
* Next we want to create a folder for our Application/Project, So use "WORKDIR" key word to create a folder 

  * Syntax: WORKDIR /app
* Next step we want copy our files into the image, So we using "COPY" command to do that

  * Syntax: COPY . .

    * The first "." means current directory, the first "." is used to mention where we want to copy from and 2nd is used to when to copy on Image
* Next step install the require moduls, so agin use the RUN command to install require modul we mentioned in the requirement.txt file

  * Syntax: RUN requirements.txt
* Next step we want to mention the port number which is used to run our application to another developer, So use "EXPOSE" key word mention our port number, but this is not a mandatory but it used to give a extra information to another person to tell the our application running port number 
* Last and final step. Mention our application start command, by using "CMD" keyword to mention our application running command

  * Syntax: CMD \["python", "/app/my\_script.py"]
  * python → launches the Python interpreter
  * /app/my\_script.py → path of your Python file inside the container

\------------------------------------------------------------------------------------------------------------------

> Final work flow of docker file:

Step 1: Create a image from a base image

Step 2: Creating a working dir

Step 3: Copy our apllication files 

Step 4: Install the required modules 



All the steps will excute and create the docker image except the "CMD" step,

the cmd step will exucute only when start create the docker container



\----------------------------------------------------------------------------------------------------------------------



