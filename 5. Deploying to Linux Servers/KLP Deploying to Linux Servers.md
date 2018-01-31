# Delpoy Linux Servers

This course is a part of [Udacity's Full Stack Nanodegree program](https://www.udacity.com/nanodegree).

## Intro to Linux



## Linux Security

__rule of least privilege__ - user or an app have only enought premision to do its job - nothing else

sudo ls -al /home/ubuntu/.ssh - lists all files within ubuntu ssh directory

- All available package source are listed in: sudo cat /etc/apt/sources.list
- Update package source list: __sudo apt-get update__
- Update installed packages: __sudo apt-get upgrade__
- __man apt-get__ - info on packages
- __sudo apt-get autoremove__ - remove unnecessary packages
- __finger__ - check logged in users
- __finger vagrant__ - more info on logged in users

Finger is retrives  data from the file that stores info about all users: __cat /etc/passwd__

__/etc/passwd__ - This is a very important file on your system! It's used to keep track of all users on the system. Run cat /etc/passwd and look at the output; each line is organized in this format:

__<em>username:password:UID:GID:UID info:home directory:command/shell</em>__

Let’s run through what each of those mean:

1. __username__: the user’s login name
2. __password__: the password, will simply be an x if it’s encrypted
3. __user ID (UID)__: the user’s ID number in the system. 0 is root, 1-99 are for predefined users, and 100-999 are for other system accounts
4. __group ID (GID)__: Primary group ID, stored in /etc/group.
5. __user ID info__: Metadata about the user; phone, email, name, etc.
6. __home directory__: Where the user is sent upon login. Generally /home/
7. __command/shell__: The absolute path of a command or shell (usually /bin/bash). Does not have to be a shell though!

__sudo adduser user_name__ - add new user
__finger__ - you can see all users

To connect to the server as new created user we need to use command __ssh new_user_name@127.0.0.1 -p 2222__
Ssh is an application that we use to remotely connect to the sever. 127.0.0.1 is <em>IP</em> address to which we want to connect. -p 2222 mentions to which port we should connect.

__sudo cat /etc/passwd__ - asks for sudo password

__sudo cat /etc/sudoers__ - list sudo users

__sudo ls /etc/sudoers.d__ - list of uses who can perform administrative tasks

__includedir /etc/sudoers.d__ - looks through all the files in the /etc/sudoers.d

__sudo cp <source path> <destination path>__ - copy file from source to destination path and rename it
(in out case it would be sudo cp /etc/sudoers.d/vagrant /etc/sudoers.d/student)

__sudo nano <file path>__ - make small edit to the file
We need to change the content of the file (change vagrant to student)
```
CLOUD_IMG: This file was created/modified by the Cloud Image build process vagrant ALL=(ALL) NOPASSWD:ALL
```

- Press <em>Ctrl+X</em> or F2 to Exit. You will then be asked if you want to save.
- Press <em>Ctrl+O</em> or F3 and Ctrl+X or F2 for Save and Exit

If you want to expire users password immediately (so when they log in they can set new one) you have to use command __sudo passwd -e user_name__

Public key
Privet key

__ssh-keygen__ - generate private key locally
/home/vagrant/.ssh/linuxCourse
This command creates two files:
- linuxCourse.pub
- linuxCourse

SSH version 2 supports DSA, ECDSA, ED25519 and RSA key types. You can find this information by running man ssh-keygen and reading the documentation for the -t flag.


#### Installing a public key on the server:
1. Login as a student
  - mkdir .ssh
  - touch .ssh/authorized_keys
2. Go to local machine to /home/vagrant/.ssh/linuxCourse.pub and copy the key
3. Go back to server and use command nano .ssh/authorized_keys and patse previously coppied key.
4. chmod 700 .ssh
5. chmod 644 .ssh/authorized_keys

6. log in on server using ssh student@127.0.0.1 -p 2222 -i ~/.ssh/linuxCourse
7. Disable password based login for users. They will have to use keypair. We will use following command: sudo nano /etc/ssh/sshd_config
8. restart the service so the new configuration option is used: sudo service ssh restart


#### Introduction to File Permissions
chmod
ls -al

Permissions are described as r,w, x.
It's also possible to use values for changing of the permission (__octal form__):
r = 4
w = 2
x = 1
no permissions = 0



rw- (read and write) : owner
r-- (read): group
r-- (read): everyone
x - execute

sudo ls -al /var/log


#### chgrp (change group) and chown (change owner)
sudo chown root .bash_history
cat .bash_history =>


#### Intro to Ports
Each of your applications are configured to respond to request destined to specific port.

__sudo ufw status__ - check status of the preinstalled firewall

Add rules to firewall:
- __sudo ufw default deny incoming__ - deny incoming
- __sudo ufw default allow outgoing__ - allow outgoing
Configure ports in UFW:
- __sudo ufw allow 2222/tcp__ - configure port for ssh
- __sudo ufw allow www__ - configure http

- __sudo ufw enable__ - enable firewall


```
sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
2222/tcp                   ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
2222/tcp (v6)              ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
```


## Web Applications Server
Now that you have a shiny new server that is safe and secure, it’s time to turn it into a web application server! By the end of this lesson you will accomplish the following:

1. <em>Install Apache</em>

  Install Apache using your package manager with the following command: __sudo apt-get install apache2__ Confirm Apache is working by visiting http://localhost:8080 in your browser.Apache, by default, serves its files from the /var/www/html directory. If you explore this directory you will find a file called index.html and if you review that file you will see it contains the HTML of the page you see when you visit http://localhost:8080.

2. Use the Apache HTTP Server to respond to HTTP requests and serve a static webpage
3. Configure Apache to hand-off specific requests to Python providing the ability to develop dynamic websites
4. Setup PostgreSQL and write a simple Python application that generates a data-driven website

# References
- https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/
- https://wiki.archlinux.org/index.php/users_and_groups
- https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-14-04
- https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-ubuntu-14-04
- https://www.digitalocean.com/community/tutorials/how-to-run-your-own-mail-server-and-file-storage-with-peps-on-ubuntu-14-04
- https://www.digitalocean.com/community/tutorials/how-to-run-your-own-mail-server-with-mail-in-a-box-on-ubuntu-14-04
- https://www.digitalocean.com/community/tutorials/how-to-install-the-lita-chat-bot-for-irc-on-ubuntu-14-04
