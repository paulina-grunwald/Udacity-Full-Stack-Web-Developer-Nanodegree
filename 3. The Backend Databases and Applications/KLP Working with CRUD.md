# Key Learning points for Working with CRUD



## Table of contents

1. Working with CRU




## 1. Working with CRUD

__CRUD__ - Create, Read, Update, Delete

__Object-Rational Mapping (ORM)__ - transforms code to the SQL statement.

### Creating a Database

Restaurant: name, id
MenuItem: name, id, description, price, course, restaurant_id

restaurant_id is a foreign key that will assign relation to table restaurant (id column)/


[__SQLAlchemy__](http://www.sqlalchemy.org/)
With SQLAlchemy we can write a single python file to set up a database.

Creating database using ```SQLAlchemy``` has few major components:
- __Configuration__:
  - used for importing necessary modules,
  - creates instances of declarative base),
  - creates (or connects) the database and adds tables to columns.
- __Class__ (used to represent data in python),
- __Table__ (represents specific table in the database),
- __Mapper__ (links the columns of the table to the classes that represent them).
