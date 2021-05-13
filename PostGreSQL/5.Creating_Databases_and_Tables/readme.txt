Data types
- Boolean - True, False
- Charcter - char, varchar, text
- Numeric - integer, floating-point
- Temporal - date, time, timestamp, interval
- UUID - algorithmic unique code
- Array
- JSON
- Hstore key-vale pair
- network address and geometric data

Primary and Foreign key
- PK is a column or group of columns used to identify a row uniquely in a table
- FK is a field or group of fields in a table that uniquely identifies a row in another table
- A foreign key is defined in a table that references to the PK of the other table

Constraints
- Constraints are the rules enforced on data column on tables
- these prevent from invalid data to be entered into the database
- Column/Table Constraints
    - NOT null
    - unique
    - primary key
    - foreign key
    - check
    - exclusion
    - check - also table Constraints
    - references - TC
    - unique - TC
    - primary key - TC

Create Table
-   create table table_name(
    column_name type column_constraint,
    table_constraint table_constraint
    ) inherits existing_table_name;
- serial data type - special kind of database object that generates a sequence of integers
-   create table job(
        job_id serial PRIMARY KEY,
        username varchar(50) UNIQUE NOT NULL,
        password varchar(50) not null,
        email varchar(250)  unique not null,
        created_on timestamp not null,
        last_login timestamp
    )
-   create table job(
        job_id serial PRIMARY KEY,
        job_name varchar(200) unique not null
    )
-   create table account_job(
        user_id integer references account(user_id) ,
        job_id integer references job(job_id),
        hire_date timestamp
    )

INSERT
-   insert into account(
	    username,password,email,created_on
    )
    values (
	    'Sachin','password','shaggi199712@gmail.com',current_timestamp
    )

-   insert into job(
	    job_name
    )
    values (
	    'Devops Engineer'
    )
-   insert into account_job(
	    user_id, job_id, hire_date
    )
    values(
	    1,1,current_timestamp
    )

UPDATE
-   update account
    set last_login = current_timestamp
-   update account
    set last_login = created_on
-   update account_job
    set hire_date = account.created_on
    from account
    where account_job.user_id = account.user_id
-   update account
    set last_login = current_timestamp
    returning email, created_on,last_login

DELETE
-   delete from job
    where job_name = 'Cowboy'
    returning job_id, job_name

ALTER
-   alter table informatiob
    rename to information
-   alter table information
    alter column person drop not null
-   alter table information
    alter column person set not null

drop
-   alter table information
    drop column person
-   alter table information
    drop column if exists person

check
-   create table employees(
	emp_id serial primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	birthday date check (birthday > '1900-01-01'),
	hire_date date check (hire_date > birthday)
)