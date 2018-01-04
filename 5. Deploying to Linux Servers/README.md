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

Finger is retrives data from the file that stores info about all users: __cat /etc/passwd__

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
