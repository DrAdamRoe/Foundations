## simple function for reading from a sqlite database and returning a list
# takes a single argument of the neighborhood name, and returns a list of 
# resturants in the neighborhood.

# import the python library for SQLite 
import sqlite3

# function to open the database connection, run a query, close the database connection, and return the value of the query. 
def query_db(query):
    # connect to the database file, and create a connection object
    db_connection = sqlite3.connect('restaurants.db')

    # create a database cursor object, which allows us to perform SQL on the database. 
    db_cursor = db_connection.cursor()

    db_cursor.execute(query)

    # this will be a list of tuples, where each tuple represents a row in the table
    query_response = db_cursor.fetchall()

    db_connection.close()

    return query_response

def get_restaurants_names():
    # define a query, taking the string input for the neighborhood name 

    query = """SELECT restaurants.NAME from restaurants"""
    # store the result in a local variable. 
    list_restaurants = query_db(query)

    return(list_restaurants)
