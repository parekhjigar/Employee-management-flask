# Employee-Management-flask-webapp

This is developed on MacOS Catalina

## Installing Anaconda

Download [Anaconda](https://www.anaconda.com/distribution/#download-section)

### Create a Virtual Environment

	`$ conda create -n flaskenv python=2.7 anaconda`

#### Activate the environment

	`$ conda activate flaskenv`

##### To deactivate an active environment, use

	`$ conda deactivate`

## Install Flask

	`$ pip install Flask`

## Install [MySQL](https://dev.mysql.com/downloads/mysql/)

**NOTE: Use Legacy Passowrd Encryption while setting up MySQL**

(flaskenv):$ mysql -u root -p

##### Creating user with username- em_admin and password- em2020

mysql> CREATE USER 'em_admin'@'localhost' IDENTIFIED BY 'em2020';
Query OK, 0 rows affected (0.01 sec)

##### Creating database named- emp_db

mysql> CREATE DATABASE emp_db;

##### Granting access to our user

mysql> GRANT ALL PRIVILEGES ON emp_db . * TO 'em_admin'@'localhost';

