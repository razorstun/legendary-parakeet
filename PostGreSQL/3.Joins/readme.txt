Joins
- allow us to combine information from multiple tables
- AS - allow us to create alias
    - select column_name as alias_name from tables
- INNER JOIN - will result with the set of records thaat match in both tables
    -   select customer.email, payment_id 
        from customer
        inner join payment
        on customer.customer_id = payment.customer_id
- OUTER JOIN - they allow us to specify how to deal with values present in one of the tables being joined
    - full outer join
        -   select count(*) from customer
            full outer join payment
            on customer.customer_id = payment.customer_id
        - opposite of inner join using outer join
        -   select count(*) from customer
            full outer join payment
            on customer.customer_id = payment.customer_id
            where customer.customer_id is null or payment.payment_id is null
    - left outer join
        -   select film.film_id, film.title, inventory_id from film
            left join inventory
            on inventory.film_id = film.film_id
    - right outer join
        -   select inventory.film_id, title, inventory_id from inventory
            left join film
            on film.film_id = inventory.film_id
    - unions - used to combine the result-set of two or more select statements
        - stack/concatenate two select statements
        -   select * from table1
            unions
            select * from table2
            orderby column_name

- Challenges
-   select email, district from customer
    inner join address
    on customer.address_id = address.address_id
    where district = 'California'
    order by email
-   select starttime, name from cd.bookings
    inner join cd.facilities
    on bookings.facid = facilities.facid
    where name like 'Tennis Court%' and starttime >= '2012-09-21' and starttime < '2012-09-22'
    order by starttime
    
