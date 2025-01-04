--3. Query 1: Count and Percentage of Orders Purchased in Jan 2018 with 5 Review Score
--Write and execute a SQL query to count the number of orders purchased in January 2018 that have a review score of 5 and calculate the percentage of such orders.

WITH jan_2018_orders AS (
    SELECT o.order_id
    FROM olist_orders_dataset o
    JOIN olist_order_reviews_dataset r ON o.order_id = r.order_id
    WHERE o.order_purchase_timestamp BETWEEN '2018-01-01' AND '2018-01-31'
      AND r.review_score = 5
)
SELECT 
    COUNT(*) AS total_5_star_orders,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) 
                         FROM olist_orders_dataset 
                         WHERE order_purchase_timestamp BETWEEN '2018-01-01' AND '2018-01-31')) AS percentage_5_star_orders
FROM jan_2018_orders;


--4. Query 2: Customer Purchase Trend Year-on-Year
--Write and execute a SQL query to analyze the customer purchase trend year-on-year.

SELECT 
    strftime('%Y', order_purchase_timestamp) AS year,
    COUNT(order_id) AS total_orders
FROM olist_orders_dataset
GROUP BY year
ORDER BY year;


--5. Query 3: Average Order Values of Customers
--Write and execute a SQL query to calculate the average order values of customers.

SELECT 
    o.customer_id,
    AVG(oi.price + oi.freight_value) AS avg_order_value
FROM olist_orders_dataset o
JOIN olist_order_items_dataset oi ON o.order_id = oi.order_id
GROUP BY o.customer_id
ORDER BY avg_order_value DESC;


--6. Query 4: Top 5 Cities with Highest Revenue from 2016 to 2018
--Write and execute a SQL query to find the top 5 cities with the highest revenue from 2016 to 2018.

SELECT 
g.geolocation_city AS city,
SUM(oi.price + oi.freight_value) AS total_revenue
FROM olist_order_items_dataset oi
JOIN olist_orders_dataset o ON oi.order_id = o.order_id
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
JOIN olist_geolocation_dataset g ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix
WHERE strftime('%Y', o.order_purchase_timestamp) BETWEEN '2016' AND '2018'
GROUP BY city
ORDER BY total_revenue DESC
LIMIT 5;
