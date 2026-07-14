# SQL Notes – Joins and Subqueries

# Joins

## What is a Join?

A **join** is used to combine data from two or more tables using a common column. It helps us retrieve related information stored in different tables.

---

## Inner Join

- Returns only the matching rows from both tables.
- If there is no match, the row is not displayed.

---

## Left Join

- Returns all rows from the left table.
- If there is no matching row in the right table, it displays `NULL`.

---

## Right Join

- Returns all rows from the right table.
- If there is no matching row in the left table, it displays `NULL`.

---

## Full Outer Join

- Returns all rows from both tables.
- If there is no match, `NULL` is displayed for the missing values.
- **MySQL does not support `FULL OUTER JOIN` directly.**
- It can be achieved by combining `LEFT JOIN` and `RIGHT JOIN` using `UNION`.

---

# Bridge Table

A **bridge table** connects two tables that have a **many-to-many relationship**.

### Example (Sakila)

```
actor
   |
film_actor
   |
film
```

Here, **film_actor** is the bridge table because it connects actors and films.

---

# Cartesian Product

A **Cartesian Product** combines every row from one table with every row from another table.

If one table has 100 rows and another has 2 rows, the result will contain **200 rows**.

It usually happens when there is no join condition.

---

# Cardinality

**Cardinality** describes the relationship between two tables.

### Types

- One to One (1:1)
- One to Many (1:M)
- Many to Many (M:N)

### Example

- One customer → Many rentals (One to Many)
- Many actors ↔ Many films (Many to Many)

---

# Cross Join

A **Cross Join** returns every possible combination of rows from two tables.

- No `ON` condition is required.
- It produces a Cartesian Product.

---

# Union

`UNION` combines the results of two queries.

- Removes duplicate rows.
- Both queries must have the same number of columns and compatible data types.

---

# Union All

`UNION ALL` also combines the results of two queries.

- Keeps duplicate rows.
- Faster than `UNION` because it does not remove duplicates.

---

# Subqueries

## What is a Subquery?

A **subquery** is a query written inside another SQL query.

The result of the inner query is used by the outer query.

---

# Scope of a Subquery (Execution Level)

The **subquery always executes first**.

After the subquery returns the result, the outer query executes using that result.

Execution order:

1. Inner query
2. Outer query

---

# Correlated Subquery

A **correlated subquery** depends on the outer query.

- It executes once for every row returned by the outer query.
- It cannot run independently.

---

# Derived Table

A **derived table** is a subquery written inside the `FROM` clause.

- It creates a temporary table.
- The outer query uses this temporary table for further processing.

---

# Execution Order

For a normal subquery:

1. SQL executes the inner query.
2. The inner query returns the result.
3. SQL executes the outer query using that result.

This is why we say:

> **First the subquery executes, then the main query executes.**
