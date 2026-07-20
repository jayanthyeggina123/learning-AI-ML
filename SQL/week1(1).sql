## 1. Identify if there are duplicates in Customer table. Don't use customer id to check the duplicates
select first_name,
count(*) as total
from customer
group by first_name
having count(*) > 1;
## it counts how many times each first name appears in the customer table.
## It only shows first names that appear more than once.

select first_name,
last_name,
email,
count(*) as total
from customer
group by first_name, last_name, email
having count(*) > 1;
## No duplicate records were found in the customer table based on first_name, last_name, and email.

## 2. Number of times letter 'a' is repeated in film descriptions
select sum(length(description) - length(replace(description, 'a', ''))) as total_a
from film;
## it counts how many times the letter 'a' appears in all film descriptions.
## It uses replace() and length() to calculate the total count.

## 3. Number of times each vowel is repeated in film descriptions
select
sum(length(description)-length(replace(description,'a',''))) as a_count,
sum(length(description)-length(replace(description,'e',''))) as e_count,
sum(length(description)-length(replace(description,'i',''))) as i_count,
sum(length(description)-length(replace(description,'o',''))) as o_count,
sum(length(description)-length(replace(description,'u',''))) as u_count
from film;
##it counts how many times each vowel (a, e, i, o, u) appears in all film descriptions.
## It uses length() and replace() to calculate the total count for each vowel.

## Display the payments made by each customer 1. Month wise 2. Year wise 3. Week wise
select customer_id,
month(payment_date) as month,
sum(amount) as total_payment
from payment
group by customer_id, month(payment_date);
## it shows the total payment made by each customer every month. groups the payments using customer ID and month.
select customer_id,
year(payment_date) as year,
sum(amount) as total_payment
from payment
group by customer_id, year(payment_date);
## it shows the total payment made by each customer every year. groups the payments using customer ID and year.
select customer_id,
week(payment_date) as week,
sum(amount) as total_payment
from payment
group by customer_id, week(payment_date);
## it shows the total payment made by each customer every week. groups the payments using customer ID and week.

## 5. Check if any given year is a leap year or not. You need not consider any table from sakila database. Write within the select query with hardcoded date
select
case
when mod(2024,400)=0 or (mod(2024,4)=0 and mod(2024,100)!=0)
then 'leap year'
else 'not a leap year'
end as result; 
## divisible by 400, or divisible by 4 but not by 100.
## 2024 is a leap year 

##6. Display number of days remaining in the current year from today. 
select datediff(
concat(year(curdate()),'-12-31'),
curdate()
) as remaining_days;
## datediff() - Calculates the difference between two dates.
## it calculates the number of days remaining until the last day of the current year.
## It compares today's date with December 31 of the current year.

## 7. Display quarter number(Q1,Q2,Q3,Q4) for the payment dates from payment table.
select payment_date,
concat('q', quarter(payment_date)) as quarter
from payment;
## concat('q', quarter(payment_date))  - Joins the letter Q with the quarter number.
## it shows the payment date and the quarter in which the payment was made.
## It displays the quarter as Q1, Q2, Q3, or Q4.
