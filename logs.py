#! /usr/bin/env python3

import datetime
import psycopg2

DBNAME = "news"

# 1. What are the most popular three articles of all time?
question1 = "1. What are the most popular three articles of all time?"
query1 = ("select articles.title, count(*) as views "
          "from articles inner join log on log.path "
          "like concat('%', articles.slug, '%') "
          "where log.status like '%200%' "
          "group by articles.title, log.path order by views desc limit 3")

# 2. Who are the most popular article authors of all time?
question2 = "2. Who are the most popular article authors of all time?"
query2 = ("select authors.name, count(*) as views "
          "from articles inner join authors on articles.author = authors.id "
          "inner join log on log.path "
          "like concat('%', articles.slug, '%') "
          "where log.status like '%200%' "
          "group by authors.name order by views desc")

# 3. On which days did more than 1% of requests lead to errors?
question3 = "3. On which days did more than 1% of requests lead to errors?"
query3 = ("select day, percent "
          "from (select day, round((sum(requests)/(select count(*) from log "
          "where substring(cast(log.time as text), 0, 11) = day) * 100), 2) "
          "as percent from (select substring(cast(log.time as text), 0, 11) "
          "as day, count(*) as requests from log where status like '%404%' "
          "group by day) as log_percent group by day order by percent desc) "
          "as percent_result where percent >= 1")


def get_query_result(query):
    """Connect and return report query"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    report = c.fetchall()
    db.close()
    return report


f = open("report.txt", "w+")


def print_article_query(query_result):
    print(query_result[1])
    f.write(query_result[1] + "\n")
    for result in (query_result[0]):
        print('"' + result[0] + '"' + " - " + str(result[1]) + " views")
        f.write('"' + result[0] + '"' + " - " + str(result[1]) + " views\n")


def print_query_result(query_result):
    print(query_result[1])
    f.write(query_result[1] + "\n")
    for result in (query_result[0]):
        print(result[0] + " - " + str(result[1]) + " views")
        f.write(result[0] + " - " + str(result[1]) + " views\n")


def print_error_result(query_result):
    print(query_result[1])
    f.write(query_result[1] + "\n")
    for result in query_result[0]:
        result_date = datetime.datetime.strptime(result[0], "%Y-%m-%d")
        date = result_date.strftime("%B %d, %Y")
        print(date + " - " + str(result[1]) + "% errors")
        f.write(date + " - " + str(result[1]) + "% errors\n")


if __name__ == '__main__':
    # store query results
    query1_result = get_query_result(query1), question1
    query2_result = get_query_result(query2), question2
    query3_result = get_query_result(query3), question3

    # print query results
    print_article_query(query1_result)
    print_query_result(query2_result)
    print_error_result(query3_result)

f.close()
