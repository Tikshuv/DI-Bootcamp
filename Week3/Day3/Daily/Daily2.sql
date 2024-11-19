-- Part II:

-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL

-- CREATE TABLE book(
-- book_id SERIAL PRIMARY KEY,
-- title VARCHAR(25) NOT NULL,
-- author VARCHAR(50) NOT NULL
-- );

-- Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee
-- INSERT INTO book(title, author)
-- VALUES('Alice In Wonderland', 'Lewis Carroll'),('Harry Potter', 'J.K. Rowling'),('To kill a mockingbird', 'Harper Lee');


-- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);
-- CREATE TABLE student(
-- student_id SERIAL PRIMARY KEY,
-- name VARCHAR(25) NOT NULL UNIQUE,
-- age SMALLINT NOT NULL CHECK(age <= 15)
-- );

-- Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14

-- INSERT INTO student(name,age)
-- VALUES('John',12),('Lera',11),('Patrick',10),('Bob',14);

-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date

-- CREATE TABLE library(
-- book_fk_id SMALLINT,
-- student_id SMALLINT,
-- borrowed_date DATE,
-- CONSTRAINT fk_lib_book_id FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- CONSTRAINT fk_lib_student_id FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021

-- INSERT INTO library(book_fk_id, student_id, borrowed_date)
-- VALUES((SELECT book_id FROM book WHERE title ILIKE 'Alice In Wonderland'), (SELECT student_id FROM student WHERE name ILIKE 'John'), '02/15/2022'),
-- ((SELECT book_id FROM book WHERE title ILIKE 'To kill a mockingbird'), (SELECT student_id FROM student WHERE name ILIKE 'Bob'), '03/03/2021'),
-- ((SELECT book_id FROM book WHERE title ILIKE 'Alice In Wonderland'), (SELECT student_id FROM student WHERE name ILIKE 'Lera'), '05/23/2021'),
-- ((SELECT book_id FROM book WHERE title ILIKE 'Harry Potter'), (SELECT student_id FROM student WHERE name ILIKE 'Bob'), '08/12/2021')

-- Display the data
-- Select all the columns from the junction table

-- SELECT * FROM library;

-- Select the name of the student and the title of the borrowed books

-- SELECT s.name, b.title
-- FROM library l
-- RIGHT JOIN student s
-- ON l.student_id = s.student_id
-- RIGHT JOIN book b
-- ON l.book_fk_id = b.book_id;

-- Select the average age of the children, that borrowed the book Alice in Wonderland
-- SELECT ROUND(AVG(s.age), 2), b.title
-- FROM library l
-- JOIN student s
-- ON l.student_id = s.student_id
-- JOIN book b
-- ON l.book_fk_id = b.book_id
-- WHERE b.title ILIKE 'Alice In Wonderland'
-- GROUP BY b.title

-- Delete a student from the Student table, what happened in the junction table ?

-- DELETE FROM student
-- WHERE name ILIKE 'Bob';

-- SELECT * FROM library

-- two records with Bob were deleted accordingly because of CASCADE
