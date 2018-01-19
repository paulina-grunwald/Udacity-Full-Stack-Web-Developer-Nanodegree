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
- Launch Vagrant VM by running ```vagrant up```, you can the log in with ```vagrant ssh```
- When having problems with starting up your vagrant you can try following command instead vagrant ssh: ```VAGRANT_PREFER_SYSTEM_BIN=1 vagrant ssh```
- To load the data go to the folder where the database is stored, use the command ```psql -d news -f newsdata.sql``` to connect a database and run the necessary SQL statements.

To execute the program, run ```python3 newsdata.py``` from the command line.

The database includes three tables:

- The __authors table__ includes information about the authors of articles.
- The __articles table__ includes the articles themselves.
- The __log table__ includes one entry for each time a user has accessed the site


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
  - time (timestamp with time zone) e.g
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

### Investigation in Articles table

1. View all article titles from articles table:

```SQl
SELECT articles.title FROM articles;
```       

The query displayed ```8 articles```. They are following:

- Bad things gone, say good people
- Balloon goons doomed
- Bears love berries, alleges bear
- Candidate is jerk, alleges rival
- Goats eat Google's lawn
- Media obsessed with bears
- Trouble for troubled troublemakers
- There are a lot of bears


Author column has integer values form 1 to 4.
```SQL
SELECT articles.author SELECT articles.slug FROM articles;
 articles;
```

Let's have a look at slug column in articles table.
```SQL
SELECT articles.slug FROM articles;
```
Above query results in following output:
```
Output:
bad-things-gone
balloon-goons-doomed
bears-love-berries
candidate-is-jerk
goats-eat-googles
media-obsessed-with-bears
trouble-for-troubled
so-many-bears
```
As we can see slug is actually text which is pretty much shorter version of the title

Article id is simply number assigned to certain article. The numbers in the table fo from 23 to 30

```SQL
SELECT articles.id, articles.slug FROM articles ORDER BY articles.id ASC;
```
```
id |           slug
----+---------------------------
23 | bad-things-gone
24 | balloon-goons-doomed
25 | bears-love-berries
26 | candidate-is-jerk
27 | goats-eat-googles
28 | media-obsessed-with-bears
29 | so-many-bears
30 | trouble-for-troubled

```

In this project I will not use column lead (short description of the article), body (longer description of the article), time (same value for all articles ``` 2016-08-15 18:55:10.814316+00```).

### Investigation in Author table

Authors table has only 3 columns: name, bio and id. I will focus only on columns name and id as bio is just description of the author career which will not be useful for my investigation.

Let's find out what are the names and id numbers of authors:
```sql
SELECT authors.name, authors.id FROM authors;
```
```
name                   | id
------------------------+----
Ursula La Multa        |  1
Rudolf von Treppenwitz |  2
Anonymous Contributor  |  3
Markoff Chaney         |  4

```

As we can see there are 4 authors present in the database.

### Investigation in Log table
We have 6 columns in log table: path, ip, method, status, time, id.

There are 1677735 unique rows in log table.
```SQL
select count(*) from log;
/*Output: 1677735*/
```

Let's have a look first at path column.

```SQL
SELECT COUNT (DISTINCT log.path) from log;

```
```
count
-------
  212
(1 row)
```
There are 212 unique rows in path column.

Now we will view sample of 10 rows:

```SQL
SELECT DISTINCT log.path from log LIMIT 10;
```

```
path
-------------------------------------
/article/goats-eat-googlesh
/article/goats-eat-googlesy
/article/candidate-is-jerkb
/article/balloon-goons-doomedr
/article/bad-things-gonex
/article/bears-love-berriese
/article/candidate-is-jerkn
/article/media-obsessed-with-bearsl
/article/media-obsessed-with-bearsa
/article/candidate-is-jerky
(10 rows)
```

Ip signifies IP from which the article was accesses. We would use ip if we would like to find e.g how man unique people viewed certain article.  

```SQL
SELECT COUNT (DISTINCT log.ip) from log;
```
```
count
-------
  762
(1 row)

```
We have 762 unique users that used the database.

Method column has only one value: GET
```SQL
SELECT DISTINCT log.method from log;
```

Status column indicates the action requested by the client was received, understood and accepted. We will be only filtering status __200 OK__ which is standard response for successful HTTP requests.

```SQL
SELECT DISTINCT log.status from log;
```
```
status
---------------
404 NOT FOUND
200 OK
(2 rows)

```

In further investigation we will use only status ```200 OK```.


Column time shows exact date and time when the search was performed by the users.
```SQL
SELECT log.time from log limit 3;
```
```
time
------------------------
2016-07-14 15:19:47+00
2016-07-14 15:19:32+00
2016-07-14 15:19:53+00
(3 rows)
```

Each performed search (this every column in log database) has unique
```SQL
SELECT COUNT (log.time) from log;
```
```
count
---------
1677735
(1 row)
```



### Queries performed using multiple tables

```SQL
select title, name
from articles join authors
on articles.author = authors.id;
```



# Questions for this assignment
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

```SQl
SELECT title,
       author,
       count(title) AS views
FROM articles,
     log
WHERE log.path LIKE concat('%',articles.slug)
GROUP BY articles.title,
         articles.author
ORDER BY views DESC;
```



To answer this question we need to use following columns from following tables

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

```SQl
SELECT name,
       sum(article_view.views) AS total
FROM article_view,
     authors
WHERE authors.id=article_view.author
GROUP BY authors.name
ORDER BY total DESC;
```



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
