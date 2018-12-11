### General Command related to MySQL
|Command|Description |
|--|--|
|`SHOW WARNINGS`|Display warnings|


## **DATABASES**

Database names are **snake_case** usually.

### Commands related to Databases
|Command|Description |
|--|--|
|`CREATE DATABASE <name>;`|Create a new database|
|`DROP DATABASE <name>;`|Drop a database|
|`USE <db_name>;`|Use a database|
|`SELECT database();`|Show the current database we are using|
|`show databases;`|Show the all the database|


## **TABLES**
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
|`SELECT col1,col2 FROM <tablename>`|select data from table|
|`SELECT DISTINCT col1, FROM <tablename>`|select distinct col1 from table|



## **DATATYPES**

### Numeric Types
* INT
* SMALLINT
* TINYINT
* BGIINT
* MEDIUMINT
* DECIMAL (like DECIMAL(total_max_num_of_digits,digits_after_decimal_point))
* FLOAT

### String Types
* VARCHAR (variable length char) => VARCHAR(X=maximum number of chars)
* CHAR (has the same lenght;suitable for fixed-length values like gender)

### Date Types
* DATE 'YYYY-MM-DD'
* TIME 'HH:MM:SS'
* DATETIME 
* TIMESTAMP (it takes less space)


## **CRUD**
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

ORDER BY:
```mysql
SELECT column1 AS col1, ...
FROM table_name
WHERE condition;
ORDER BY col2 ASC[DESC];
```
Ticky part: order by two columns one desc and the other asc!
```
SELECT column1 AS col1, ...
FROM table_name
WHERE condition;
ORDER BY col1 ASC, col2 DESC;
```

LIMIT:
```mysql
SELECT column1 AS col1, ...
FROM table_name
WHERE condition;
ORDER BY col2 ASC[DESC]
LIMIT X; [LIMIT startpoint,number_of_items]
```

LIKE:
```
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```
#### WILDCARDS
% is multiple chars!
_ is one char!


### **AGGREGATE COMMANDS**
COUNT:
```
SELECT COUNT(col1) FROM tablename
```

GROUP BY:
```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```

MIN and MAX
```
SELECT MIN/MAX(column_name)
FROM table_name
WHERE condition;
```

HAVING:
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.
```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

OTHER FUNCTIONS:
* SUM
* AVG

### LOGICAL OPERATORS
* NOT EQUAL [!=]
* NOT LIKE
* GREATER THAN [>]
* LESS THAN [<]
* LOGICAL AND [&& or AND]
* LOGICAL OR [|| or OR]
* BETWEEN [BETWEEN x AND Y]
* IN with a list [x IN (x1,x2,x3) ]
* Modulo [%]
* CASE
```
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```

### MATH OPERATORS
* FLOOR => round to nearest integer
* CEIL




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
DELETE WHOLE TABLE:
```mysql
DELETE FROM tablename SET col1=x WHERE col2=y;
```


### SQL STRING FUNCTIONS
The link to all string functions available in MySQL

https://dev.mysql.com/doc/refman/8.0/en/string-functions.html


CONCAT
```mysql
SELECT CONCAT(col1,'sep!',col2) AS col FROM tablebame;
```

CONCAT_WS= Concat with separator
```mysql
SELECT CONCAT_WS('sep!',col1,col2) AS col FROM tablebame;
```

SUBSTRING
```mysql
SELECT SUBSTRING(col1,beging,end) AS col FROM tablebame;
```

REPLACE
```mysql
SELECT REPLACE(col1,char1,char2) FROM tablebame;
```

REVERSE
```mysql
SELECT REVERSE(col1) FROM tablebame;
```

CHAR_LENGTH
```mysql
SELECT CHAR_LENGTH('a text!');
```


UPPER & LOWER
```mysql
SELECT UPPER('a text!');
```


### **Relationship**
FOREIGN KEY:
```
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
```

## **JOINS**

IMPLICIT INNER JOIN:
```
SELECT * FROM customers, orders 
WHERE customers.id = orders.customer_id;
```

EXPLICIT INNER JOIN:
```
SELECT * FROM cutomers
(INNER) JOIN ordrer ON cutomers.id = orders.customer_id;
```

LEFT JOIN:
```
SELECT * FROM customers
LEFT JOIN order ON customers.id = orders.customer_id;
```


### FUNCTIONS
Some MySQL functions that come in handy: https://www.w3schools.com/sql/sql_ref_mysql.asp

## DATABSE TRIGGERS
Triggers are SQL codes if certain changes are made to tables and consist of 3 main components
* Trigger time is either BEFORE or AFTER
* Triger event is UPDATE, INSERT or DELETE
* Table name!
```
CREATE TRIGGER tirgger_name
    trigger_time trigger_event ON tablename FOR EACH ROW
    BEGIN
    ...
    END; 
```


## **SUBQUERIES**
A good resource on using subqueries: https://community.modeanalytics.com/sql/tutorial/sql-subqueries/

Subqueries need to be named. For example:
```
SELECT sub.*
FROM (
.......
) sub
;
```
