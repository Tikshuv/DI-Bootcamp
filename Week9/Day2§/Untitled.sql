-- DAILY

--Task 1: Calculate the Average Budget Growth Rate for Each Production Company
--Calculate the average budget growth rate for each production company across all movies they have produced. Use window functions to determine the budget growth rate and then calculate the average growth rate.

WITH BudgetGrowth AS (
    SELECT 
        pc.company_name,
        m.title,
        m.budget,
        LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) AS previous_budget,
        CASE 
            WHEN LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) IS NOT NULL 
                 AND LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date) > 0 
            THEN (m.budget - LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date)) 
                 / LAG(m.budget) OVER (PARTITION BY pc.company_name ORDER BY m.release_date)
            ELSE NULL
        END AS budget_growth_rate
    FROM 
        movie_company mc
    JOIN 
        production_company pc ON mc.company_id = pc.company_id
    JOIN 
        movie m ON mc.movie_id = m.movie_id
)
SELECT 
    company_name,
    AVG(budget_growth_rate) AS avg_budget_growth_rate
FROM 
    BudgetGrowth
WHERE 
    budget_growth_rate IS NOT NULL
GROUP BY 
    company_name
ORDER BY 
    avg_budget_growth_rate DESC;


--🌟 Task 2: Determine the Most Consistently High-Rated Actor
--Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.

WITH MovieAverageRating AS (
    SELECT 
        AVG(vote_average) AS overall_avg_rating
    FROM 
        movie
),
ActorHighRatedMovies AS (
    SELECT 
        p.person_name AS actor_name,
        COUNT(*) AS high_rated_movie_count
    FROM 
        movie_cast mc
    JOIN 
        person p ON mc.person_id = p.person_id
    JOIN 
        movie m ON mc.movie_id = m.movie_id,
        MovieAverageRating mar
    WHERE 
        m.vote_average > mar.overall_avg_rating
    GROUP BY 
        p.person_name
)
SELECT 
    actor_name,
    high_rated_movie_count
FROM 
    ActorHighRatedMovies
ORDER BY 
    high_rated_movie_count DESC
LIMIT 1;


--🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
--Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre. Use window functions with the ROWS frame specification to achieve this.

SELECT 
    g.genre_name,
    m.title,
    m.revenue,
    AVG(m.revenue) OVER (
        PARTITION BY g.genre_name 
        ORDER BY m.release_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM 
    movie_genres mg
JOIN 
    genre g ON mg.genre_id = g.genre_id
JOIN 
    movie m ON mg.movie_id = m.movie_id
WHERE 
    m.revenue IS NOT NULL
ORDER BY 
    g.genre_name, m.release_date;


--🌟 Task 4: Identify the Highest-Grossing Movie Series
--Identify the movie series (based on shared keywords) with the highest total revenue. Use window functions and CTEs to group movies by their series and calculate the total revenue.

WITH SeriesRevenue AS (
    SELECT 
        k.keyword_name AS series_name,
        SUM(m.revenue) AS total_revenue
    FROM 
        movie_keywords mk
    JOIN 
        keyword k ON mk.keyword_id = k.keyword_id
    JOIN 
        movie m ON mk.movie_id = m.movie_id
    WHERE 
        k.keyword_name ILIKE '%series%'
    GROUP BY 
        k.keyword_name
)
SELECT 
    series_name,
    total_revenue
FROM 
    SeriesRevenue
ORDER BY 
    total_revenue DESC
LIMIT 1;
