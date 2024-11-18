-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- );

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');

-- SELECT * FROM FirstTab;

-- CREATE TABLE SecondTab (
--     id integer 
-- );

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL);


-- SELECT * FROM SecondTab;

-------------------------------------------------------------------------
-- Questions
-- Q1. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
-- 	   
---- Returns 0 cause of NULL in returning set, leading to postgress not being able to compare values 
--
-- Q2. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- Returns 2 for 6 and 7 and I guess ignores NULL cause of issues with comparisons with NULL values

-- Q3. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- Same as Q1 NULL in NOT IN() leads to issues with comparing

-- Q4. What will be the OUTPUT of the following statement?

    -- SELECT COUNT(*) 
    -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

	-- Same as Q2 since NOT IN() returns only 5 in set, 6 and 7 pass while not counting NULL
-- SELECT * FROM FirstTab WHERE id != NULL -- therefore returns nothing 
-- SELECT * FROM FirstTab WHERE id != 5 -- returns 6 and 7, since 5 doesn't pass and NULL can't be compared
