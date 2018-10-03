#!/usr/bin/env python3
import psycopg2

class MyClass(object):
    def __init__(self):
        self.top_articles()
        self.top_authors()
        self.errors_over_one_percent()

    def top_articles(self):
        conn = psycopg2.connect("dbname=news")
        cursor = conn.cursor()
        cursor.execute("""select title, cast(count as int) 
                       from (select path, count(path) from 
                       log where path LIKE '/article/%' and 
                       status='200 OK' group by path order by 
                       count DESC limit 3) l join articles a 
                       on '/article/'||a.slug = l.path order 
                       by count DESC""");
        results = cursor.fetchall()
        conn.close()
        print("Now printing top viewed articles...")
        for items in results:
            print(items)
        print("")
        return 1

    def top_authors(self):
        conn = psycopg2.connect("dbname=news")
        cursor = conn.cursor()
        cursor.execute("""select name, cast(views as int) from 
                       (select author, SUM(count) as views from 
                       (select path, count(path) from log where 
                       path LIKE '/article/%' and status='200 OK' 
                       group by path) l join articles a on 
                       '/article/'||a.slug = l.path group by author) 
                       as f join authors as w on f.author = w.id 
                       order by views DESC""")
        results = cursor.fetchall()
        conn.close()
        print("Now printing the most popular article authors...")
        for items in results:
            print(items)
        print("")
        return 1

    def errors_over_one_percent(self):
        conn = psycopg2.connect("dbname=news")
        cursor = conn.cursor()
        cursor.execute("""select time, cast(errors as float)/
                       cast(total as float) as error_percent 
                       from (select time::timestamp::date,count(*) 
                       total, sum(case when status !='200 OK' then 
                       1 else 0 end) errors from log group by 
                       time::timestamp::date) as z where 
                       cast(z.errors as float) / 
                       cast(z.total as float) > 0.01""")
        results = cursor.fetchall()
        conn.close()
        print("Now printing dates in which more than 1% of requests resulted in errors...")
        for items in results:
            print(items)
        print("")
        return 1

if __name__ == '__main__':
    instance = MyClass()
