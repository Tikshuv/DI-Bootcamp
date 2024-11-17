-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt', 'Damon', '08/10/1970', 5)

-- SELECT * FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- SELECT * FROM actors

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('Marian', 'Boogie', '10/25/1935', 25);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('GERINI', 'Sarini', '02/11/1944', 4);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('Peray', 'Kona', '03/17/1917', 3), ('Cosy', 'Monte', '06/29/1954', 7);


-- SELECT * FROM actors

-- SELECT 
-- 	first_name
-- FROM
-- 	actors;

-- SELECT
-- 	first_name,
-- 	last_name,
-- 	age
-- FROM
-- 	actors;

-- SELECT first_name FROM actors WHERE first_name = 'Matt'


-- SELECT first_name, last_name, number_oscars FROM actors WHERE number_oscars > 3
-- ORDER BY number_oscars DESC;


-- UPDATE actors
-- SET first_name = 'Angelina',
-- 	last_name = 'Jobilie'
-- WHERE
-- 	first_name = 'Matt';

-- SELECT * FROM actors


-- DELETE FROM actors
-- WHERE first_name = 'Angelina';

-- SELECT * FROM actors


-- ALTER TABLE actors RENAME COLUMN number_oscars TO oscars

SELECT * FROM actors
