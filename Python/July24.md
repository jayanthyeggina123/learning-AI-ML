# Python Libraries, Pandas & Data Visualization Notes

# Libraries

## Pandas
- Pandas is a Python library used for data analysis and manipulation.
- It mainly works with **DataFrames** (rows and columns) and **Series** (single column).

```python
import pandas as pd
```

### Uses
- Read data
- Clean data
- Filter data
- Analyze data
- Merge datasets
- Handle missing values

---

## NumPy
- NumPy (Numerical Python) is used for mathematical operations and arrays.
- Pandas is built on top of NumPy.

```python
import numpy as np
```

### Uses
- Arrays
- Mathematical functions
- Matrix operations
- Random numbers

---

# Structured Files (Data Files)

Common file formats used in Pandas:

- CSV (.csv)
- Excel (.xlsx)
- JSON (.json)
- SQL Databases

---

# Reading Data

## Read CSV File

```python
df = pd.read_csv("students.csv")
```

Example

```python
import pandas as pd

df = pd.read_csv("students.csv")
print(df)
```

---

# Pandas DataFrame

A **DataFrame** is a table containing rows and columns.

Example

| Name | Age | City |
|------|----|------|
| John | 20 | NY |
| Sam | 22 | LA |

```python
print(df)
```

---

# Data Types

Shows the datatype of every column.

```python
df.dtypes
```

Example Output

```
Name      object
Age        int64
Marks    float64
```

---

# dtypes.index

Returns the column names.

```python
df.dtypes.index
```

Output

```
Index(['Name','Age','Marks'])
```

---

# describe()

Displays statistical summary of numerical columns.

```python
df.describe()
```

Includes

- Count
- Mean
- Standard Deviation
- Minimum
- Maximum
- Quartiles

---

# loc[]

Used to access rows or columns using labels.

Syntax

```python
df.loc[row, column]
```

Examples

```python
df.loc[0]

df.loc[0, "Name"]

df.loc[:, "Age"]
```

---

# iloc[]

Used to access rows or columns using index positions.

Syntax

```python
df.iloc[row, column]
```

Examples

```python
df.iloc[4]

df.iloc[0]

df.iloc[0,1]
```

---

# mean()

Finds the average.

```python
df["Marks"].mean()
```

Example

```
Marks = 80,90,70

Mean = 80
```

---

# Random Seed

Produces the same random values every time.

```python
np.random.seed(100)
```

Example

```python
np.random.seed(1)
np.random.randint(1,10,5)
```

---

# drop()

Removes rows or columns.

Drop Column

```python
df.drop("Age", axis=1)
```

Drop Row

```python
df.drop(0, axis=0)
```

---

# Matrix Data

A matrix is a 2D array.

Example

```python
matrix_data = np.array([
    [1,2],
    [3,4]
])

print(matrix_data)
```

---

# Filtering Data

Select rows based on conditions.

Example

```python
df[df["Marks"] > 80]
```

---

# Multiple Conditions

AND

```python
df[(df["Marks"] > 80) & (df["Age"] > 20)]
```

OR

```python
df[(df["Marks"] > 80) | (df["Age"] > 20)]
```

NOT

```python
df[~(df["Age"] > 20)]
```

---

# Reset Index

Resets row numbers.

```python
df.reset_index()
```

Remove old index

```python
df.reset_index(drop=True)
```

---

# Split

Split a string into multiple parts.

```python
df["Name"].str.split(" ")
```

Example

```
John Smith

↓

["John","Smith"]
```

---

# Concatenate

Join DataFrames.

```python
pd.concat([df1, df2])
```

Column-wise

```python
pd.concat([df1, df2], axis=1)
```

---

# zip() Function

Combines multiple lists.

Example

```python
names = ["John","Sam"]
marks = [80,90]

list(zip(names, marks))
```

Output

```
[('John',80), ('Sam',90)]
```

Unzip

```python
a, b = zip(*list(zip(names, marks)))
```

---

# MultiIndex

Uses multiple indexes.

Example

```python
df.set_index(["Department","Name"])
```

Example Output

```
Department Name
IT         John
HR         Sam
```

---

# Drop Missing Values

Remove rows containing missing values.

```python
df.dropna()
```

Remove columns

```python
df.dropna(axis=1)
```

---

# fillna()

Replace missing values.

Replace with 0

