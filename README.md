# Logs Analysis
Udacity logs analysis project

## Project Overview
In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.

## Supporting Materials
  - [Python3](https://www.python.org/)
  - [Vagrant](https://www.vagrantup.com/)
  - [VirtualBox](https://www.virtualbox.org/)
  - [News Database Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Installation
  1. Install Vagrant and VirtualBox
  2. Download or clone this repository

## Run the code
Startup Vagrant VM by typing `vagrant up` through a command line, to login type `vagrant ssh`

To load the data, cd into the vagrant directory after logging in and use the command `psql -d news -f newsdata.sql`.

The News database includes three tables:
- Authors table - includes information about authors of articles
- Articles table - includes articles
- Log table - includes one log entry for each time a user accessed the site

Use `psql -d news` to connect to database.

To run the log analysis program, run `python3 logs.py` from the command line.

A report will be created `report.txt` within the same directory.
