# Object-Oriented Programming (OOP)

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **classes** and **objects**. It helps make programs more organized, reusable, and easier to maintain.

Instead of writing everything in one place, we divide the program into small objects that work together.

### Features of OOP

- Inheritance
- Reusability
- Encapsulation
- Polymorphism
- Abstraction

### Encapsulation

Encapsulation means **data and code are bundled together** inside a class.

---

# Class and Objects

## Class

A **class** is a **blueprint (template)** used to create objects.

## Object

An **object** is an **instance of a class** created from a class.

Objects contain **methods** and **data**.

---

# Self

`self` refers to the **current object**.

- It is always the **first parameter** inside an instance method.
- It allows an object to access its own variables and methods.

---

# Methods

A **method** is a **function written inside a class**.

Methods define the actions that an object can perform.

---

# `__init__()`

`__init__()` is a **special method (constructor)** that runs automatically whenever an object is created.

It is mainly used to initialize object variables.

---

# `__str__()`

`__str__()` controls **what is displayed when we print an object**.

It returns a human-readable string representation of the object.

---

# `__repr__()`

`__repr__()` returns the **official string representation** of an object.

It is mainly used for debugging and by developers.

---

# Advantages of OOP

1. Abstraction
2. Inheritance
3. Reusability
4. Encapsulation

---

# Abstraction

Abstraction means **hiding internal implementation details** and showing only the necessary functionality.

It helps:

- Protect sensitive information
- Restrict direct access to internal details
- Reduce complexity

---

## Methods of Achieving Abstraction

### 1. Abstract Class

An **abstract class** hides implementation details and forces child classes to implement the required methods.

### 2. Private Members (Double Underscore `__`)

Using **double underscores (`__`)** before a variable makes it **private**, preventing direct access from outside the class.

### 3. `__dict__`

`__dict__` returns a **dictionary containing all the attributes of an object**.

---

# Encapsulation Using Methods

Encapsulation is achieved by **keeping data (variables) and methods together inside a class** and controlling access to that data through methods.

It protects data by allowing controlled access using methods such as getters and setters.

---

# Inheritance


Inheritance is an OOP feature where **one class acquires (inherits) the properties and methods of another class**.

It helps in **code reusability**.

---

## Parent Class

A **Parent Class** (also called **Base Class** or **Super Class**) is the class whose properties and methods are inherited by another class.

---

## Child Class

A **Child Class** (also called **Derived Class** or **Sub Class**) inherits the properties and methods of the parent class.

> **Note:** A child class **can inherit** from a parent class. A parent class **cannot automatically access child-specific methods or properties**.

---

# `*args`


`*args` allows a function or method to accept **any number of positional arguments**.

The values are stored as a **tuple**.

---

# `**kwargs`


`**kwargs` allows a function or method to accept **any number of keyword arguments**.

The values are stored as a **dictionary**.

---

# Args vs Kwargs

| `*args` | `**kwargs` |
|----------|------------|
| Accepts positional arguments | Accepts keyword arguments |
| Stored as a tuple | Stored as a dictionary |

---

# Positional and Keyword Arguments

- **Positional arguments** are matched based on their position.
- **Keyword arguments** are matched using parameter names.

### Rule

**Positional arguments must come before keyword arguments.**

Correct:

```python
student("John", age=20)
```

Incorrect:

```python
student(name="John", 20)
```

This produces a `SyntaxError` because positional arguments cannot follow keyword arguments.
