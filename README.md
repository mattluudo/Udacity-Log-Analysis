Pre-requisite:
Vagrant
Virtualbox

Design:
Write 3 queries using psycopg2 connected to news database
1. Top 3 articles
2. Top 3 authors
3. Days with request error greater than 1%


SQL #1:
Join log and article on log's path and articles' slug
Order by descending count 
Output only first 3 rows

SQL #2:
Join log and article on log's path and articles' slug
Join authors and articles on authors' id and articles' author
Order by descending count 
Output only first 3 rows

SQL #3:
Create table with total count of views per day
Create table with total view error per day
Join the two tables to get view error percentage
Output all rows with view error percentage greater than 1



Execute:
Download vagrant configuration file from https://github.com/udacity/fullstack-nanodegree-vm
Download data file newsdata.sql from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
Include the data file "newsdata.sql" in the project folder path (fullstack-nanodegree-vm/vagrant)
In a bash terminal, change directory to the fullstack-nanodegree-vm/vagrant 
Run "vagrant up", then "vagrant ssh"
Change directory to /vagrant
Load the data by using the command "psql -d news -f newsdata.sql"
Run python main.py on the virtual machine