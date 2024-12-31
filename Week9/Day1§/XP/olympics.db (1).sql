-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. Use a correlated subquery to achieve this.
SELECT 
    ce.medal_id,
    (
        SELECT AVG(gc.age)
        FROM games_competitor gc
        WHERE gc.id = ce.competitor_id
    ) AS average_age
FROM 
    competitor_event ce
WHERE EXISTS (
    SELECT 1
    FROM games_competitor gc
    WHERE gc.id = ce.competitor_id
)
GROUP BY 
    ce.medal_id;
    

-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.
SELECT 
    nr.region_name,
    COUNT(DISTINCT pr.person_id) AS unique_competitors
FROM 
    person_region pr
JOIN 
    noc_region nr ON pr.region_id = nr.id
WHERE 
    pr.person_id IN (
        SELECT gc.person_id
        FROM games_competitor gc
        WHERE gc.id IN (
            SELECT ce.competitor_id
            FROM competitor_event ce
            GROUP BY ce.competitor_id
            HAVING COUNT(DISTINCT ce.event_id) > 3
        )
    )
GROUP BY 
    nr.region_name
ORDER BY 
    unique_competitors DESC
LIMIT 5;


-- Task 3: Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.
CREATE TEMP TABLE competitor_medal_count AS
SELECT 
    ce.competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM 
    competitor_event ce
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    ce.competitor_id
HAVING 
    COUNT(ce.medal_id) > 2;

SELECT 
    gc.person_id,
    cm.total_medals
FROM 
    competitor_medal_count cm
JOIN 
    games_competitor gc ON cm.competitor_id = gc.id
ORDER BY 
    cm.total_medals ASC;

-- Task 4: Use a subquery within a DELETE statement to remove records of competitors who have not won any medals from a temporary table created for analysis.
DELETE FROM competitor_medal_count
WHERE competitor_id IN (
    SELECT ce.competitor_id
    FROM competitor_event ce
    WHERE ce.medal_id IS NULL
    GROUP BY ce.competitor_id
);



-- Task 1: Update the heights of competitors based on the average height of competitors from the same region. Use a correlated subquery within the UPDATE statement.

UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr1 ON p2.id = pr1.person_id
    JOIN person_region pr2 ON person.id = pr2.person_id
    WHERE pr1.region_id = pr2.region_id AND p2.height IS NOT NULL
)
WHERE height IS NULL;

-- Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.

CREATE TEMP TABLE competitors_multiple_events AS
SELECT 
    gc.person_id,
    gc.games_id,
    COUNT(DISTINCT ce.event_id) AS total_events
FROM 
    games_competitor gc
JOIN 
    competitor_event ce ON gc.id = ce.competitor_id
GROUP BY 
    gc.person_id, gc.games_id
HAVING 
    COUNT(DISTINCT ce.event_id) > 1;


-- Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. Use subqueries to calculate and compare averages.

SELECT 
    nr.region_name,
    AVG(region_medals.total_medals) AS avg_medals_per_competitor
FROM (
    SELECT 
        pr.region_id,
        COUNT(ce.medal_id) AS total_medals,
        COUNT(DISTINCT pr.person_id) AS total_competitors
    FROM 
        person_region pr
    JOIN 
        games_competitor gc ON pr.person_id = gc.person_id
    JOIN 
        competitor_event ce ON gc.id = ce.competitor_id
    WHERE 
        ce.medal_id IS NOT NULL
    GROUP BY 
        pr.region_id
) AS region_medals
JOIN noc_region nr ON region_medals.region_id = nr.id
GROUP BY 
    nr.region_name
HAVING 
    AVG(region_medals.total_medals) > (
        SELECT AVG(total_medals_per_competitor)
        FROM (
            SELECT 
                COUNT(ce.medal_id) * 1.0 / COUNT(DISTINCT gc.person_id) AS total_medals_per_competitor
            FROM 
                competitor_event ce
            JOIN games_competitor gc ON ce.competitor_id = gc.id
            WHERE ce.medal_id IS NOT NULL
        ) AS overall_avg
    );


-- Task 4: Create a temporary table to track competitors’ participation across different seasons and identify those who have participated in both Summer and Winter games

CREATE TEMP TABLE competitors_seasons AS
SELECT 
    gc.person_id,
    COUNT(DISTINCT g.season) AS season_count
FROM 
    games_competitor gc
JOIN 
    games g ON gc.games_id = g.id
WHERE 
    g.season IN ('Summer', 'Winter')
GROUP BY 
    gc.person_id
HAVING 
    COUNT(DISTINCT g.season) = 2;