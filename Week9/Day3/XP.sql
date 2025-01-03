--Exercise 1: Building a Comprehensive Dataset for Employee Analysis

  --  Create a temporary table that join all tables and create a new one using LEFT JOIN.
drop table df_employee;
CREATE TEMPORARY TABLE emp_dataset AS
SELECT 
salaries.employee_id,
salaries.employee_name,
salaries.date,
salaries.salary,
functions.function AS func_name,
functions.function_group,
employees.[GEN(M_F)] AS gender,
employees.age,
companies.company_name,
companies.company_city,
companies.company_state,
companies.company_type,
companies.const_site_category
FROM salaries
LEFT JOIN functions ON salaries.func_code = functions.function_code
LEFT JOIN employees ON salaries.employee_id = employees.employee_code_emp AND salaries.comp_code = employees.comp_code_emp
LEFT JOIN companies ON salaries.comp_name = companies.company_name;
   -- Create an unique identifier code between the columns â€˜employee_idâ€™ and â€˜dateâ€™ and call it â€˜idâ€™.
   -- Convert the column â€˜dateâ€™ to DATE type because it was previously configured as TIMESTAMP.
  ---  Transform this new table into a dataset â€œdf_employeeâ€ for analysis.
--You should get a new df-employee table with the following columns : id, month_year, employee_id, employee_name, gender, age, salary,
--function_group, company_name, company_city, company_state, company_type, and const_site_category.
CREATE TABLE df_employee AS
SELECT 
employee_id || '_' || CAST(date AS TEXT) AS id,
DATE(date) AS month_year,
employee_id,
employee_name,
gender,
age,
salary,
function_group,
company_name,
company_city,
company_state,
company_type,
const_site_category
FROM emp_dataset;

drop table emp_dataset;

--Exercise 2: Cleaning Data for Consistency and Quality

--1. run the following SQLite request and observe your new table.

SELECT * FROM df_employee;
SELECT * FROM salaries;



--2. Remove all unwanted spaces from all text columns using TRIM

--Hint :

--UPDATE df_employee
--SET
--id = TRIM(id),
--...
--...;

UPDATE df_employee
SET
id = TRIM(id),
employee_name = TRIM(employee_name),
gender = TRIM(gender),
salary = TRIM(salary),
function_group = TRIM(function_group),
company_name = TRIM(company_name),
company_city = TRIM(company_city),
company_state = TRIM(company_state),
company_type = TRIM(company_type),
const_site_category = TRIM(const_site_category);


--3. Check for NULL values and empty values.


SELECT *
FROM df_employee
WHERE id IS NULL
-- OR month_year IS NULL
OR employee_id IS NULL
OR employee_name IS NULL
OR salary IS NULL
OR gender IS NULL
OR function_group is NULL


--4. Delete rows of the detected missing values.

--Hint :

--DELETE FROM df_employee
--WHERE salary = ' '
--;


DELETE FROM df_employee
-- WHERE month_year Is NULL
WHERE company_name Is  NULL
OR company_city IS NULL
OR company_state IS NULL
OR company_type IS NULL
OR const_site_category IS NULL;









.
--ðŸŒŸ Exercise 3 : Calculating Current Employee Counts by Company

   -- How many employees do the companies have today?
 --   Group them by company

SELECT 
company_name,
COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY company_name;


--ðŸŒŸ Exercise 4 : Analyzing Employee Distribution by City and Over Time

  --  What is the total number of employees each city? Add a percentage column
  
WITH city_counts AS (
SELECT 
company_city,
COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY company_city
)
SELECT 
company_city,
employee_count,
ROUND(100.0 * employee_count / (SELECT SUM(employee_count) FROM city_counts), 2) AS percentage
FROM city_counts;

  --  What is the total number of employees each month?
  
SELECT 
month_year,
COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year;

 --   What is the average number of employees each month?

SELECT 
    AVG(employee_count) AS average_employees
FROM (
    SELECT 
        month_year,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
);



--ðŸŒŸ= Exercise 5 : Analyzing Employment Trends and Salary Metrics

 --   What is the minimum and maximum number of employees throughout all the months? In which months were they?
 
SELECT 
MIN(employee_count) AS min_employees,
MAX(employee_count) AS max_employees,
month_year
FROM (
SELECT 
month_year,
COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year
);


  --  What is the monthly average number of employees by function group?
  
SELECT 
function_group,
AVG(employee_count) AS avg_employees
FROM (
SELECT 
function_group,
month_year,
COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY function_group, month_year
)
GROUP BY function_group;

  --  What is the annual average salary?
  
SELECT 
AVG(CAST(salary AS REAL)) AS annual_avg_salary
FROM df_employee;


