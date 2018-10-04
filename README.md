# Logs Project


This is a python based application that runs PostgreSQL queries against a database
with over 1.5 million rows for a fictional news website.

#### Requirements
Logs Project will compile with a basic linux stack using PostgreSQL and the dependencies listed below:
  - python3
  - psycopg2
```
To install python3 run the following command:
$ sudo apt-get install python3

And for psycopg2:
$ sudo pip install psycopg2
```
#### The database
The SQL database is named "news" and can be acquired [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
Unzip the newsdata.sql file somewhere on your linux machine and import with
```sh 
$ psql -f newsdata.sql
```
The **news** database contains 3 tables
* The **_articles_** table holds information regarding the article body and 
its slug (*identifying part of a web address*). The column *authors* is
used as a **foreign key** for the purpose of identifying which author wrote
each article.
* The **_authors_** table keeps the names and the biography of each author.
* The **_log_** table stores the *http://* request data, users IP address, 
status of the request (200, 301, 404), and the file path.

#### The questions
Following are the questions that this project answers
 1. What are the most popular three articles of all time?
 2. Who are the most popular article authors of all time?
 3. On which days did more than 1% of requests lead to errors?
#### Compile
Navigate to file location and run command
```sh
$ python main.py
```

