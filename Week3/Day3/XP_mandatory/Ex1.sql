--  Exercise 1: DVD Rental
-- Instructions

-- Get a list of all the languages, from the language table.
-- SELECT name FROM language

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.

-- SELECT f.title, f.description, l.name as language
-- FROM film f
-- INNER JOIN language l -- feels more right to use RIGHT but INNER does everything what's needed so...
-- ON f.language_id = l.language_id

-- There's no other language id in films other than 1(English)

-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

-- SELECT f.title, f.description, l.name as language
-- FROM film f
-- RIGHT JOIN language l
-- ON f.language_id = l.language_id ORDER BY l.name DESC


-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- CREATE TABLE new_film (
-- n_film_id SERIAL PRIMARY KEY,
-- n_film_name VARCHAR(25)
-- );

-- INSERT INTO new_film(n_film_name)
-- VALUES('Moebius'),('It''s Morbin Time'),('The Princess Bride');

-- SELECT * FROM new_film


-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- CREATE TABLE customer_review(
-- review_id SERIAL PRIMARY KEY,
-- title VARCHAR(50) NOT NULL,
-- score SMALLINT NOT NULL,
-- review_text TEXT NOT NULL,
-- last_update DATE NOT NULL DEFAULT CURRENT_DATE,
-- n_film_id INT,
-- language_id INT,

-- CONSTRAINT fk_review_nf_id FOREIGN KEY (n_film_id)
-- REFERENCES new_film(n_film_id) 
-- ON DELETE CASCADE,

-- CONSTRAINT fk_review_language_id FOREIGN KEY (language_id)
-- REFERENCES language(language_id)
-- ON DELETE SET NULL
-- );
-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
-- INSERT INTO customer_review(title, score, review_text, n_film_id, language_id)
-- VALUES
-- ('タイトル: モービウス', 8, 'レビュー:
-- モービウスは、視覚的に衝撃的で、従来の物語の枠を超える作品です。キム・ギドク監督によるこの映画は、欲望、復讐、
-- そして人間の感情と身体的苦痛の関係というテーマを描いています。物語は、深い悲劇によって壊れた家族を中心に展開し、
-- 登場人物の道徳観に深く挑戦します。セリフがほとんどないため、感情の重さが強調され、ジェスチャーや表情が物語の真髄を伝えています。
-- 映画は挑発的で大胆な映像を多用し、観客を不安でありながらも魅力的な領域へと引き込みます。
-- 痛みを伴う人間の感情を描いた演技は心に響き、説得力があります。いくつかのシーンは実験的で過激と感じるかもしれませんが、
-- モービウスは私たちの行動の限界や決断がもたらす影響について考えさせる作品です。', 1, (SELECT language_id FROM language WHERE name = 'Japanese')
-- ),
-- (
-- '视听盛宴与情感交织：一部值得一看的电影',
-- 10,
-- '这部电影给我留下了深刻的印象。导演巧妙地运用了视听语言，创造出一个既紧张又感人的故事。演员们的表现也非常出色，
-- 特别是主角，他/她通过细腻的演技，将角色的复杂情感展现得淋漓尽致。
-- 影片的情节紧凑，节奏把握得非常好，尽管有一些情节发展略显预测，但整体故事依然充满了吸引力。
-- 电影的视觉效果令人惊叹，特别是在动作场面和特效方面，几乎每一帧都充满了艺术感。
-- 我特别喜欢电影中的音乐，它恰到好处地提升了情绪的起伏，让观众更能沉浸其中。整体而言，
-- 这部电影是一部值得一看的佳作，无论是从剧情、演员的表现，还是制作水平来说，都做得非常出色。',
-- 2,
-- (SELECT language_id FROM language WHERE name = 'Mandarin')
-- )

-- SELECT * FROM customer_review



-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
-- DELETE FROM new_film
-- WHERE n_film_id = 1

-- SELECT * FROM customer_review

--Review that was referencing the deleted movie was deleted in a cascade