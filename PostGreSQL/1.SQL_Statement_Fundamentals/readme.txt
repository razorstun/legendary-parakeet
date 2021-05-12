Select
- allow us to retrive data from tables
- select * from table - retrives all cloumns for database
- select column1, column2, columnn from table - retrive particular column from table

Select Distinct
- get only the unique value from the column
- Select Distinct coulumn from table;
- select distinct (release_year) from film;

Select Count
- select count (Distinct rating) from film;
- select count * from film;

Select and Where statements
- Comaparison operators - = < > >= <= <>/!=
- Logical operators - ANS OR NOT
-   select * from customer
    where first_name = 'Jared'
-   select * from film
    where rental_rate > 4 AND replacement_cost >= 19.99
-   select count(title) from film
    where rental_rate > 4 AND replacement_cost >= 19.99

Order by
- you can sort rows based on a column value, in either ASC/DESC Order ASC is default
-   select store_id, first_name, last_name from customer
    order by store_id DESC, first_name ASC

Limit
- allow us to limit the number of rows returned for a query
- LIMIT goes at the very end of a query
-   select * from payment
    where amount != 0.00
    order by payment_date DESC
    limit 5
-   select customer_id from payment
    where amount != 0.00
    order by payment_date
    limit 10
-   select count(title) from film
    where length <= 50

Between
- match value between a range of values
- between can also be used with dates 'yyyy-mm-dd'
-   select * from payment
    where payment_date between '2007-02-01' AND '2007-02-15'

in
-   select count(amount) from payment
    where amount not in (0.99,1.98,1.99)

LIKE and ILIKE(its less case sensitive)
- pattern matching with string data
- % matches any sequence of characters
- _ matches any single character
-   select * from customer
    where first_name not like 'Sa%'


