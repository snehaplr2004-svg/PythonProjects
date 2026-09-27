					-- **SQL Queries**
		-- creating a new database file

		-- show all databases in server
		-- show databases;

			-- creating a new db file
			-- create database databasename;
		--  eg) create database company;
       
       -- **PROBLEM**
-- create database company;
			-- sql query to switch to a particular db file
			-- use databasename;
-- use company;
		-- query to create a table 
-- create table employee(empid int not null unique primary key,
						-- name varchar(30),
--                         age int,
--                         gender enum("male","female"),
--                         place varchar(30),
--                         salary int,
--                         designation varchar(30));

-- insert into employee(empid,name,age,gender,place,salary,designation)
-- 			values(101,"Arun",23,"male","ekm",20000,"developer"),
--             (102,"Amal",29,"male","tvm",40000,"developer"),
--             (103,"Anu",25,"female","ekm",30000,"tester"),
--             (104,"Kiran",27,"male","tcr",35000,"tester"),
--             (105,"Manu",26,"male","tvm",27000,"tester");
-- insert into employee(empid,name,age,gender,place,salary,designation)
-- 			values(106,"Tharun",24,"male","klm",50000,"designer");

			-- sql query to read all records
--  select * from employee;

			-- sql query to read records with empid=103
-- select * from employee where empid=103;

    -- sql query to read all records with attributes empid and salary
-- select empid,salary from employee;

    -- sql query to read all records having place=ekm
-- select * from employee where place="ekm";

    -- sql query to read all records having gender =female
-- select * from employee where gender="female";

			-- sql query to read all records in ascending order based on salary
-- select * from employee order by salary;
			-- sql query to read all records in ascending order based on salary
-- select * from employee order by salary desc;

use company;
-- select * from employee where place="ekm" and age<30; 
-- select * from employee where  not(designation="developer"); 
-- select * from employee where salary between 30000 and 40000; 
-- select * from employee where age between 25 and 30;
--  select * from employee where salary=30000 or salary=20000; 
	-- or
 --    select * from employee where salary in(20000,30000); 
 -- select * from employee where age in(28,30); 
-- select * from employee where name like "A%"; 
-- select * from employee where name like "__u";
-- select * from employee where place like "%m";
				-- ORDER BY-- 
-- select * from employee order by salary;
-- select * from employee order by age desc;
-- select * from employee order by name;

	-- 	LIMIT-- 
-- select * from employee limit 3;
-- select * from employee limit 2 offset 1;

-- update employee set age=30 ,salary=50000 where empid=106;
-- select * from employee;

-- delete from employee where empid=102;
-- select * from employee;

-- 				AGGREGATE FUNCTIONS
-- select max(age) from employee;
-- select avg(salary) from employee;
-- select count(*) from employee;
-- select count(age) from employee;
-- select sum(salary) from employee;

select gender,count(*) from employee group by gender;
select gender,max(salary) from employee group by gender;
select place, count(*) from employee group by place;
select place,avg(salary) from employee group by place;
select place,avg(salary) from employee group by place having place="ekm";
select designation,max(salary) from employee group by designation having designation="developer";