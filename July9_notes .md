# SQL Notes

## SQL Tools

* **SQL Server**: A database management system used to store and manage data.
* **MySQL Workbench**: A graphical tool used to create databases, write SQL queries, and manage MySQL servers.

## SQL Command Categories

* **DDL (Data Definition Language)**: Used to create or modify database objects.
  Examples: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`

* **DML (Data Manipulation Language)**: Used to add, update, or delete data.
  Examples: `INSERT`, `UPDATE`, `DELETE`

* **DQL (Data Query Language)**: Used to retrieve data from a database.
  Example: `SELECT`

* **DCL (Data Control Language)**: Used to control user access and permissions.
  Examples: `GRANT`, `REVOKE`

* **TCL (Transaction Control Language)**: Used to manage database transactions.
  Examples: `COMMIT`, `ROLLBACK`, `SAVEPOINT`

## Constraints

Constraints are rules used to control the type of data that can be stored in a table.

* **NOT NULL**: A column cannot contain an empty or `NULL` value.
* **UNIQUE**: All values in a column must be different.
* **PRIMARY KEY**: Uniquely identifies each row in a table. It cannot contain `NULL` values.
* **FOREIGN KEY**: Connects one table to another table using a related column.
* **CHECK**: Ensures that values meet a specific condition.
* **DEFAULT**: Adds a default value when no value is provided.

## Normalization and Denormalization

* **Normalization**: Organizing database tables to reduce duplicate data and improve data consistency.
* **Denormalization**: Adding duplicate data intentionally to improve query performance.

## SQL Operators

* **AND**: Returns rows only when all conditions are true.
* **OR**: Returns rows when at least one condition is true.
* **NOT**: Reverses a condition.
* **NOT IN**: Returns rows that are not included in a specified list.
* **Not equal to**: Use `!=` or `<>`.

Example:

```sql
SELECT *
FROM employees
WHERE department != 'HR';
```

## SELECT Statement

The `SELECT` statement is used to retrieve data from a table.

```sql
SELECT column_name
FROM table_name
WHERE condition;
```

Example:

```sql
SELECT *
FROM students
WHERE age > 20;
```

## LIKE Operator

The `LIKE` operator is used to search for a specific pattern.

* `%` represents zero or more characters.
* `_` represents exactly one character.

Examples:

```sql
SELECT *
FROM employees
WHERE name LIKE 'A%';
```

This returns names that start with `A`.

```sql
SELECT *
FROM employees
WHERE name LIKE '_a%';
```

This returns names where the second letter is `a`.

## NULL Values

`NULL` means that a value is missing or unknown.

* `NULL` values are not returned using `= NULL`.
* Use `IS NULL` to find missing values.
* Use `IS NOT NULL` to find values that are available.

Examples:

```sql
SELECT *
FROM employees
WHERE manager_id IS NULL;
```

```sql
SELECT *
FROM employees
WHERE manager_id IS NOT NULL;
```

## GROUP BY and HAVING

* **GROUP BY**: Groups rows with the same values.
* **HAVING**: Filters grouped data.
* **COUNT()**: Counts the number of rows.

Example:

```sql
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

## ORDER BY

`ORDER BY` is used to sort query results.

* `ASC`: Sorts in ascending order. This is the default.
* `DESC`: Sorts in descending order.

Example:

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

## LIMIT

`LIMIT` is used to restrict the number of rows returned.

Example:

```sql
SELECT *
FROM employees
LIMIT 5;
```

## SQL Query Execution Order

The general order in which SQL processes a query is:

1. `FROM`
2. `JOIN`
3. `WHERE`
4. `GROUP BY`
5. `HAVING`
6. `SELECT`
7. `ORDER BY`
8. `LIMIT`
