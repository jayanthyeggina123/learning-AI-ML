##Primary Key (PK) – A unique column that identifies each row in a table.
##Foreign Key (FK) – A column in another table that refers to the primary key.

##customer.customer_id` → Primary Key
##payment.customer_id` → Foreign Key


## inner join - Returns only the matching rows from both tables.
select customer.customer_id,
first_name,
amount
from customer
join payment
on customer.customer_id = payment.customer_id;
## it joins customer and payment tables,shows only customer whop have made payment 

##left join - Returns all rows from the left table and matching rows from the right table.
select customer.customer_id,
first_name,
rental_id
from customer
left join rental
on customer.customer_id = rental.customer_id;
##shows all customers, even if they have never rented a film,If no rental exists, the rental columns show null

##right join - Returns all rows from the right table and matching rows from the left table.
select customer.customer_id,
first_name,
rental_id
from customer
right join rental
on customer.customer_id = rental.customer_id;
## it shows all rental records and the matching customer details.Every rental is displayed, even if no matching customer is found.

## full outer join - return all rows from both tables 
## it doesnt support directly (mysql)
select *
from customer
full outer join rental
on customer.customer_id = rental.customer_id;
## have to use union 
## returns all rows from both customer and rental tables.
## Matching rows are combined, and non-matching rows show null.

## cross join - Combines every row from one table with every row from another table.
select customer.customer_id,
store.store_id
from customer
cross join store;
##This query matches every customer with every store.No joining condition is required.

##self join 
##It is used when we want to compare rows within the same table or find relationships between rows in that table.

## Bridge Table - table used to connect two tables that have a many-to-many relationship.
## actor - film actor - film ( film actor is bridge table)
select *
from film_actor;
## gives info like actor id,film id and last update 

## Cartesian Product
## Every row from the first table is combined with every row from the second table.
select *
from customer
cross join store;
## combines every customer with every store.number of rows equals customers × stores.

## Cardinality - Describes the relationship between tables.
## One to Many: One customer → Many rentals.
## Many to Many: Many actors ↔ Many films (through film_actor).

## union - Combines the results of two queries and removes duplicates.
select first_name
from customer

union

select first_name
from actor;
## This query combines first names from both tables.Duplicate names are removed.

## union all - keeps duplicates 
select first_name
from customer
union all
select first_name
from actor;
## This query combines first names from both tables.Duplicate names are included.

## subqueries - A query written inside another query.
select *
from film
where rental_rate = (
select max(rental_rate)
from film
);
 ## drawbacks -                          reusabiity , readabiity , complexity 
## sub query - without using join 
select max(rental_rate)
from film;
## it returns 4.99
## main query
select *
from film
where rental_rate = 4.99;
##First, the inner query runs.Then, the outer query uses the result.

## Correlated Subquery - The inner query depends on the outer query and runs once for each row.
select first_name,
last_name
from customer c
where exists (
select *
from payment p
where c.customer_id = p.customer_id
);

## where c.customer_id = p.customer_id
##The inner query depends on the current customer from the outer query, so it cannot run by itself.
##This query checks each customer one by one to see if they have made any payment.If a payment exists for that customer, their name is displayed.

## Derived Table - A subquery used in the from clause.
select *
from (
select customer_id,
sum(amount) as total_amount
from payment
group by customer_id
) as payment_total;
## The subquery creates a temporary table.The outer query displays the data from that temporary table.