## temp tables : Used to store temporary data
## table that exists only for the current MySQL session.
## It stores temporary data.It is automatically deleted when you close MySQL.
create temporary table active_customers as
select customer_id, first_name, last_name
from customer
where active = 1;
## to view data 
select *
from active_customers;
## This query creates a temporary table containing only active customers.
##limitations:
## Exists only during the current session.Automatically deleted when the session ends.
## Cannot be shared with other users.


## CTE common table expression : Mainly used to simplify queries
## temporary result set created using the "with" keyword.
## It exists only while the query is running.It makes long SQL queries easier to read and understand.
## It is similar to a temporary table, but you don't have to create or delete it.
with expensive_films as (
select title, rental_rate
from film
where rental_rate > 3
)
select *
from expensive_films;
##This query first creates a temporary result called expensive_films.
##Then it displays all films whose rental rate is greater than 3.
select title, rental_rate
from film
where rental_rate > 3;
## This result is stored temporarily as expensive_films.
select *
from expensive_films;
## Now SQL reads the temporary result and displays it.
## limitations
##Exists only while the query is running.Cannot be reused in another query.
##May be slower than simple queries for small tasks.Not meant for storing data permanently.


##Recursive CTE : it calls itself repeatedly until a stopping condition is met.
##Generating number sequences.Working with hierarchical data (like employee-manager relationships).
##Traversing parent-child relationships.
with recursive numbers as (
select 1 as num

union all

select num + 1
from numbers
where num < 100
)
select *
from numbers;
## The query starts with the number 1.It keeps adding 1 until the number reaches 100, then it stops.
##limitations:
##Can be slow for large amounts of data.May run forever if the stopping condition is missing.
##Uses more memory than a simple query.


## view : virtual table 
## It does not store actual data.It stores only the SQL query.
## Every time you use the view, MySQL runs the query again.
create view active_customers as
select customer_id,
first_name,
last_name
from customer
where active = 1;
## to display :
select *
from active_customers;
## A view stores only the query, not the data. It always shows the latest data from the original table.
## limitations :
## Does not store data, so it runs the query every time.Can be slower if the query is complex.
## Some views cannot be updated.

## view is called a blueprint because it only defines how data should be displayed.


## stored procedure : saved SQL program.
## Similar to a function in programming.
## It can contain multiple SQL statements.It can be executed whenever needed.
delimiter //
create procedure show_customers()
begin

select *
from customer;

end //
delimiter ;

call show_customers();
## A stored procedure saves SQL code inside the database. 
## Instead of writing the same query repeatedly, you can simply call the procedure.


## dynamic stored procedure : creates and executes SQL while the program is running.
set @sql = 'select * from customer';
prepare stmt from @sql;
execute stmt;
deallocate prepare stmt;
## The SQL query is stored in a variable and then executed. This is useful when the query changes dynamically.
##Write Query -> Store in @sql -> prepare stmt -> execute stmt -> Display Result -> deallocate stmt
set @sql = 'select * from customer';
prepare stmt from @sql;
execute stmt;
deallocate prepare stmt;
## deallocation of one line 
set @sql = 'select * from film';
prepare stmt from @sql;
execute stmt;
deallocate prepare stmt;


## delimiter : tells MySQL where a SQL statement ends.
##By default, MySQL uses:
;
When creating a stored procedure, we temporarily change it:
delimiter //
After the procedure, change it back:
delimiter ;

##Inside a stored procedure there are many semicolons (;). 
##if we don't change the delimiter, MySQL thinks the procedure ends at the first semicolon.

## info schema - meta data 
## Information Schema is a special database that stores information about all databases, tables, and columns.
## Metadata means "data about data."It stores information such as:
Database names
Table names
Column names
Data types
Constraints
##It does not store customer records or film details.
select *
from information_schema.schemata;
## This query displays all databases available in MySQL.
 
##describe : describe is used to view the structure of a table.
desc table_name;
describe customer;
