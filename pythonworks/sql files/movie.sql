-- =========================================
-- CREATE DATABASE
-- =========================================

CREATE DATABASE movie_db;

USE movie_db;


-- =========================================
-- CREATE TABLE
-- =========================================

CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(100) NOT NULL,
    director VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    language VARCHAR(30) NOT NULL,
    runtime INT NOT NULL
);


-- =========================================
-- INSERT 50 RECORDS
-- Runtime is in minutes
-- =============================movie============

INSERT INTO movie
(movie_name, director, year, language, runtime)
VALUES
('Titanic', 'James Cameron', 1997, 'English', 195),
('Dil To Pagal Hai', 'Yash Chopra', 1997, 'Hindi', 180),
('Aaram Thamburan', 'Shaji Kailas', 1997, 'Malayalam', 175),
('Iruvar', 'Mani Ratnam', 1997, 'Tamil', 140),
('Amruthavarshini', 'Dinesh Babu', 1997, 'Kannada', 145),

('The Truman Show', 'Peter Weir', 1998, 'English', 103),
('Dil Se', 'Mani Ratnam', 1998, 'Hindi', 163),
('Summer in Bethlehem', 'Sibi Malayil', 1998, 'Malayalam', 157),
('Jeans', 'S Shankar', 1998, 'Tamil', 166),
('A', 'Upendra', 1998, 'Kannada', 136),

('The Matrix', 'The Wachowskis', 1999, 'English', 136),
('Hum Dil De Chuke Sanam', 'Sanjay Leela Bhansali', 1999, 'Hindi', 188),
('Vanaprastham', 'Shaji N Karun', 1999, 'Malayalam', 119),
('Mudhalvan', 'S Shankar', 1999, 'Tamil', 169),
('Upendra', 'Upendra', 1999, 'Kannada', 138),

('Gladiator', 'Ridley Scott', 2000, 'English', 155),
('Mohabbatein', 'Aditya Chopra', 2000, 'Hindi', 216),
('Devadoothan', 'Sibi Malayil', 2000, 'Malayalam', 165),
('Kandukondain Kandukondain', 'Rajiv Menon', 2000, 'Tamil', 157),
('Sparsha', 'Sunil Kumar Desai', 2000, 'Kannada', 136),

('A Beautiful Mind', 'Ron Howard', 2001, 'English', 135),
('Lagaan', 'Ashutosh Gowariker', 2001, 'Hindi', 224),
('Meesha Madhavan', 'Lal Jose', 2002, 'Malayalam', 149),
('Anbe Sivam', 'Sundar C', 2003, 'Tamil', 160),
('Nanna Preethiya Hudugi', 'Nagathihalli Chandrashekar', 2001, 'Kannada', 150),

('The Dark Knight', 'Christopher Nolan', 2008, 'English', 152),
('3 Idiots', 'Rajkumar Hirani', 2009, 'Hindi', 170),
('Urumi', 'Santosh Sivan', 2011, 'Malayalam', 160),
('Vinnaithaandi Varuvaayaa', 'Gautham Vasudev Menon', 2010, 'Tamil', 157),
('Super', 'Upendra', 2010, 'Kannada', 135),

('Inception', 'Christopher Nolan', 2010, 'English', 148),
('Dangal', 'Nitesh Tiwari', 2016, 'Hindi', 161),
('Drishyam', 'Jeethu Joseph', 2013, 'Malayalam', 164),
('96', 'C Prem Kumar', 2018, 'Tamil', 158),
('Kantara', 'Rishab Shetty', 2022, 'Kannada', 148),

('Interstellar', 'Christopher Nolan', 2014, 'English', 169),
('Andhadhun', 'Sriram Raghavan', 2018, 'Hindi', 139),
('Premam', 'Alphonse Puthren', 2015, 'Malayalam', 156),
('Vikram', 'Lokesh Kanagaraj', 2022, 'Tamil', 174),
('KGF Chapter 1', 'Prashanth Neel', 2018, 'Kannada', 156),

('Oppenheimer', 'Christopher Nolan', 2023, 'English', 180),
('Jawan', 'Atlee', 2023, 'Hindi', 169),
('2018', 'Jude Anthany Joseph', 2023, 'Malayalam', 150),
('Maharaja', 'Nithilan Saminathan', 2024, 'Tamil', 141),
('KGF Chapter 2', 'Prashanth Neel', 2022, 'Kannada', 168),

('L2 Empuraan', 'Prithviraj Sukumaran', 2025, 'Malayalam', 179),
('Aadu 3', 'Midhun Manuel Thomas', 2026, 'Malayalam', 170),
('Vaazha II: Biopic of a Billion Bros', 'Savin SA', 2026, 'Malayalam', 163),
('Patriot', 'Mahesh Narayanan', 2026, 'Malayalam', 180),
('Toxic', 'Geetu Mohandas', 2026, 'Kannada', 180);

select * from movie;
-- 				select unique language from movie
select distinct(language) from movie;
-- 		count movie in each lang
select language,count(*) from movie group by language;
	-- 	count of movie in each year
select year,count(*) from movie group by year;
		-- highest runtime
select max(runtime) from movie;        
--        movie details having highest runtime
select * from movie where runtime=(select max(runtime) from movie);		
--    	  movie details with lowest runtime
select * from movie where runtime=(select min(runtime) from movie);		
-- 		  display avg runtime of movies
select avg(runtime) from movie;
-- 		  display all movie having runtime greater than average runtime
select  * from movie where runtime>(select avg(runtime) from movie);		
-- 		  find latest year from movie table
select max(year) from movie;
-- 			display all movie released in latest year
select * from movie where year=(select max(year) from movie);
-- 			find movies in the same year as Premam 
select * from movie where year=(select year from movie where movie_name="Premam");
-- 			find movie having runtime > runtime Titanic
select * from movie where runtime>(select runtime from movie where movie_name="Titanic");

