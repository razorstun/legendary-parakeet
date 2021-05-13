CASE: 
-   select customer_id,
    case 
            when customer_id <= 100 then 'Premium'
            when customer_id between 100 and 200 then 'Plus'
            else 'Normal'
    end
    as customer_class
    from customer

CASE expression - when we are just checking for equality
-   select customer_id,
    case customer_id
        when 2 then 'Winner'
        when 5 then 'Second Place'
        else 'Normal'
    end as raffle_results
    from customer

-   select 
    sum(case rental_rate
        when 0.99 then 1
        else 0
    end) as bargains,
    sum(
        case rental_rate
        when 2.99 then 1
        else 0
    end
    ) as regular,
    sum(
        case rental_rate
        when 4.99 then 1
        else 0
    end
    ) as premium
    from film

Challenges
-   select
    sum(
        case rating
            when 'R' then 1
        else 0
        end
    ) as r,
    sum(
        case rating
            when 'PG' then 1
        else 0
        end
    ) as pg,
    sum(
        case rating
            when 'PG-13' then 1
        else 0
        end
    ) as pg13
    from film

Coalesce - it accepts unlimited number of arguments. It returns the first argument that is not null, the coalwsce function will return null
-   select item,(price - coalesce(discount,0))
    as final from table

CAST - allow us to convert one datatype into another
-   select cast('5' as integer)
-   select '5'::integer - postgresql 
-   select char_length(cast(inventory_id as varchar)) from rental 

NULLIF - function takes 2 inputs and return null if both are equal, otherwise returns first value
-   select(
        sum(case when department = 'A' then 1 else 0 END)/
        nullif(sum(case when department = 'B' then 1 else 0 END),0)
    ) as department_ratio
    from depts

VIEWS - a database object that is of a stored query. can be accessed as a virtual table in postgresql
-   create view view_name as
    query
-   create or replace view view_name as
    new_query
-   drop view if exists view_name
-   alter view view_name rename to new_view_name

import and export
-   allow us to import/export from/to csv files - plsql feature