# Indexes
An **Index** is a database object that helps retrieve data faster. It improves query performance, reduces search time, and lowers the overall cost of database operations.

---

# Clustered Index
A **Clustered Index** stores the table data in the same order as the index. Since the data can only be sorted in one way, a table can have only **one clustered index**. In MySQL, the **Primary Key** is clustered by default.

---

# Non-Clustered Index
A **Non-Clustered Index** stores the index separately from the actual table data. It contains pointers to the rows, allowing faster searches without changing the physical order of the table. A table can have **multiple non-clustered indexes**.

---

# Creating a Non-Clustered Index
A **Non-Clustered Index** is typically created on **non-primary key columns** to improve the performance of search, filter, and sorting operations.

### Syntax
```sql
CREATE INDEX index_name
ON table_name(column_name);
```

---

# Natural Key
A **Natural Key** is a primary key formed from one or more existing columns that are naturally unique in the real world, such as an email address, Social Security Number, or passport number.

---

# Surrogate Key
A **Surrogate Key** is a system-generated primary key with no business meaning. It is usually an auto-incrementing integer or a UUID and is used solely to uniquely identify each row.
