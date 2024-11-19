-- Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- UPDATE film
-- SET language_id = 3
-- WHERE film_id BETWEEN 30 AND 150;
-- SELECT * FROM film WHERE film_id BETWEEN 30 AND 150;

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

-- FK's only an address_id. We insert this field via subquery

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- DROP TABLE customer_review
-- Easy step since customer_review's only a child table and isn't referenced anywhere else

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- SELECT * FROM rental WHERE return_date IS NULL;

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet
-- SELECT film.title, film.rental_rate
-- FROM film
-- INNER JOIN inventory
-- ON film.film_id = inventory.film_id
-- INNER JOIN rental
-- ON rental.inventory_id = inventory.inventory_id
-- WHERE rental.return_date IS NULL ORDER BY film.rental_rate DESC LIMIT 30


-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- SELECT f.title, f.description, a.first_name, a.last_name
-- FROM film f
-- INNER JOIN film_actor fa
-- ON f.film_id = fa.film_id
-- INNER JOIN actor a
-- ON fa.actor_id = a.actor_id
-- WHERE f.description ILIKE '%sumo%' AND a.first_name = 'Penelope' AND a.last_name = 'Monroe'

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- SELECT f.title, f.length, f.rating, c.name
-- FROM film f
-- INNER JOIN film_category fc
-- ON f.film_id = fc.film_id
-- INNER JOIN category c
-- ON fc.category_id = c.category_id
-- WHERE f.length < 60 AND f.rating = 'R' AND c.name ILIKE 'documentary'

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
-- SELECT f.title,	 p.amount, c.first_name, c.last_name, r.return_date
-- FROM film f
-- INNER JOIN inventory i
-- ON f.film_id = i.film_id
-- INNER JOIN rental r
-- ON r.inventory_id = i.inventory_id
-- INNER JOIN payment p
-- ON p.rental_id = r.rental_id
-- INNER JOIN customer c
-- ON p.customer_id = c.customer_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan' AND p.amount > 4 AND r.return_date::date BETWEEN '2005-07-28' AND '2005-07-31'



-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
-- SELECT f.title,	 f.replacement_cost, f.description, c.first_name, c.last_name
-- FROM film f
-- INNER JOIN inventory i
-- ON f.film_id = i.film_id
-- INNER JOIN rental r
-- ON r.inventory_id = i.inventory_id
-- INNER JOIN customer c
-- ON r.customer_id = c.customer_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan' AND f.description ILIKE '%boat%' ORDER BY f.replacement_cost DESC LIMIT 1
