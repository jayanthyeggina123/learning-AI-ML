## JOINS 

## 1.List all customers along with the films they have rented. (inner join)
select first_name,
last_name,
title
from customer
join rental
on customer.customer_id = rental.customer_id
join inventory
on rental.inventory_id = inventory.inventory_id
join film
on inventory.film_id = film.film_id;
## Join all four tables.Shows the customer's name and the film they rented.

##2. List all customers and show their rental count, including those who haven't rented any films. (left join)
select first_name,
last_name,
count(rental_id) as total_rentals
from customer
left join rental
on customer.customer_id = rental.customer_id
group by customer.customer_id, first_name, last_name;
## left join shows all customers. count() counts how many rentals each customer made.Customers with no rentals will have 0.

##3.Show all films along with their category. Include films that don't have a category assigned (right join)
select title,
name as category
from film_category
right join film
on film_category.film_id = film.film_id
left join category
on film_category.category_id = category.category_id;
## right join returns all films.if a film has no category, the category will be null.
## film is on the right side, so right join ensures every film is shown

## 4.Show all customers and staff emails from both customer and staff tables.(full outer join )
select customer.email,
staff.email
from customer
left join staff
on customer.store_id = staff.store_id
union
select customer.email,
staff.email
from customer
right join staff
on customer.store_id = staff.store_id;
## mysql doesn't support full outer join.use left join + right join + union.
## shows all customers and staff records.

##5. Find all actors who acted in the film "ACADEMY DINOSAUR". (cross join)
select first_name,
last_name,
title
from actor
cross join film
where title = 'ACADEMY DINOSAUR'
limit 10;
## cross join creates every possible combination.where clause filters to the film "ACADEMY DINOSAUR".
## in realtime, we use inner joins for this question 

##6. List all stores and the total number of staff members working in each store, even if a store has no staff.(left join)
select store.store_id,
count(staff.staff_id) as total_staff
from store
left join staff
on store.store_id = staff.store_id
group by store.store_id;
## left join returns all stores.count() counts the staff members in each store.
## if a store has no staff, the count will be 0.

##7. List the customers who have rented films more than 5 times. Include their name and total rental count (inner join)
select first_name,
last_name,
count(rental_id) as total_rentals
from customer
join rental
on customer.customer_id = rental.customer_id
group by customer.customer_id, first_name, last_name
having count(rental_id) > 5;
##inner join matches customers with their rentals.count(rental_id) counts how many times each customer rented a film.
##group by groups the records by customer.having count(rental_id) > 5 shows only customers who rented more than 5 times.

## self join example :A self join joins a table with itself.
## customers who are living in same address
select
c1.first_name as customer1,
c2.first_name as customer2,
c1.address_id
from customer c1
join customer c2
on c1.address_id = c2.address_id
where c1.customer_id < c2.customer_id;
## The table is joined with itself.address_id is used to find customers living at the same address.
## customer_id < customer_id removes duplicate pairs and prevents a customer from matching with themselves.