```python
df.fillna(0)
```

Replace with Mean

```python
df.fillna(df.mean(numeric_only=True))
```

---

# groupby()

Groups similar values.

Example

```python
df.groupby("Department").mean()
```

Example

| Department | Salary |
|------------|---------|
| IT | 70000 |
| HR | 50000 |

---

# groupby() with Transpose

Transpose converts rows into columns.

```python
df.groupby("Department").mean().T
```

`.T` means transpose.

---

# Merging Data

Combine multiple DataFrames.

---

# Merge Two DataFrames

Example

```python
pd.merge(df1, df2)
```

---

# Merge Types

Inner Join

```python
pd.merge(df1, df2, how="inner")
```

Left Join

```python
pd.merge(df1, df2, how="left")
```

Right Join

```python
pd.merge(df1, df2, how="right")
```

Outer Join (All Records)

```python
pd.merge(df1, df2, how="outer")
```

Merge using a common column

```python
pd.merge(df1, df2, on="ID")
```

---

# concat()

Row-wise

```python
pd.concat([df1, df2])
```

Column-wise

```python
pd.concat([df1, df2], axis=1)
```

---

# Applying NumPy Functions

Apply mathematical functions.

Log

```python
df.apply(lambda x: np.log(x))
```

Square Root

```python
df.apply(lambda x: np.sqrt(x))
```

Sum

```python
df.sum()
```

Mean

```python
df.mean(numeric_only=True)
```

---

# Data Visualization

Data visualization is used to represent data graphically.

Popular libraries:

- Matplotlib
- Seaborn

---

# Matplotlib

Basic plotting library.

```python
import matplotlib.pyplot as plt
```

Example

```python
plt.plot([1,2,3],[5,7,9])
plt.show()
```

---

# Seaborn

Built on top of Matplotlib.

```python
import seaborn as sns
```

Example

```python
sns.scatterplot(x="Age", y="Marks", data=df)
```

---

# Cufflinks

Cufflinks connects **Pandas** with **Plotly** to create interactive graphs.

Installation

```python
pip install cufflinks
```

Import

```python
import cufflinks as cf
cf.go_offline()
```

Example

```python
df.iplot(kind="line")
```

Other Charts

```python
df.iplot(kind="bar")
df.iplot(kind="scatter")
df.iplot(kind="hist")
```

---

# Bar Chart

Used to compare categories.

Matplotlib

```python
plt.bar(["A","B","C"], [10,20,15])
plt.show()
```

Seaborn

```python
sns.barplot(x="Department", y="Salary", data=df)
```

---

# Common Pandas Functions

| Function | Purpose |
|----------|---------|
| `pd.read_csv()` | Read CSV file |
| `df.head()` | First 5 rows |
| `df.tail()` | Last 5 rows |
| `df.info()` | Dataset information |
| `df.describe()` | Statistics summary |
| `df.dtypes` | Data types |
| `df.loc[]` | Label-based selection |
| `df.iloc[]` | Index-based selection |
| `df.mean()` | Average |
| `df.drop()` | Remove rows/columns |
| `df.dropna()` | Remove missing values |
| `df.fillna()` | Fill missing values |
| `df.groupby()` | Group data |
| `pd.concat()` | Concatenate DataFrames |
| `pd.merge()` | Merge DataFrames |
| `df.reset_index()` | Reset index |
| `df.apply()` | Apply a function |

---

# Interview Questions

### Difference between Pandas and NumPy

| Pandas | NumPy |
|---------|--------|
| Works with DataFrames | Works with Arrays |
| Used for data analysis | Used for numerical computations |
| Supports labels | Faster mathematical operations |

---

### loc vs iloc

| loc | iloc |
|------|------|
| Uses labels | Uses index positions |
| `df.loc[0,"Name"]` | `df.iloc[0,1]` |

---

### merge() vs concat()

| merge() | concat() |
|----------|-----------|
| Joins using common columns | Simply joins DataFrames |
| Similar to SQL JOIN | Stacks rows or columns |

---

### dropna() vs fillna()

| dropna() | fillna() |
|-----------|-----------|
| Removes missing values | Replaces missing values |

---

### groupby()

- Splits data into groups.
- Performs operations like `sum()`, `mean()`, `count()`, `max()`, etc.
- Combines the results into a summary.

Example

```python
df.groupby("Department")["Salary"].mean()
```
