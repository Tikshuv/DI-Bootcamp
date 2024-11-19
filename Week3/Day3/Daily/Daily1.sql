-- Part I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

-- CREATE TABLE customer(
-- c_id SERIAL PRIMARY KEY,
-- first_name VARCHAR(25) NOT NULL,
-- last_name VARCHAR(25) NOT NULL
-- );

-- CREATE TABLE customer_profile(
-- custprof_id SERIAL PRIMARY KEY,
-- isLoggedIn BOOLEAN DEFAULT FALSE,
-- customer_id INT,
-- CONSTRAINT fk_cprof_cust_id FOREIGN KEY (customer_id) REFERENCES customer(c_id)
-- );

-- Insert those customers

-- John, Doe
-- Jerome, Lalu
-- Lea, Rive

-- INSERT INTO customer(first_name, last_name)
-- VALUES('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive');

-- Insert those customer profiles, use subqueries

-- John is loggedIn
-- Jerome is not logged in
-- INSERT INTO customer_profile(isLoggedIn, customer_id)
-- VALUES(TRUE, (SELECT c_id FROM customer WHERE first_name = 'John')),(False, (SELECT c_id FROM customer WHERE first_name = 'Jerome'));

-- Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers
-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
-- The number of customers that are not LoggedIn

-- SELECT c.first_name 
-- FROM customer_profile custp
-- INNER JOIN customer c
-- ON custp.customer_id = c.c_id
-- WHERE custp.isLoggedIn;

-- SELECT c.first_name, custp.isLoggedIn 
-- FROM customer c
-- LEFT JOIN customer_profile custp
-- ON c.c_id = custp.customer_id;

-- SELECT COUNT(*)
-- FROM customer_profile
-- WHERE isLoggedIn = FALSE

