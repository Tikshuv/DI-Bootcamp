-- Create the employees table
drop table employees;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);



INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');
    --Identify and handle any missing value.
SELECT * 
FROM employees
WHERE employee_id IS NULL 
OR employee_name IS NULL 
OR salary IS NULL 
OR hire_date IS NULL 
OR department IS NULL;

UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL;
    --Check for and eliminate any duplicate rows in the dataset.
    
SELECT employee_id, employee_name, salary, hire_date, department, COUNT(*)
FROM employees
GROUP BY employee_id, employee_name, salary, hire_date, department
HAVING COUNT(*) > 1;
-- no dups found

    --Correct any structural issues, such as inconsistent naming conventions or formatting errors.
UPDATE employees
SET employee_name = UPPER(SUBSTR(employee_name, 1, 1)) || LOWER(SUBSTR(employee_name, 2));

 
    --Ensure all columns have appropriate data types (e.g. the hire_date column).
--ALTER TABLE employees 
--ALTER COLUMN hire_date TYPE DATE USING TO_DATE(hire_date, 'YYYY-MM-DD');
CREATE TABLE employees_new (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE,
    department VARCHAR(50)
);

INSERT INTO employees_new (employee_id, employee_name, salary, hire_date, department)
SELECT 
employee_id,
employee_name,
salary,
DATE(hire_date),
department
FROM employees;


DROP TABLE employees;
ALTER TABLE employees_new RENAME TO employees;




   -- Detect and address any outliers that may skew the analysis.

WITH Percentiles AS (
SELECT salary,
PERCENT_RANK() OVER (ORDER BY salary) AS percentile
FROM employees
),
Quartiles AS (
SELECT 
MAX(CASE WHEN percentile <= 0.25 THEN salary END) AS Q1,
MAX(CASE WHEN percentile <= 0.75 THEN salary END) AS Q3
FROM Percentiles
)
SELECT *,
(Q3 - Q1) AS IQR,
(Q1 - 1.5 * (Q3 - Q1)) AS lower_bound,
(Q3 + 1.5 * (Q3 - Q1)) AS upper_bound
FROM Quartiles;


WITH Quartiles AS (
SELECT 
MAX(CASE WHEN percentile <= 0.25 THEN salary END) AS Q1,
MAX(CASE WHEN percentile <= 0.75 THEN salary END) AS Q3
FROM (SELECT salary, PERCENT_RANK() OVER (ORDER BY salary) AS percentile FROM employees)
),
Boundaries AS (
SELECT 
Q1, 
Q3, 
(Q3 - Q1) AS IQR,
(Q1 - 1.5 * (Q3 - Q1)) AS lower_bound,
(Q3 + 1.5 * (Q3 - Q1)) AS upper_bound
FROM Quartiles
)
SELECT e.*
FROM employees e
JOIN Boundaries b
ON e.salary < b.lower_bound OR e.salary > b.upper_bound;


WITH Quartiles AS (
    SELECT 
        MAX(CASE WHEN percentile <= 0.25 THEN salary END) AS Q1,
        MAX(CASE WHEN percentile <= 0.75 THEN salary END) AS Q3
    FROM (SELECT salary, PERCENT_RANK() OVER (ORDER BY salary) AS percentile FROM employees)
),
Boundaries AS (
SELECT 
Q1, 
Q3, 
(Q3 - Q1) AS IQR,
(Q1 - 1.5 * (Q3 - Q1)) AS lower_bound,
(Q3 + 1.5 * (Q3 - Q1)) AS upper_bound
FROM Quartiles
)
UPDATE employees
SET salary = CASE
WHEN salary < (SELECT lower_bound FROM Boundaries) THEN (SELECT lower_bound FROM Boundaries)
WHEN salary > (SELECT upper_bound FROM Boundaries) THEN (SELECT upper_bound FROM Boundaries)
ELSE salary
END;

select * from employees

   -- Standardize and normalize data where applicable to ensure consistency.
   
SELECT employee_id, 
employee_name,
(salary - (SELECT MIN(salary) FROM employees)) /
((SELECT MAX(salary) FROM employees) - (SELECT MIN(salary) FROM employees)) AS normalized_salary,
hire_date,
department
FROM employees;