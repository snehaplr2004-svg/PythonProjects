-- Create Database
CREATE DATABASE librarydb;
-- Select Database
USE librarydb;
-- Create Book Table
CREATE TABLE book (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(8,2),
    publishedyear INT
);
-- Insert 10 Records
INSERT INTO book
(id, title, author, category, price, publishedyear)
VALUES
(1, 'The Alchemist', 'Paulo Coelho', 'Fiction', 450.00, 1988),
(2, 'Wings of Fire', 'A P J Abdul Kalam', 'Biography', 300.00, 1999),
(3, 'The Guide', 'R K Narayan', 'Fiction', 350.00, 1958),
(4, 'Godan', 'Munshi Premchand', 'Classic', 280.00, 1936),
(5, 'Atomic Habits', 'James Clear', 'Self Help', 550.00, 2018),
(6, 'Ikigai', 'Hector Garcia', 'Self Help', 400.00, 2016),
(7, 'Harry Potter', 'J K Rowling', 'Fantasy', 650.00, 1997),
(8, 'The Hobbit', 'J R R Tolkien', 'Fantasy', 500.00, 1937),
(9, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 'Finance', 600.00, 1997),
(10, 'The Power of Now', 'Eckhart Tolle', 'Self Help', 480.00, 1997);

-- Display All Records
SELECT * FROM book;

-- 1. Display the number of books in each category.
select category,count(*) from book group by category;

-- 2. Display the average price of books in each category.
select category,avg(price) from book group by category;

-- 3. Display the maximum price of books in each category.
select category,max(price) from book group by category;

-- 4. Display the minimum price of books in each category.
select category,min(price) from book group by category;

-- 5. Display the total price of books in each category.
select category,sum(price) from book group by category;

-- 6. Display the book(s) whose price is greater than the average price of all books.
select * from book where price > (select avg(price) from book);

-- 7. Display the book(s) having the highest price using a nested query.
select * from book where price=(select max(price) from book);

-- 8. Display the book(s) having the lowest price using a nested query.
select * from book where price=(select min(price) from book);

-- 9. Display the book(s) whose price is *greater than the price of 'The Alchemist' 
-- using a nested query.
select * from book where price > (select price from book where title="The Alchemist");

-- 10. Display the book(s) having the second-highest price using a nested query.
select * from book order by price desc limit 1 offset 1;

			-- or method
		select *from book where price=
		(select max(price) from book where price<(select max(price) from book)); 
