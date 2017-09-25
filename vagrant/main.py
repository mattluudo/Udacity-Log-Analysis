#!/usr/bin/env python2.7

import psycopg2

DBNAME = "news"
SQL_STATEMENT1 = "SELECT title, count(title) " \
                 "FROM log, articles " \
                 "WHERE regexp_replace(log.path,'^.*/','') = slug " \
                 "GROUP BY  title " \
                 "ORDER BY COUNT(title) DESC;"

SQL_STATEMENT2 = "SELECT authors.name, COUNT(authors.name) " \
                 "FROM authors, log, articles " \
                 "WHERE regexp_replace(log.path,'^.*/','') = slug AND " \
                 "authors.id = articles.author " \
                 "GROUP BY authors.name " \
                 "ORDER BY COUNT(authors.name) DESC;"

SQL_STATEMENT3 = "WITH error AS (SELECT DATE(time) as err_date, " \
                 "COUNT(DATE(time)) AS err_count " \
                 "FROM log WHERE status LIKE '404%' GROUP BY err_date), " \
                 "visit AS (SELECT DATE(time) as visit_date, " \
                 "COUNT(DATE(time)) AS visit_count " \
                 "FROM log GROUP BY visit_date) SELECT visit_date, " \
                 "(err_count::FLOAT/visit_count::FLOAT) as err_pct " \
                 "FROM error, visit WHERE visit_date = err_date AND " \
                 "(err_count::FLOAT/visit_count::FLOAT) > .01;"

# Connect to news database
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# Query #1: Query most popular three articles of all time
c.execute(SQL_STATEMENT1)
results = c.fetchall()

# Output results of Query #1
print("Most popular three articles of all time:")
for row in results[0:3]:
    print("\"" + row[0] + "\" -- " + str(row[1]) + " views")
print("\n")

# Query #2: Query most popular three authors of all time
c.execute(SQL_STATEMENT2)
results = c.fetchall()

# Output results of Query #2
print("Most popular three authors of all time:")
for row in results[0:3]:
    print("\"" + row[0] + "\" -- " + str(row[1]) + " views")
print("\n")

# Query #3: Query days with more than 1% requests leading to error
c.execute(SQL_STATEMENT3)
results = c.fetchall()

# Output results of Query #3
print("Days with more than 1% request error:")
for row in results:
    pct = row[1] * 100
    print(str(row[0]) + ' -- %.2f%% errors' % pct)
print("\n")

db.close()
