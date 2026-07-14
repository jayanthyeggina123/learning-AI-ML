

## 1. Get all customers whose first name starts with 'J' and who are active.
select *
from customer
where first_name like 'j%'
and active = 1;
## the customer table has a first_name field and a active field (1 means active, 0 means inactive). 
## So we use a WHERE clause with a condition that the first name starts with 'J' and active=1 

## 2. Find all films where the title contains the word 'ACTION' or the description contains 'WAR'.
select * from film
where title like '%action%'
or description like '%war%';
## The percent signs (%) mean that 'ACTION' or 'WAR' can appear anywhere in the title or description. 
## The OR ensures that if either condition is true, that film will be returned.

## 3. List all customers whose last name is not 'SMITH' and whose first name ends with 'a'.
select *
from customer
where last_name != 'smith'
and first_name like '%a';
## last_name != 'smith' ensures we exclude any customer with the last name 'smith'.
## first_name like '%a' ensures we only select customers whose first name ends with 'a'.

## 4. Get all films where the rental rate is greater than 3.0 and the replacement cost is not null.
select * from film
where rental_rate > 3.0
and replacement_cost is not null;
## The rental_rate > 3.0 condition ensures we only get films with a rental rate higher than 3.0.
## The replacement_cost not null condition makes sure we exclude any films that don’t have a replacement cost set.

## 5. Count how many customers exist in each store who have active status = 1.
select store_id, count(*) as total_customers
from customer
where active = 1
group by store_id;
##it counts the number of active customers (active = 1) in each store.
##It groups customers by store_id and displays the total number of active customers for every store.

## 6. Show distinct film ratings available in the film table.
select distinct rating from film;
##select - column 
##distinct - remove duplicates 
##from film - film table 

## 7 Find the number of films for each rental duration where the average length is more than 100 minutes.
select rental_duration,
count(*) as total_films,
avg(length) as average_length
from film
group by rental_duration
having avg(length) > 100;
## This query groups films by rental_duration, counts the number of films, and calculates the average film length for each group.
## It only shows rental durations where the average film length is greater than 100 minutes.

## 8 List payment dates and total amount paid per date, but only include days where more than 100 payments were made.
select * from payment;

select date(payment_date) as payment_day,
sum(amount) as total_amount,
count(*) as total_payments
from payment
group by date(payment_date)
having count(*) > 100;
##it groups all payments by date and calculates the total amount paid each day.
## It only shows the dates where more than 100 payments were made.

## 9 Find customers whose email is null or ends with '.org'.
select * from customer
where email is null
or email like '%.org';

## 10 List all films with rating 'PG' or 'G', and order them by rental rate in descending order.
select *from film
where rating = 'pg'
or rating = 'g'
order by rental_rate desc;
##it shows all films with a rating of 'pg' or 'g'.
## It sorts the results by rental_rate from highest to lowest using order by rental_rate desc.


## 11 Count films for each length where the title starts with 'T' and the count is more than 5.
select length, count(*) as total_films from film
where title like 't%'
group by length
having count(*) > 5;
## no film length has more than 5 films whose titles start with 't'

select length,
count(*) as total_films
from film
where title like 't%'
group by length;
## without having condition 

## 12 List all actors who have appeared in more than 10 films.
select actor.actor_id,
first_name,
last_name,
count(film_id) as total_films
from actor
join film_actor
on actor.actor_id = film_actor.actor_id
group by actor.actor_id, first_name, last_name
having count(film_id) > 10;
##it joins the actor and film_actor tables to count how many films each actor has appeared in.
## it only shows actors who have acted in more than 10 films.

## 13 Find the top 5 films with the highest rental rates and longest lengths combined.ordering by rental rate first and length second.

select title,
rental_rate,
length
from film
order by rental_rate desc,
length desc
limit 5;
##shows the top 5 films with the highest rental rates. If two films have the same rental rate, it sorts them by length from longest to shortest.
## in this case, both rental rate and lenght are same for all.

## 14 Show all customers with the total number of rentals they have made.ordered from most to least rentals.
select customer.customer_id,
first_name,
last_name,
count(rental.rental_id) as total_rentals
from customer
left join rental
on customer.customer_id = rental.customer_id
group by customer.customer_id, first_name, last_name
order by total_rentals desc;
## This displays the actor's first name, last name, and the total number of films they have acted in.
## Only actors with more than 10 films are included in the result.


## 15 List the film titles that have never been rented.
select distinct film.title
from film
join inventory
on film.film_id = inventory.film_id
left join rental
on inventory.inventory_id = rental.inventory_id
where rental.rental_id is null;
## it shows the titles of films that have never been rented.
## If every film has been rented at least once in the Sakila database, the query will return no rows.
