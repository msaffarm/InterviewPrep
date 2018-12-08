### General Command related to MySQL
|Command|Description |
|--|--|
|`SHOW WARNINGS`|Display warnings|


## DATABASES

Database names are **snake_case** usually.

### Commands related to Databases
|Command|Description |
|--|--|
|`CREATE DATABASE <name>;`|Create a new database|
|`DROP DATABASE <name>;`|Drop a database|
|`USE <db_name>;`|Use a database|
|`SELECT database();`|Show the current database we are using|
|`show databases;`|Show the all the database|


## TABLES
A db is a collection of tables (and RDBMS at least)! 

### Commands related to Tables
Creating a new table
```mysql
CREATE TABLE <table_name>
    (
        column_name data_type NOT NULL,
        column_name data_type DEFAULT x,
        colname datatype AUTO_INCREMENT,
        PRIMARY KEY (colname)
    );
```
Insert data to a new table
```mysql
INSERT INTO <table_name>(col1,col2)
VALUES (val1,val2),(val1,val2);
```



|Command|Description |
|--|--|
|`SHOW TABLES;`|show avialable tables in the db|
|`DESC <tablename>;`|describe the table.|
|`SHOW COLUMNS FROM <tablename>;`|describe the table columns and datatypes|
|`DROP TABLE <tablename>;`|drop a table|
|`SELECT col1,col2 FROM <tablename>`|select data from db|



## DATATYPES

### Numeric Types
* INT
* SMALLINT
* TINYINT
* BGIINT
* MEDIUMINT
* DECIMAL
* FLOAT

### String Types
* VARCHAR (variable length char) => VARCHAR(X=maximum number of chars)
* CHAR

### Date Types
* DATE
* DATETIME


## CRUD
Create, Read, Update and Delete!


### CREATE COMMANDS

### READ COMMANDS

SELECT:
```mysql
SELECT col1,col2 FROM tablename
```

WHERE:
```mysql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

ALIASES:
```mysql
SELECT column1 AS col1, ...
FROM table_name
WHERE condition;
```

### UPDATE COMMANDS
UPDATE:
```mysql
UPDATE tablename SET col1=x WHERE col2=y;
```

### DELETE COMMANDS
DELETE:
```mysql
DELETE FROM tablename SET col1=x WHERE col2=y;
```

