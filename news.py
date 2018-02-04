#!/usr/bin/env python3
# Logs analysis project.

import datetime
import psycopg2

pg = psycopg2.connect("dbname=news")
c = pg.cursor()
# The most popular three articles of all time
c.execute("select title, count(ip) as views from authors inner join \
        articles on articles.author = authors.id inner join log on\
        concat('/article/', articles.slug) = path group by title\
        order by views desc limit 3;")
results = c.fetchall()

print('\n')
print('The most popular three articles of all time:')
for x in range(3):
    print(u'\u2022' + ' "' + results[x][0] + '" ' + u'\u2014' + ' ' +
          str(results[x][1]) + ' views')

# The most popular article authors of all time
c.execute("select name, count(ip) as views from authors inner join \
        articles on articles.author = authors.id inner join log on \
        concat('/article/', articles.slug) = path group by name \
        order by views desc;")
results = c.fetchall()

print('\n')
print('The most popular article authors of all time:')
y = len(results)
for x in range(y):
    print(u'\u2022' + ' ' + results[x][0] + ' ' + u'\u2014' + ' ' +
          str(results[x][1]) + ' views')

# Days on which more than 1% of requests lead to errors
c.execute("select table1.Date, concat(round(cast(table2.StatNum as numeric)/\
        table1.StatNum * 100, 2), '% errors') as Error from \
        (select to_char(log.time, 'Month DD, YYYY') as Date, count(status) \
        as StatNum from log group by Date) as table1 inner join \
        (select to_char(log.time, 'Month DD, YYYY') as Date, count(status) \
        as StatNum from log where (left(status, 1) = '4' or \
        left(status, 1) = '5') group by Date) as table2 on \
        table1.Date = table2.Date where round(cast(table2.StatNum as \
        numeric)/table1.StatNum * 100, 2) > 1 order by Error desc;")
results = c.fetchall()

print('\n')
print('Days on which more than 1% of requests lead to errors:')
y = len(results)
for x in range(y):
    print(u'\u2022' + ' ' + results[x][0] + ' ' + u'\u2014' + ' ' +
          str(results[x][1]) + ' views')
print('\n')

# Close the database connection
pg.close()
