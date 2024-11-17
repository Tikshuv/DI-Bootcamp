-- DROP TABLE IF EXISTS actors
-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- );

-- SELECT * FROM actors;

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt', 'Damon', '08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('Marian', 'Boogie', '10/25/1935', 25);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('GERINI', 'Sarini', '02/11/1944', 4);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('Peray', 'Kona', '03/17/1917', 3), ('Cosy', 'Monte', '06/29/1954', 7);


-- SELECT * FROM actors

------------------------------------------------------------------------------
-- Instructions
-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?


-- SELECT COUNT(last_name)
-- FROM actors;


-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('', '', '06/10/1930', 5)

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES() -- VALUES(, , ,); -- Error

-- INSERT INTO actors(firs_name, last_name)
-- VALUES('Joe', 'Po'); -- Error too

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('', '', '', ''); -- Error for date type

-- SELECT * FROM actors