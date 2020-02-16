# Employee-Management-flask-webapp

This is developed on MacOS Catalina with Python version 2.7 using Anaconda.

## Installing Anaconda

Download [Anaconda](https://www.anaconda.com/distribution/#download-section)

### Create a Virtual Environment

	`$ conda create -n flaskenv python=2.7 anaconda`

### Activate the environment

	`$ conda activate flaskenv`

### To deactivate an active environment, use

	`$ conda deactivate`

## Install Flask

	`$ pip install Flask`
	
## Other dependencies

	`click==6.6`
Click is Command Line Interface Creation Kit which is used to add custom shell commands for the webapp.

	`itsdangerous==0.24`
ItsDangerous provides security when sending data using cryptographical signing.

	`jinja2==2.8`
Jinja2 is a templating language which is used to create HTML markup formats that are returned to the user upon an HTTP request. Moreover it is even used for Template Inheritance wherein we can save a basic layout in a base template and extend it to other pages.

	`MarkupSafe==0.23`
MarkupSafe is a string handling library that implements a text object that escapes characters so it is safe to use in HTML and XML.

	`Werkzeug==0.11.11`
Werkzeug is a utility library for WSGI(Web Server Gateway Interface) a protocol that ensures web apps and web servers can communicate effectively.
	

## Install [MySQL](https://dev.mysql.com/downloads/mysql/)

##### NOTE: Use Legacy Passowrd Encryption while setting up MySQL

	`(flaskenv):$ mysql -u root -p`

### Creating user with username- em_admin and password- em2020

	`mysql> CREATE USER 'em_admin'@'localhost' IDENTIFIED BY 'em2020';
	Query OK, 0 rows affected (0.01 sec)`

### Creating database named- emp_db

	`mysql> CREATE DATABASE emp_db;`

### Granting access to our user

	`mysql> GRANT ALL PRIVILEGES ON emp_db . * TO 'em_admin'@'localhost';`

## Models- Employee, Department and Role

### Installing Flask-Login

#### For user management and handle logging in, logging out, and user sessions.

	`$ pip install flask-login`

### Installing flask-migrate

#### Migrations allow us to manage changes we make to the models, and propagate these changes in the database.

	`$ pip install flask-migrate`

### Create Migration Repository

	`$ flask db init`

#### Creating first migration

	`$ flask db migrate`

#### Applying the migration

	`$ flask db upgrade`


### Tables will now be successfully created and can be checked by:

	`$ mysql -u root -p`

	`mysql> use em_db;`

	`mysql> show tables;
	+-----------------+
	| Tables_in_em_db |
	+-----------------+
	| alembic_version |
	| departments     |
	| employees       |
	| roles           |
	+-----------------+
	4 rows in set (0.00 sec)`

### Creating registration and login forms

	`pip install Flask-WTF`

	`pip install flask-bootstrap`

### For unit testing

	`pip install Flask-Testing`

