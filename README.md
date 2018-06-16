# Udacity-Backend-Project

# Description

The Udacity-Backend-Project is designed to teach students database concepts and how to interact with a database using PostgreSQL and Python.
This project is written in Python 2.7 and it solves three problems using database queries and minimal post processing in Python.


## Problem 1:

What are the most popular three articles of all time?


## Problem 2:

Who are the most popular article authors of all time? 


## Problem 3:

On which days did more than 1% of requests lead to errors? 


## Getting Started:

To get started with this project you will need to have a couple of files.

* A Unix style terminal. Windows users, I prefer Git Bash. Mac users your regular terminal will be fine.
* The SQL database. This is located in the repository named newsdata.sql
* The tools Vagrant and VirtualBox
* The virtual machine files: https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
* The Python code logs.py also located in the repository.


## Starting up the virtual machine

1. Install the version of [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) for your operating system.
 _Windows users may have to disable Hyper-V_

2. Install [Vagrant](https://www.vagrantup.com)

3. cd into the directory with the virtual machine files then cd into the /vagrant directory

4. Use the command vagrant up to start the virtual machine.

5. Once that is complete use the command vagrant ssh to log into your virtual machine.


## Using this code

1. Put newsdata.sql and logs.py in the vagrant directory as shown above.

2. Run the command psql -f newsdata.sql This builds the database.

3. Run the logs.py file from the command line using python logs.py.

4. Answers will be displayed in a file called output.txt.
