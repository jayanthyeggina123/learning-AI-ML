use sakila;
show tables;
select * from actor;
DESCRIBE customer;
describe film;
describe rental;

select * from customer;
## returns all columns from table 

select first_name, last_name, email from customer;
## returns only selected columns 

select * from customer where active = 1;
##filter rows of active customers 

SELECT * from customer
WHERE active = 1
AND store_id = 2;
## customer is active and store id = 2

select * from customer 
where store_id = 1
or store_id =2;
## returns customers from wither store 1 or 2 

select *
FROM customer
WHERE store_id NOT IN (1);
## shows customers that are not in 1 



select distinct address_id from customer;
select * from actor limit 5;
SELECT COUNT(*) from actor;
SELECT rating, COUNT(*) AS total_films FROM film GROUP BY rating;
SELECT rating, COUNT(*) AS total_films
FROM film
GROUP BY rating
having COUNT(*) < 200;

##lpad 
select first_name,
lpad(first_name, 10, '*') as new_name
from customer;
##Adds * to the left of the customer's first name until it becomes 10 characters long.

##rpad
select first_name,
rpad(first_name, 10, '*') as new_name
from customer;
##Adds * to the right of the customer's first name until it becomes 10 characters long.

##substring()
select first_name,
substring(first_name, 1, 3) as short_name
from customer;
##Returns the first 3 letters of each customer's first name.

##concat() join 2 or more strings 
select concat(first_name, ' ', last_name) as full_name
from customer;
##Combines the first name and last name into one full name.

##reverse()
select first_name,
reverse(first_name) as reverse_name
from customer;
##Displays the customer's first name in reverse order.

##ength()
select first_name,
length(first_name) as total_letters
from customer;
##Shows the number of characters in each first name.

##substring() with locate()
select description,
substring(description, locate('a', description), 10) as result
from film;
##Finds the first letter a in the description and returns the next 10 characters.

##substring_index()
select email,
substring_index(email, '@', 1) as username
from customer;
##Returns only the username part of the email before @.

##upper()
select upper(first_name) as upper_name
from customer;
##Converts every first name into uppercase letters.

select lower(last_name) as lower_name
from customer;
#Converts every last name into lowercase letters.


##left 
select left(first_name, 2) as first_two_letters
from customer;

select left(first_name, 4) as first_two_letters
from customer;
##Returns the first 4 letters of each first name.

##right
select right(first_name, 2) as last_two_letters
from customer;
##Returns the last two letters of each first name.

## conditional statements : case - end
select first_name,
case
when active = 1 then 'active'
else 'inactive'
end as status
from customer;
##Checks whether the customer is active or inactive and displays the status.

##replace()
select first_name,
replace(first_name, 'a', '@') as new_name
from customer;
##Replaces every letter a with @ in the first name.

##where like
select *
from customer
where first_name like 'k%';
##Shows customers whose first name starts with k.

##regexp
select *
from customer
where email regexp 'org$';
##Shows customers whose email ends with org $ means "ends with".

##rand()
select rand();
##Returns a different random decimal number every time you run the query.

##mod()
select mod(15, 4) as remainder;
##Divides 15 by 4 and returns the remainder, which is 3.

##round()
select round(15.678, 2) as rounded_value;
##Rounds the number to 2 decimal places.

##datediff()
select datediff('2005-06-01', '2005-05-25') as total_days;
##Calculates the number of days between the two dates.

##Customers who paid in the last 24 hours
select *
from payment
where payment_date >= now() - interval 1 day;
##Shows payments made in the last 24 hours from the current time.

##concat() with date
select concat('payment date: ', date(payment_date)) as payment_info
from payment;
##Combines the text "payment date:" with the payment date into one column.
