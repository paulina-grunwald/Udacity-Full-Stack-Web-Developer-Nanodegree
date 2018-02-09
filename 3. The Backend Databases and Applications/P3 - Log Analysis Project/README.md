# Log Analysis Project
> by Paulina Grunwald

This project is a part of [Udacity's Full Stack Nanodegree Program](https://www.udacity.com/nanodegree). In this project, I had to use my SQL database knowledge in order to extract various data from the database. I practiced interacting with a live database both from the command line and from your code. I have explored a large database with over a million rows. I have also  built and refined complex queries and use them to draw business conclusions from data.

In this project, I have used  PostgreSQL database. My task was to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


# Table of contents

- [How to run my project](#how-to-run-my-project)
- [Data used in the project](#data-used-in-the-project)
- [Data exploration](#data-exploration)
- [Questions for this assignment](#questions-for-this-assignment)
- [Troubleshooting](#troubleshooting)
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
- To load the data go to the folder where the database is stored, use the command ```psql -d news -f newsdata.sql``` to connect a database and run the necessary SQL statements.

To execute the program, run ```python3 newsdata.py``` from the command line.

The database includes three tables:

- The __authors table__ includes information about the authors of articles.
- The __articles table__ includes the articles themselves.
- The __log table__ includes one entry for each time a user has accessed the site


# Data used in the project
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

My task was to write a program that will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


# Data exploration

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
As we can see slug is actually text which is pretty much shorter version of the title.

Article id is simply number assigned to certain article. The numbers in the table from 23 to 30

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
SELECT count(*) FROM log;
/*Output: 1677735*/
```

Let's have a look first at path column.

```SQL
SELECT COUNT (DISTINCT log.path) FROM log;

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
SELECT DISTINCT log.path FROM log LIMIT 10;
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
SELECT COUNT (DISTINCT log.ip) FROM log;
```
```
count
-------
  762
(1 row)

```

We have 762 unique users that used the database.

```SQl
SELECT ip, count(*) AS num
FROM Log
GROUP BY ip
LIMIT 3;  
```

```
ip       | num
----------------+------
192.0.2.233    | 2307
192.0.2.254    | 2275
198.51.100.217 | 2154
```


Method column has only one value: GET
```SQL
SELECT DISTINCT log.method from log;
```

Status column indicates the action requested by the client was received, understood and accepted. We will be only filtering status __200 OK__ which is standard response for successful HTTP requests.

```SQL
SELECT DISTINCT log.status FROM log;
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
SELECT log.time FROM log LIMIT 3;
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
SELECT COUNT (log.time) FROM log;
```
```
count
---------
1677735
(1 row)
```

```SQL
SELECT date(time) AS date
FROM log
GROUP BY date
LIMIT 3;
```

```
date
------------
2016-07-01
2016-07-02
2016-07-03
(3 rows)
```


```SQL
SELECT DATE(time)
SUM(CASE WHEN status LIKE '404%' THEN 1 ELSE 0 END)ErrCount,
COUNT(id) AS TotCount
FROM log
GROUP BY DATE(time)
ORDER BY DATE(time)
```


### Queries performed using multiple tables

As we remember from previous investigations we have 8 articles and 4 authors. Let's see which author has the biggest number of articles in the  news database.

```SQL
SELECT title, name
FROM articles JOIN authors ON articles.author = authors.id;
```

```
title                |          name
------------------------------------+------------------------
Bad things gone, say good people   | Anonymous Contributor
Balloon goons doomed               | Markoff Chaney
Bears love berries, alleges bear   | Ursula La Multa
Candidate is jerk, alleges rival   | Rudolf von Treppenwitz
Goats eat Google's lawn            | Ursula La Multa
Media obsessed with bears          | Ursula La Multa
Trouble for troubled troublemakers | Rudolf von Treppenwitz
There are a lot of bears           | Ursula La Multa
(8 rows)

```


# Questions for this assignment

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

```SQL
SELECT title, author, count(title) AS views
FROM articles, log
WHERE log.path=CONCAT('/article/',articles.slug) AND log.status LIKE '%200%'
GROUP BY articles.title, articles.author
ORDER BY views DESC
LIMIT 3;
```

Output:
```
title                            | author | views
----------------------------------+--------+--------
Candidate is jerk, alleges rival |      2 | 338647
Bears love berries, alleges bear |      1 | 253801
Bad things gone, say good people |      3 | 170098

```


2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

```SQl
SELECT authors.name, count(*) as views FROM articles inner
JOIN authors on articles.author = authors.id inner
JOIN log on log.path LIKE concat('%', articles.slug, '%')
WHERE log.status LIKE '%200%'
GROUP BY authors.name
ORDER BY views DESC
```

Output:
```
name                   | views
------------------------+--------
Ursula La Multa        | 507594
Rudolf von Treppenwitz | 423457
Anonymous Contributor  | 170098
Markoff Chaney         |  84557
```


3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

```SQL
SELECT * FROM (SELECT date(time),round(100.0*sum(CASE log.status
WHEN '200 OK'  THEN 0 ELSE 1 END)/count(log.status),3)
AS error FROM log
GROUP BY date(time)
ORDER BY error DESC) AS subquery
WHERE error > 1;
```

Output:
```
date       | error
------------+-------
2016-07-17 | 2.263

```

# Troubleshooting

While I was working on this project I have encountered following error: ``ERROR relation "..." already exists ALTER TABLE.`` The error was caused by the fact that I have tried to import newsdata.sql mutiple times.


![troubleshooting](https://discourse-cdn-sjc3.com/udacity/uploads/default/original/4X/9/7/d/97d9b7644c997f558e22fbb001fe96997d6bb039.png)

I took following steps to solve this issue:
- display the users connected to the database: ```select * from pg_stat_activity```
- Restart ```psql: sudo /etc/init.d/postgresql restart```
- Drop database: ```DROP DATABASE IF EXISTS news;```
- Create empty database: ```createdb news```
- Populate with the data from the SQL file: ```psql -d news -f newsdata.sql```
- Connect to the database with ```psql -d news```.



# 6. REFERENCES

- https://pypi.python.org/pypi/psycopg2
- https://app.pluralsight.com/library/courses/introduction-to-sql/table-of-contents
- https://www.w3schools.com/sql/sql_view.asp
- https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
- https://stackoverflow.com/questions/4005251/select-from-tbl-where-clm-like-concat-other-sql-query-limit-1-how
- https://stackoverflow.com/questions/5243596/python-sql-query-string-formatting
- http://www.sqlines.com/oracle-to-sql-server/to_char_datetime
- https://stackoverflow.com/questions/35374148/how-to-query-the-percentage-of-aggregate-in-vertica
- https://discussions.udacity.com/t/issues-with-newsdata-sql/524112
