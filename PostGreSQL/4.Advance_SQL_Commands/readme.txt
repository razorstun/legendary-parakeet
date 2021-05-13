POSTGRESQL docs: https://www.postgresql.org/docs/current/

- SELECT NOW() - gives current timestamp
- SELECT TIMEOFDAY() - same as now() but more readable
- SELECT CURRENT_TIME, SELECT CURRENT_DATE
- extract() allow us to extract or obtain a sub-component from a timestamp
- age() - calculates and returns the current age
- to_char() - general function to convert data types to text - to_char(date_col,'mm-dd-yy')

Challenges
-   select distinct(to_char(payment_date,'MONTH')) from payment
-   select count(*) from payment
    where extract(dow from payment_date) = 1

Mathematical functions
- select round((rental_rate/replacement_cost)*100, 2) as percent_cost from film

String functions and operators
- select first_name || ' ' ||last_name from customer as full_name

Subquery adn exist()
- it allow us to query on the result of another query
-   select title, rental_rate from film
    where rental_rate > (select AVG(rental_rate) from film)

Challenges
-   select name, membercost from cd.facilities
    where membercost between 1 and (monthlymaintenance/50)
-   select * from cd.facilities
    where name like '%Tennis%'
-   select * from cd.facilities
    where facid in (1,5)
-   select facid, sum(slots) as total_slots from cd.bookings
    where starttime >= '2012-09-01' and starttime <= '2012-10-01'
    group by facid
    order by facid 
-   select facid, sum(slots) as total_slots from cd.bookings
    group by facid
    having sum(slots) > 1000
    order by facid
-   select starttime from cd.bookings
    inner join cd.members 
    on cd.members.memid = cd.bookings.memid
    where firstname = 'David' and surname = 'Farrell' 
