#! /usr/bin/env/python2.7
import psycopg2
import datetime
# Define the problem.
# Problem 1: Which three articles are the most popular of all time?
# Present the information as a sorted list with the most popular article
# at the top.
# Write a function that accomplishes this goal.


def display_top_three_articles():
    """ Display the top three articles from the database.
    """
    # Connect to the database
    try:
        conn = psycopg2.connect("dbname=news")
    except BaseException:
        print "I am unable to connect to the database."
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    # Execute the query.
    cur.execute("""SELECT articles.title, count(*) as views
     FROM log JOIN articles on log.path =
     concat('/article/', articles.slug)
     GROUP BY articles.title
     ORDER BY views DESC
     LIMIT 3;""")
    rows = cur.fetchall()
    # Write the results of the query to file.
    output = open("output.txt", "a")
    output.write("Show me the top three articles:\r\n\r\n")
    for row in rows:
        output.write(row[0] + " " + str(row[1]) + " --views" + '\r\n')
    output.write('\r\n')
    # Close the file.
    output.close()
    # Close communication with the database.
    cur.close()
    conn.close()

# Define the problem.
# Problem 2: Who are the most popular article authors of all time?
# Present the information as a sorted list with the most popular author
# at the top.
# Write a function that accomplishes this goal.


def display_top_three_authors():
    """ Display the top three authors from the database.
    """
    # Connect to the database
    try:
        conn = psycopg2.connect("dbname=news")
    except BaseException:
        print "I am unable to connect to the database."
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    # Execute the query.
    cur.execute(""" SELECT authors.name, count(*) as cnt
    FROM authors, articles, log
    WHERE articles.author = authors.id and log.path
    = concat('/article/', articles.slug)
    GROUP BY authors.name, articles.author
    ORDER BY cnt DESC LIMIT 3;
    """)
    rows = cur.fetchall()
    # Write the results of the query to file.
    output = open('output.txt', 'a')
    output.write("Show me the top three authors:\r\n\r\n")
    for row in rows:
        output.write(row[0] + " " + str(row[1]) + " --views" + '\r\n')
    output.write('\r\n')
    # Close the file.
    output.close()
    # Close communication with the database.
    cur.close()
    conn.close()

# Define the problem.
# Problem 3: On which days did more than 1% of requests lead to errors?
# The log table includes a column status that indicated the HTTP status code
# that the news site sent to the user's browser.


def display_high_error_count():
    """ Queries the database to check for days when errors were > 1%.

    """
    # Connect to the database
    try:
        conn = psycopg2.connect("dbname=news")
    except BaseException:
        print "I am unable to connect to the database."
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    # Execute the query.
    # This query is a little more complicated because it uses a subquery.
    # We want to select all results from the inner select.
    # We convert the time stamp to a date. The we round the sum
    # of times where a day had a status that was not '200 OK'
    cur.execute("""SELECT * FROM (SELECT date(log.time), round( 100.0 *
    SUM(CASE WHEN log.status != '200 OK' THEN 1 ELSE 0 end) /
    COUNT(log.status), 3) as num FROM log
    GROUP BY date(log.time)
    ORDER BY num DESC) as
    error_rate where num > 1;""")
    rows = cur.fetchall()
    # Write the results of the query to file.
    output = open("output.txt", "a")
    output.write("Show me the days with high error rate:\r\n\r\n")
    for row in rows:
        """ How to convert a datetime string to a different string taken from:
        https://stackoverflow.com/questions/14524322/how-to-convert-a-date-
        string-to-different-format
        """
        dt = datetime.datetime.strptime(
            str(row[0]), '%Y-%m-%d').strftime('%-m/%d/%y')
        output.write(dt + " " + str(row[1]) + r"% errors")
    # Close the file.
    output.close()
    # Close communication with the database.
    cur.close()
    conn.close()

display_top_three_articles()
display_top_three_authors()
display_high_error_count()
