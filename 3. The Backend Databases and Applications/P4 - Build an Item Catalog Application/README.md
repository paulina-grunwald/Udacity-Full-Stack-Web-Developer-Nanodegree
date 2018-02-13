# Build a Item Catalog Application Project
> by Paulina Grunwald

This project is a part of [Udacity's Full Stack Nanodegree Program](https://www.udacity.com/nanodegree). In this project I had to develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. The goal was also to allow registered users to post, edit and delete their own items. This project combines the knowledge of building dynamic websites with persistent data storage to create a web application that provides a compelling service to the users.


# Table of contents

- [How to run my project](#how-to-run-my-project)
- [Steps taken in developing Item Catalog App](#steps-taken-in-developing-Item-Catalog-App)
- [References](#references)


# How to run my project
In order to be able to run all the files included in this project you need to have installed on your machine following  applications:
- Python 3.6.x
- PostgreSQL 9.6.x
- Vagrant
- VirtualBox

Steps:
- Unizp newsdata.rar (you can find newsdata.sql database inside of the zipped file)
- Install Vagrant And VirtualBox
- Clone this repository
- Launch Vagrant VM by running ```vagrant up```, you can the log in with ```vagrant ssh```
- When having problems with starting up your vagrant you can try following command instead vagrant ssh: ```VAGRANT_PREFER_SYSTEM_BIN=1 vagrant ssh```
- To load the data go to the folder where the database is stored, use the command ```psql -d news -f catalog.sql``` to connect a database and run the necessary SQL statements.

The database includes three tables:

- The __authors table__ includes information about the authors of articles.
- The __articles table__ includes the articles themselves.
- The __log table__ includes one entry for each time a user has accessed the site


# Steps taken in developing Item Catalog App

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.




# 6. REFERENCES
