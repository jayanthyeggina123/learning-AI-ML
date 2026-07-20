# Python
**Python** is a **high-level, dynamically typed, multi-paradigm programming language**. It has a simple syntax that is almost like **pseudocode**, making it easy to learn and read.

---

# Dynamic Typing
Python is a **dynamically typed** language, meaning you do not need to specify the data type of a variable. The type is determined automatically at runtime.

```python
x = 10
name = "John"
price = 19.99
```

---

# Variables
A **variable** is a named location used to store data. The value of a variable can change during program execution.

```python
age = 21
name = "Alice"
```

---

# Naming Conventions for Variables
- Must start with a **letter** or an **underscore (`_`)**.
- Cannot start with a number.
- Cannot contain special characters (except `_`).
- Cannot use Python keywords or built-in function names.
- Variable names are case-sensitive.

```python
name = "John"
_age = 20
studentName = "Alice"
```

---

# Data Types
Python supports several built-in data types.

- Integer (`int`)
- Float (`float`)
- String (`str`)
- Boolean (`bool`)
- Complex (`complex`)

```python
a = 10
b = 3.14
c = "Hello"
d = True
e = 2 + 3j
```

---

# Complex Literals
A **complex literal** represents a complex number using the format `real + imaginaryj`.

```python
num = 5 + 2j
```

---

# Type Casting
**Type Casting** converts one data type into another.

- **Implicit Casting:** Done automatically by Python.
- **Explicit Casting:** Done using functions like `int()`, `float()`, and `str()`.

```python
num = int("25")
price = float(10)
text = str(100)
```

---

# Boolean
A **Boolean** data type has only two values:
- `True`
- `False`

It is commonly used in conditions and comparisons.

```python
is_student = True
```

---

# Strings
A **String** is a sequence of characters enclosed in **single (`' '`)** or **double (`" "`)** quotes.

```python
name = "Alice"
city = 'Boston'
```

---

# Operators in Python
Operators perform operations on variables and values.

### Arithmetic Operators
```python
+, -, *, /, %, //, **
```

### Comparison Operators
```python
==, !=, >, <, >=, <=
```

### Logical Operators
```python
and, or, not
```

### Assignment Operators
```python
=, +=, -=, *=, /=, %=
```

---

# Input Function
The `input()` function is used to accept input from the user.

```python
name = input("Enter your name: ")
```

---

# Type Conversion Functions
Python provides built-in functions to convert data types.

```python
int()
float()
str()
bool()
```

Example:

```python
age = int(input("Enter age: "))
```

---

# Formatted Strings (f-Strings)
An **f-string** allows variables and expressions to be embedded directly inside a string.

```python
name = "John"
print(f"My name is {name}")
```

---

# `.format()` Method
The `.format()` method is another way to insert values into strings.

```python
name = "John"
print("My name is {}".format(name))
```

---

# Boolean Evaluation
Python evaluates conditions to either `True` or `False`.

```python
print(10 > 5)
print(5 == 8)
```

---

# Branching (`if`, `elif`, `else`)
Branching allows a program to make decisions based on conditions.

```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

---

# Nested `if`
A **Nested `if`** is an `if` statement inside another `if` statement.

```python
if condition1:
    if condition2:
        ...
```

---

# Loops
Loops are used to execute a block of code repeatedly.

### `for` Loop
Used to iterate over a sequence.

```python
for i in range(5):
    print(i)
```

### `while` Loop
Executes as long as the condition is `True`.

```python
while condition:
    ...
```
