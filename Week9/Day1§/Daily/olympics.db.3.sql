-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics.
-- Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.
CREATE TEMP TABLE competitors_summer_winter_medals AS
SELECT 
    gc.person_id,
    SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM 
    games_competitor gc
JOIN 
    competitor_event ce ON gc.id = ce.competitor_id
JOIN 
    games g ON gc.games_id = g.id
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    gc.person_id
HAVING 
    summer_medals > 0 AND winter_medals > 0;

SELECT * FROM competitors_summer_winter_medals;


-- Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery 
-- to identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.

CREATE TEMP TABLE competitors_two_sports AS
SELECT 
    gc.person_id,
    COUNT(DISTINCT e.sport_id) AS sport_count,
    COUNT(ce.medal_id) AS total_medals
FROM 
    games_competitor gc
JOIN 
    competitor_event ce ON gc.id = ce.competitor_id
JOIN 
    event e ON ce.event_id = e.id
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    gc.person_id
HAVING 
    sport_count = 2;
SELECT 
    person_id,
    total_medals
FROM 
    competitors_two_sports
ORDER BY 
    total_medals DESC
LIMIT 3;


-- Exercise 2: Region and Competitor Performance
-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. 
-- Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.
WITH competitor_event_medals AS (
    SELECT 
        ce.competitor_id,
        ce.event_id,
        COUNT(ce.medal_id) AS medal_count
    FROM 
        competitor_event ce
    WHERE 
        ce.medal_id IS NOT NULL
    GROUP BY 
        ce.competitor_id, ce.event_id
),
competitor_max_medals AS (
    SELECT 
        competitor_id,
        MAX(medal_count) AS max_medals
    FROM 
        competitor_event_medals
    GROUP BY 
        competitor_id
),
competitor_top_event AS (
    SELECT 
        cem.competitor_id,
        cem.event_id,
        cem.medal_count
    FROM 
        competitor_event_medals cem
    JOIN 
        competitor_max_medals cmm ON cem.competitor_id = cmm.competitor_id
    WHERE 
        cem.medal_count = cmm.max_medals
)
SELECT 
    nr.region_name,
    SUM(cte.medal_count) AS total_medals
FROM 
    competitor_top_event cte
JOIN 
    games_competitor gc ON cte.competitor_id = gc.id
JOIN 
    person_region pr ON gc.person_id = pr.person_id
JOIN 
    noc_region nr ON pr.region_id = nr.id
GROUP BY 
    nr.region_name
ORDER BY 
    total_medals DESC
LIMIT 5;

-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals.
-- Retrieve and display the contents of this table, including their full names and the number of games they participated in.
CREATE TEMP TABLE competitors_no_medals AS
SELECT 
    p.full_name,
    COUNT(DISTINCT gc.games_id) AS games_participated
FROM 
    games_competitor gc
JOIN 
    person p ON gc.person_id = p.id
LEFT JOIN 
    competitor_event ce ON gc.id = ce.competitor_id
WHERE 
    ce.medal_id IS NULL
GROUP BY 
    p.id, p.full_name
HAVING 
    COUNT(DISTINCT gc.games_id) > 3;
SELECT * FROM competitors_no_medals;
