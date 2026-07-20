##Subquery
## 1.Display all customer details who have made more than 5 payments.
select *
from customer
where customer_id in (
select customer_id
from payment
group by customer_id
having count(*) > 5
);
## Subquery (in, having)

## 2.Find the names of actors who have acted in more than 10 films.
select first_name,
last_name
from actor
where actor_id in (
select actor_id
from film_actor
group by actor_id
having count(film_id) > 10
);
## Subquery (in, group by)

## 3.Find the names of customers who never made a payment.
select first_name,
last_name
from customer
where customer_id not in (
select customer_id
from payment
);
## Subquery (not in)
## subquery gets all customer IDs from the payment table. main query shows customers who are not in that list.

## 4.List all films whose rental rate is higher than the average rental rate.
select title,
rental_rate
from film
where rental_rate >
(
select avg(rental_rate)
from film
);
## Subquery (avg)
## subquery calculates the average rental rate. main query shows films with a higher rental rate.

## 5. List the titles of films that were never rented
select title
from film
where film_id not in (
select film_id
from inventory
where inventory_id in (
select inventory_id
from rental
)
);
## subquery finds all rented films.The main query shows films that were never rented.

## Temp tables
## 6.Store customers who are active.
create temporary table customer5_month as
select distinct month(rental_date) as rental_month
from rental
where customer_id = 5;

select distinct customer_id
from rental
where month(rental_date) in (
select rental_month
from customer5_month
);
## emporary table stores the rental month of customer 5. second query finds customers who rented in the same month.

## VIEW
## 7.Find all staff members who handled a payment greater than the average payment amount.
create view above_avg_payment as
select *
from payment
where amount >
(
select avg(amount)
from payment
);

select distinct staff_id
from above_avg_payment;
## view stores payments greater than the average amount, second query shows the staff members who handled those payments.

## 8. Show the title and rental duration of films whose rental duration is greater than the average.
create view long_rental_films as
select title,
rental_duration
from film
where rental_duration >
(
select avg(rental_duration)
from film
);
select *
from long_rental_films;
## view stores films with rental duration greater than the average. second query displays those films.

## CTE
## 9.Find all customers who have the same address as customer with ID 1.
with customer_address as
(
select address_id
from customer
where customer_id = 1
)

select first_name,
last_name
from customer
where address_id in (
select address_id
from customer_address
);
## CTE stores the address of customer 1. main query finds customers living at the same address.

## 10.List all payments that are greater than the average of all payments.
with avg_payment as
(
select avg(amount) as average_amount
from payment
)

select *
from payment
where amount >
(
select average_amount
from avg_payment
);
## CTE calculates the average payment amount.main query displays payments greater than the average.
