# Method Overriding

Method overriding occurs when a **child class provides its own version of a method that already exists in the parent class**.

The child class **inherits the method but changes its behaviour** without changing the parent class.

It is useful when the parent's behaviour is not exactly what the child class needs.

Instead of creating a completely new method, the child overrides the inherited method.

---

# Encapsulation

Encapsulation is the process of **bundling data (variables) and methods together inside a class**.

It protects data by restricting direct access and providing controlled access through methods.

Private variables (`__variable`) and getter/setter methods are commonly used to achieve encapsulation.

---

# Composition

Composition is an OOP concept where **one class contains another class as one of its objects**.

Instead of inheriting from another class, a class **uses another class** to perform its work.

This is often described as a **"has-a" relationship**.

Example:

- A **Car has an Engine**
- A **Computer has a CPU**

Composition helps build complex programs by combining smaller classes.

---

# Dynamic Extension

Dynamic extension means the superclass or behaviour of a class can be **determined during program execution (runtime)** instead of being fixed beforehand.

It makes programs more flexible because decisions can be made while the program is running.

---

# Polymorphism

Polymorphism means **one interface, many forms**.

The same method name can perform different actions depending on which object calls it.

It allows different classes to implement the same method in their own way.

---

# Duck Typing

Duck typing is a feature of Python where the **type of an object is not important**.

Python only checks whether the object has the required method or behaviour.

"If it walks like a duck and quacks like a duck, then it is treated like a duck."

This is why Python is called a **dynamically typed language**.

---

# Method Overloading (Same Method, Different Parameters)

Python does **not support traditional method overloading** like Java or C++.

Instead, Python achieves similar behaviour by:

- Using default arguments
- Using `*args`
- Using `**kwargs`

This allows the same function to accept different numbers of parameters.

---

# Class Variable

A class variable belongs to the **class itself**.

All objects of the class share the same class variable.

If one object changes it, the change is visible to all objects (unless overridden by an instance variable).

---

# Instance Variable

An instance variable belongs to an **individual object**.

Each object has its own copy of the instance variable.

Changing one object's instance variable does not affect other objects.

---

# Global Variable

A global variable is declared **outside all functions and classes**.

It can be accessed from anywhere in the program.

Its scope is the entire program.

---

# Local Variable

A local variable is created **inside a function or method**.

It exists only while that function is executing.

It cannot be accessed outside that function.

---

# Instance Method

An instance method works with **object-specific data**.

It always takes `self` as the first parameter.

It can access both instance variables and class variables.

---

# Class Method

A class method works with **class-level data**.

It uses `cls` as the first parameter instead of `self`.

It is created using the `@classmethod` decorator.

Class methods can access class variables but not instance variables directly.

---

# Static Method

A static method belongs to a class but **does not use `self` or `cls`**.

It is mainly used for **utility or helper functions** that perform independent tasks, such as simple calculations or conversions.

It is created using the `@staticmethod` decorator.

---

# Decorators

A decorator is a function that **modifies or enhances another function without changing its original code**.

It returns a new function with additional behaviour.

Decorators are commonly used for:

- Logging
- Authentication
- Validation
- Measuring execution time

Python provides built-in decorators such as:

- `@staticmethod`
- `@classmethod`
- `@property`

---

# Dataclass

A dataclass is a special class provided by Python that automatically generates common methods such as:

- `__init__()`
- `__repr__()`
- `__eq__()`

It reduces boilerplate code when creating classes that mainly store data.

It is created using the `@dataclass` decorator.

---

# `__post_init__()`

`__post_init__()` is a special method used inside a dataclass.

It runs **immediately after `__init__()`**.

It is mainly used for additional initialization or validation after the object has been created.

---

# How Long Should a Class Be?

A class should only contain the variables and methods needed for a **single purpose**.

Avoid making one class responsible for many unrelated tasks.

Keeping classes small makes the code easier to understand, test, and maintain.

---

# Single Responsibility Principle (SRP)

The Single Responsibility Principle states that **a class should have only one responsibility and only one reason to change**.

Each class should focus on one specific task.

This makes programs easier to maintain and reduces code complexity.

---

# Build Applications with Python

Python is commonly used to build:

- Desktop applications
- Web applications
- Data analysis projects
- Machine learning and AI applications
- Automation scripts
- APIs
- Data visualization dashboards

---

# Store Data with SQL

SQL (Structured Query Language) is commonly used to store and manage application data.

Python can connect to databases such as:

- SQLite
- MySQL
- PostgreSQL
- SQL Server

Python performs the application logic, while SQL stores, retrieves, updates, and deletes data from the database.
