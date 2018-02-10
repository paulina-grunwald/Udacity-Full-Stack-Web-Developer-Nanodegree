#!/usr/bin/env python3

# This Log Analysis project is a part of Udacity Full Stack Nanodegree
# Import modules

import psycopg2


def get_query_results(query):
    # Connect to the news database
    try:
        # connect to the database
        db = psycopg2.connect(database='news')
        cursor = db.cursor()
        # connect to the database
        cursor.execute(query)
        # Return result of the query
        result = cursor.fetchall()
        # Close database
        db.close()
        return result
    # If not possible to connect to the database
    except psycopg2.Error as e:
        print(e)
        exit(1)


def print_query_1(query_result):
    # Print query result
    print(query_result[1])
    # Iterate over results
    for index, results in enumerate(query_result[0]):
        print("\t", str(index + 1) + ".", results[0],
              "\t - ", str(results[1]), "views")


def print_query_2(query_result):
    # Print query result
    print(query_result[1])
    # Iterate over results
    for index, results in enumerate(query_result[0]):
        print("\t", str(index+1) + ".", results[0],
              "\t - ", str(results[1]), "views")


def print_query_3(query_result):
    # Print query result
    print(query_result[1])
    # Iterate over results
    for index, results in enumerate(query_result[0]):
        print("\t", str(index+1) + ".", results[0],
              "\t - ", str(results[1]), "%")
question1 = ("What are the most popular three articles of all time?")

query1 = """SELECT title, count(title) AS views
            FROM articles, log
            WHERE log.path=CONCAT('/article/',articles.slug)
            AND log.status LIKE '%200%'
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3;"""

question2 = ("Who are the most popular article authors of all time?")

query2 = """SELECT authors.name, count(*) as views FROM articles inner
            JOIN authors on articles.author = authors.id inner
            JOIN log on log.path LIKE concat('%', articles.slug, '%')
            WHERE log.status LIKE '%200%'
            GROUP BY authors.name
            ORDER BY views DESC;"""

question3 = ("On which days did more than 1% of requests lead to errors?")

query3 = """SELECT * FROM (SELECT date(time),round(100.0*sum(CASE log.status
            WHEN '200 OK'  THEN 0 ELSE 1 END)/count(log.status),3)
            AS error FROM log
            GROUP BY date(time)
            ORDER BY error DESC) AS subquery
            WHERE error > 1;"""

# Execute when running script
if __name__ == '__main__':
    # Store query results
    query1_result = get_query_results(query1), question1
    query2_result = get_query_results(query2), question2
    query3_result = get_query_results(query3), question3

    # Print query results
    print_query_1(query1_result)
    print_query_2(query2_result)
    print_query_3(query3_result)
