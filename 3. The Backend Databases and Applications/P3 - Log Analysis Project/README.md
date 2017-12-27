# Log Analysis Project
> by Paulina Grunwald

This project is a part of Udacity's full-stack [nanodegree program](https://www.udacity.com/nanodegree). In this project, I had to use my SQL database skills. I practiced interacting with a live database both from the command line and from your code. I have explored a large database with over a million rows. I have also  built and refined complex queries and use them to draw business conclusions from data.

In this project, I have used  PostgreSQL database. My task was to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


## Table of contents

- [How to run my project](#how-to-run-my-project)
- [Data used in the project](#data-used in the project)
- [References](#references)


## How to run my project
In order to be able to run all the files included in this project you need to have installed on your machine following  applications:
- Python 3.6.x
- PostgreSQL 9.6.x
- Vagrant
- VirtualBox

Steps:
- Install Vagrant And VirtualBox
- Clone this repository
- Launch Vagrant VM by running __vagrant up__, you can the log in with __vagrant ssh__
- When having problems with starting up your vagrant you can try following command instead vagrant ssh: __VAGRANT_PREFER_SYSTEM_BIN=1 vagrant ssh__
- To load the data, use the command __psql -d news -f newsdata__ to connect a database and run the necessary SQL statements.

The database includes three tables:

- The authors table includes information about the authors of articles.
- The articles table includes the articles themselves.
- The log table includes one entry for each time a user has accessed the site

To execute the program, run python3 newsdata.py from the command line.

## Data used in the project
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

My task was to write a programme that will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


## Questions for this assigment

To get familiar with the database I run few quick commands:
- \dt+ — the datbase has three columns: articles, authors and log. The biggest in size is log (129MB).

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)
