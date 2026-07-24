# Python Extensions

# File Operations

Used to create, read, write, update, and delete files in Python.

---

# Working with Text Files

Stores data in plain text format (such as `.txt` files). Python provides different file modes to read and write text files.

---

# Read Mode (`r`)

Used to open and read the contents of a file.

---

# Write Mode (`w`)

Used to create a new file or overwrite the contents of an existing file.

---

# Read First 10 Characters

`read(10)` reads only the first 10 characters from a file.

---

# Read Line by Line

Reads one line at a time from a file. Useful for large files.

---

# Read File into a List

`readlines()` reads all lines from a file and stores them as elements in a list.

---

# Copy File

Reads the contents of one file and writes them into another file.

---

# `r+` Mode

Allows both reading and writing in the same file.

---

# Working with Excel Files

Stores structured data in rows and columns. Python uses the **Pandas** library to read, write, and analyze Excel files.

---

# Pandas

A Python library used for data analysis and working with structured data.

---

# DataFrame

A two-dimensional table with rows and columns, similar to an Excel spreadsheet.

---

# Modules

A single Python file that contains functions, variables, or classes.

---

# Libraries

A collection of related modules that provides additional functionality in Python.

---

# Built-in Modules

Predefined modules provided by Python that can be used directly without creating them.

**Example:**

```python
import math

print(math.sqrt(25))
```

---

# User-defined Module (`mymath.py`)

A Python file created by the programmer to store reusable functions and variables.

---

# Exception Handling

Prevents a program from crashing when an error occurs.

---

# `try-except`

`try` contains code that may cause an error, and `except` handles the error if it occurs.

---

# `try-except-finally`

`try` executes the code, `except` handles errors, and `finally` always executes whether an error occurs or not.

---

# `try-finally`

`finally` always executes after the `try` block. Commonly used to close files or release resources.

---

# Connecting to Databases

Used to store, retrieve, update, and manage data.

---

# SQLite (`sqlite3`)

A lightweight database built into Python. It stores data in a single database file and does not require a separate database server.
