GROUP BY and AGGEREGATE FUNCTIONS
- allow us to  ggregate data and apply functions to better understaand how data is distributed per category
- aggregate functions - avg(), count(), max(), min(), sum(), round()
- aggregate function call happens on;y in the select clause or having clause
-   select max(replacement_cost) from film
-   select round(avg(replacement_cost)) from film
-   select sum(replacement_cost) from film
-   select customer_id, sum(amount) from payment
    group by customer_id
    order by sum(amount)
-   select customer_id, count(amount) from payment
    group by customer_id
    order by count(amount)
-   select date(payment_date), sum(amount) from payment
    group by date(payment_date)
    order by sum(amount)
-   select staff_id, count(payment_id) from payment
    group by staff_id
    order by count(payment_id)
-   select rating, avg(replacement_cost) from film
    group by rating
-   select customer_id, sum(amount) from payment
    group by customer_id
    order by sum(amount) DESC
    limit 5

- Having clause alowws us to filter after an aggregation has taken place
-   select customer_id, count(payment_id) from payment
    group by customer_id
    having count(payment_id) >= 40
-   select customer_id, sum(amount) from payment
    where staff_id = 2
    group by customer_id
    having sum(amount) > 100 

ASSESSMENT

-   select customer_id, sum(amount) from payment
    where staff_id = 2
    group by customer_id
    having sum(amount) >= 110
-   select count(*) from film
    where title like 'J%'
-   select first_name, last_name, max(customer_id) from customer
    where first_name like 'E%' and address_id < 500
    group by first_name, last_name
    order by max(customer_id) DESC
    limit 1