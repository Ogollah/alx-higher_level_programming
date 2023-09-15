# 0x0F. Python - Object-relational mapping

## `Python` `OOP` `SQL` `MySQL` `ORM` `SQLAlchemy`

# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

# Install and activate venv

To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

# Install MySQLdb module version 2.0.x

For installing `MySQLdb`, you need to have `MySQL` installed: How to install MySQL 8.0 in Ubuntu 20.04

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

# Install `SQLAlchemy` module version `1.4.x`

```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```

Also, you can have this warning message:

```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
  cursor.execute(statement, parameters)
```

You can ignore it.

# Tasks

## 0. Get all states

## 1. Filter states

## 2. Filter states by user input
