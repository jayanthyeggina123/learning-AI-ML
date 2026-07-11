# July 10 Notes

## String Functions

* **LPAD** – Adds characters to the left side of a string until it reaches a specified length.
* **RPAD** – Adds characters to the right side of a string until it reaches a specified length.
* **SUBSTRING** – Extracts part of a string.
* **CONCAT** – Joins two or more strings together.
* **SUBSTRING** – Used to get a specific portion of a string.
* **REVERSE** – Reverses the characters in a string.
* **LENGTH** – Returns the number of characters in a string.
* **SUBSTRING with LOCATE** – Finds the position of a word using `LOCATE()` and extracts it with `SUBSTRING()`.
* **SUBSTRING_INDEX** – Returns part of a string before or after a delimiter.
* **UPPER and LOWER** – Converts text to uppercase or lowercase.
* **LEFT and RIGHT** – Returns characters from the left or right side of a string.

## Conditional Statements

* **CASE ... END AS** – Used to create conditions and return different values based on those conditions.

## Search & Pattern Matching

* **SELECT REPLACE** – Replaces specific text in a string with another value.
* **WHERE LIKE** – Searches for values that match a pattern using `%` or `_`.
* **REGEXP (ends with `$`)** – Uses regular expressions to search for patterns. `$` means the value ends with the specified text.

## String Built-in Functions

* Collection of functions used to manipulate and format string values.

## Math Built-in Functions

* **RAND** – Generates a random number.
* **MOD** – Returns the remainder after division.
* **ROUND** – Rounds a number to the nearest value or decimal places.

## Date & Time Operations

* Used to work with dates and times in SQL.
* **DATEDIFF** – Returns the difference between two dates.

## Practice Queries

* **Find customer who paid in the last 24hrs** – Query to retrieve customers who made payments within the past 24 hours.
* **CONCAT date** – Combines a date with text or another string using `CONCAT()`.
