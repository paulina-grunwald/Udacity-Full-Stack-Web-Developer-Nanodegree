# LINUX SERVER CONFIGURATION PROJECT
> by Paulina Grunwald

This course is a part of [Udacity's Full Stack Nanodegree Program](https://www.udacity.com/nanodegree).

My task in this project was to baseline installation of a Linux server and prepare it to host your web applications. I had to secure my server from a number of attack vectors, install and configure a database server, and deploy one of your existing web applications onto it.

This project develops deep understanding of exactly what your web applications are doing, how they are hosted, and the interactions between multiple systems are what define you as a Full Stack Web Developer. In this project, I was  responsible for turning a brand-new, bare bones, Linux server into the secure and efficient web application host your applications need.

## Table of contents

- [SSH Client Info](#ssh-client-info)
- [Project Steps](#project-steps)
- [References](#references)


## SSH Client info

It's possible to connect to my instance using following address:
IP address: 52.58.147.11
Accessible SSH port: 2200

## Project steps

##### 1. Update all currently installed packages.
```
sudo apt-get update
sudo apt-get upgrade
```

##### 2. Install finger, a utility software to check users' status:
``sudo apt-get install finger``

##### 3. Add new users grader and give permission to sudo for this user
Create grader user:

``sudo add user grader``

Add sudo premission:

``sudo nano /etc/sudoers.d/grader `` type in ``grader ALL=(ALL:ALL) ALL`` save and quit.

Verify if permission was given correctly:

``sudo ls /etc/sudoers.d``



#### 4. Change the SSH port from 22 to 2200. Make sure to configure the Lightsail firewall to allow it.

6. Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123).



# References
- https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/
