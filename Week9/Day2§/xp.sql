-- XP

-- Task 1: Rank Movies by Popularity within Each Genre

--Use the RANK() function to rank movies by their popularity within each genre. Display the genre name, movie title, and their rank based on popularity.

SELECT 
    g.genre_name,
    m.title,
    RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
FROM 
    movie_genres mg
JOIN 
    genre g ON mg.genre_id = g.genre_id
JOIN 
    movie m ON mg.movie_id = m.movie_id;


--Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

--Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.

SELECT 
    pc.company_name,
    m.title,
    m.revenue,
    NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS revenue_quartile
FROM 
    movie_company mc
JOIN 
    production_company pc ON mc.company_id = pc.company_id
JOIN 
    movie m ON mc.movie_id = m.movie_id;



--Task 3: Calculate the Running Total of Movie Budgets for Each Genre

--Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets within each genre. Display the genre name, movie title, budget, and running total budget.

SELECT 
    g.genre_name,
    m.title,
    m.budget,
    SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.title ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total_budget
FROM 
    movie_genres mg
JOIN 
    genre g ON mg.genre_id = g.genre_id
JOIN 
    movie m ON mg.movie_id = m.movie_id;


--Task 4: Identify the Most Recent Movie for Each Genre

--Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. Display the genre name, movie title, and release date.

SELECT 
    g.genre_name,
    FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_movie,
    FIRST_VALUE(m.release_date) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS release_date
FROM 
    movie_genres mg
JOIN 
    genre g ON mg.genre_id = g.genre_id
JOIN 
    movie m ON mg.movie_id = m.movie_id;


--🌟 Exercise 2: Cast and Crew Performance Analysis


--Task 1: Rank Actors by Their Appearance in Movies

--Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. Display the actor’s name and their rank.

SELECT 
    p.person_name AS actor_name,
    DENSE_RANK() OVER (ORDER BY COUNT(mc.movie_id) DESC) AS appearance_rank
FROM 
    movie_cast mc
JOIN 
    person p ON mc.person_id = p.person_id
GROUP BY 
    p.person_name;


--Task 2: Identify the Top Director by Average Movie Rating

--Use a CTE and the RANK() function to find the director with the highest average movie rating. Display the director’s name and their average rating.

WITH DirectorRatings AS (
    SELECT 
        p.person_name AS director_name,
        AVG(m.vote_average) AS avg_rating
    FROM 
        movie_crew mc
    JOIN 
        person p ON mc.person_id = p.person_id
    JOIN 
        movie m ON mc.movie_id = m.movie_id
    WHERE 
        mc.job = 'Director'
    GROUP BY 
        p.person_name
)
SELECT 
    director_name,
    avg_rating
FROM 
    DirectorRatings
ORDER BY 
    avg_rating DESC
LIMIT 1;



--Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

--Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. Display the actor’s name and the cumulative revenue.

SELECT 
    p.person_name AS actor_name,
    SUM(m.revenue) AS cumulative_revenue
FROM 
    movie_cast mc
JOIN 
    person p ON mc.person_id = p.person_id
JOIN 
    movie m ON mc.movie_id = m.movie_id
GROUP BY 
    p.person_name
ORDER BY 
    cumulative_revenue DESC;


--Task 4: Identify the Director Whose Movies Have the Highest Total Budget

--Use a CTE and a window function to find the director whose movies have the highest total budget. Display the director’s name and the total budget.

WITH DirectorBudgets AS (
    SELECT 
        p.person_name AS director_name,
        SUM(m.budget) AS total_budget
    FROM 
        movie_crew mc
    JOIN 
        person p ON mc.person_id = p.person_id
    JOIN 
        movie m ON mc.movie_id = m.movie_id
    WHERE 
        mc.job = 'Director'
    GROUP BY 
        p.person_name
)
SELECT 
    director_name,
    total_budget
FROM 
    DirectorBudgets
ORDER BY 
    total_budget DESC
LIMIT 1;