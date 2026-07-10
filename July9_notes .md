#July 9th notes
## SQL Cheat Sheet

## SQL Tools

* **SQL Server**: Used to store and manage databases.
* **MySQL Workbench**: Used to write and run SQL queries.

## SQL Commands

* **DDL**: Used to create or change tables.
  Examples: `CREATE`, `ALTER`, `DROP`

* **DML**: Used to add, update, or delete data.
  Examples: `INSERT`, `UPDATE`, `DELETE`

* **DQL**: Used to get data from a table.
  Example: `SELECT`

* **DCL**: Used to give or remove permissions.
  Examples: `GRANT`, `REVOKE`

* **TCL**: Used to save or undo transactions.
  Examples: `COMMIT`, `ROLLBACK`

## Constraints

* `NOT NULL` — The column cannot be empty.
* `UNIQUE` — Values must be different.
* `PRIMARY KEY` — Unique ID for each row.
* `FOREIGN KEY` — Connects one table to another table.
* `CHECK` — Checks if a value follows a rule.
* `DEFAULT` — Adds a default value if no value is entered.

## Normalization

* **Normalization**: Reduces duplicate data in tables.
* **Denormalization**: Adds duplicate data to make queries faster.

## SQL Operations

* `AND` — Both conditions must be true.
* `OR` — At least one condition must be true.
* `NOT IN` — Excludes values from a list.
* `!=` or `<>` — Not equal to.
* `ASC` — Sorts from low to high or A to Z.
* `DESC` — Sorts from high to low or Z to A.

## Basic SELECT Query

```sql
SELECT *
FROM table_name
WHERE condition;
```

## LIKE Operator

* `%` means zero or more characters.
* `_` means one character.


## NULL Values

* `NULL` means the value is missing or unknown.
* Do not use `= NULL`.
* Use `IS NULL` to find empty values.

## GROUP BY, HAVING, and COUNT

* `GROUP BY` groups similar values.
* `COUNT()` counts rows.
* `HAVING` filters grouped results.


## ORDER BY and LIMIT

* `ORDER BY` sorts results using `ASC` or `DESC`.
* `LIMIT` controls how many rows are returned.

## SQL Query Order

```text
FROM
JOIN
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```
