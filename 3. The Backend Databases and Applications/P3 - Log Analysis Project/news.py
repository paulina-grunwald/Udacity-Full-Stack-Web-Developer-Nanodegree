#!/usr/bin/env python3

# This Log Analysis project is a part of Udacity Full Stack Nanodegree 

# Import modules
import psycopg2


def connect(database_name="news"):
    # Connect to the news database
    try:
        # connect to the database
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    # If not possible to connect to the database 
    except:
        print ("It is not possible to connect to the database!")


def get_query_results(query):
    # # connect to the database
    db, cursor = connect()
    cursor.execute(query)
    # Return result of the query
    return cursor.fetchall()
    # Close database
    db.close()