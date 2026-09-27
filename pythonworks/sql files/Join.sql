-- 			FOREIGN KEY
create database taskdb;
use taskdb;
create table user(id int not null auto_increment primary key,
					name varchar(30) unique not null,email varchar(30) unique not null,
                    phone varchar(20) unique not null);
create table task(id int  auto_increment primary key,
					title varchar(30) not null,date datetime default current_timestamp,
                    status enum("pending","finished") default "pending",
                    user_id int ,
                    foreign key(user_id) references user(id));
insert into user (name,email,phone) values("Arun","arun@gmail.com","7654321"),
										  ("Amal","amal@gmail.com","2345689"),
                                          ("Hari","hari@gmail.com","461748529");
insert into task(title,user_id) values ("pay bill",1),("book a ticket",1),("buy groceries",2);

insert into task(title,user_id) values ("pay bill",5);-- not work bz the foreign key 5 not exist

insert into task(title,status,user_id) values ("pay bill","finished",3);
insert into user (name,email,phone) values("Yash","yash@gmail.com","949510617");
select * from user;
select * from task;

--       JOIN OPERATION

select * from user inner join task on user.id=task.user_id;
select name,title,status from user inner join task on user.id=task.user_id;

select * from user left join task on user.id=task.user_id;

select * from user cross join task;


-- create two tables Books and Author
-- Books  --bookno,title,author id(foreign),price,pages,published year
-- Author ---author_id,name,nationality,birthyear

create database libry;
use libry;
create table author(author_id int auto_increment not null primary key,
			        name varchar(30),nationality varchar(30), birthyear varchar(30));
create table books(bookno int auto_increment primary key,title varchar(50),authorid int,
					foreign key(authorid) references author(author_id), price int,
                    pages int,published_year varchar(30));
insert into author(name,nationality,birthyear) values("Ravinder Singh","Indian","21-03-1995"),
					('Paulo Coelho','Indian',"11-07-1988"),("J K Rowling","British","20-05-1990");
select * from author;                   
insert into books(title,authorid,price,pages,published_year) values
				("Your Dreams are mine now",1,400,80,2016),("Alcheimist",2,600,140,2011),
                ("Harry Porter",3,800,200,2008);
insert into books(title,authorid,price,pages,published_year) values
				("I too had a love story",1,500,120,2019);
select * from books;
                
-- 1,Find all books of specific author
select * from books where authorid =1;
select * from books where authorid=(select author_id from author where name like "Ravinder Singh");

-- 2.Find the publication year of a particular book
select published_year from books where title= "Harry Porter";

-- 3.Find the youngest author
select * from author where birthyear=(select max(birthyear) from author);

-- 4.List books with their corresponding author where booktitle contains a specific keyword
select title,name from author inner join books on author.author_id=books.authorid 
					where title like "%Porter%";
                    
-- 5.list all authors who have written books published after a particular year.  -- use join
select * from author inner join books on author.author_id=books.authorid 
			where published_year>"2012";

