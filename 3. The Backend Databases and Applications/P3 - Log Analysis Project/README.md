# Log Analysis Project
> by Paulina Grunwald

This project is a part of [Udacity's Full Stack Nanodegree Program](https://www.udacity.com/nanodegree). In this project, I had to use my SQL database knowledge in order to extract various data from the database. I practiced interacting with a live database both from the command line and from your code. I have explored a large database with over a million rows. I have also  built and refined complex queries and use them to draw business conclusions from data.

In this project, I have used  PostgreSQL database. My task was to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


# Table of contents

- [How to run my project](#how-to-run-my-project)
- [Data used in the project](#data-used in the project)
- [References](#references)


# How to run my project
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
- To load the data go to the folder where the database is stored, use the command __psql -d news -f newsdata.sql__ to connect a database and run the necessary SQL statements.


The database includes three tables:

- The __authors table__ includes information about the authors of articles.
- The __articles table__ includes the articles themselves.
- The __log table__ includes one entry for each time a user has accessed the site

To execute the program, run python3 newsdata.py from the command line.

# Data used in the project
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

My task was to write a program that will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


# Data Exploration

To get familiar with the database I run few quick commands:

__\dt+__ — the database has three tables: articles, authors and log. The biggest in size is log (129MB).

__Articles__ table has following columns:
  - author (integer),
  - title (text)
  - slug (text)
  - lead (text)
  - body (text)
  - time (timestamp with time zone)
  - id (integer)

__Author__ table has following columns:
  - name (text)
  - bio (text)
  - id (integer)

__Log__ table has following columns:
- path (text)
- ip (inet)
- method (text)
- status (text)
- timestamp (timestamp)
- id (integer)

All tables have one column in common - this is __id column__. I will use this column to extract various information from multiple tables in one query.

Let's find out what are the names of authors:

```sql
SELECT * from authors;
```
Let's now try to print authors name and associated id:
```sql
SELECT authors.name, authors.id FROM authors;
```

There are 4 authors present in the database:
- Ursula La Multa  - id 1
- Rudolf van Treppenwitz - id 2
- Anonymous Contributor - id 3
- Markoff Chaney - id 4


Let's now try to print authors name and associated id:

```sql
SELECT authors.name, authors.id FROM authors;
```

View all article titles from articles table:

```
SELECT articles.title FROM articles;
```       
The query displayed 8 articles. They are following:

- Bad things gone, say good people
- Balloon goons doomed
- Bears love berries, alleges bear
- Candidate is jerk, alleges rival
- Goats eat Google's lawn
- Media obsessed with bears
- Trouble for troubled troublemakers
- There are a lot of bears



```SQL
select title, name
from articles join authors
on articles.author = authors.id;
```

Let's try to pint nam

Let's have a look closer at the log table.
```SQl
SELECT * from log Limit 10;
```

As mentioned before log table contains following columns:  path, ip, method, status, timestamp and id.
- Path is a path to the article and includes article's namee.g /article/candidate-is-jerk.
- Ip signifies IP from which the article was accesses. We would use ip if we would like to find e.g how man unique people viewed certain article.  
- Status indicates the action requested by the client was received, understood and accepted. We will be only filtering status __200 OK__ which is standard response for successful HTTP requests.
- Time column shows at what in which day and at what time the article was viewed e.g 2016-07-01 07:00:00+00
- Id is linked to the specific author


```SQL
select count(*) from log;
/*1677735*/
```

# Questions for this assignment
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.



To answer this question we need to use following columsn from following tables

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.


path

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)


# Troubleshooting

While I was working on this project i have encountered following error: "ERROR relation "..." already exists ALTER TABLE.
I took following steps to solve this issue:
- Restart psql: sudo /etc/init.d/postgresql restart
- Drop database:
  ```y
  psql
  DROP DATABASE IF EXISTS news;
  ```

# REFERENCES

- https://pypi.python.org/pypi/psycopg2
- https://app.pluralsight.com/library/courses/introduction-to-sql/table-of-contents
- https://www.w3schools.com/sql/sql_view.asp
- https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
