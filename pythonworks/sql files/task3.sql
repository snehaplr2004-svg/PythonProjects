create database compdb;
use compdb;
create table department (id int unique not null primary key,
							department_name varchar(30) not null);
create table employee(id int primary key,employee_name varchar(20),age int,salary int,
					joining_year int,department_id int,city varchar(30),
					foreign key(department_id) references department(id));
insert into department(id,department_name) values(1,"sales"),(2,"HR"),(3,"Marketing");
insert into employee(id,employee_name,age,salary,joining_year,department_id,city) values
			(1,"Arun",22,50000,2020,1,"Kochi"),(2,"Amal",25,55000,2019,1,"tvm"),
            (3,"Anu",23,56000,2021,2,"Kochi"),(4,"Manu",25,60000,2023,3,"klm");
-- 1.Retrieve all records from the department table             
select * from department;
-- 2.Retrieve employee_name,age and salary from the employee table
select employee_name,age,salary from employee;
-- 3.Retrieve the names and salaries of employees whose salary greater than 50,000
select employee_name,salary from employee where salary>50000;
-- 4 Retrieve the names,ages and cities of employees whose name starts with 'A'           
select employee_name,age,city from employee where employee_name like "A%";
-- 5 Retrive the names ,salaries of employees who joined after 2020 and earn more than 60000
select employee_name,salary from employee where joining_year>2020 and salary>60000;
-- 6.Retrieve name,city and salaries of employees from "Kochi" sorted by saalry in descending order
select employee_name,city,salary from employee where city="Kochi" order by salary desc;
-- 7.Find the number of employees in each department
select department_id,count(*) from employee group by department_id;
-- 8.Find average salary in each city
select city,avg(salary) from employee group by city;
-- 9.Display only those cities where the average salary greater than 45,000
select city,avg(salary) from employee group by city having avg(salary)>45000;
-- 10.Retrieve each employee name along with their corresponding department name using the relationship between two table
select employee_name,department_name from department inner join employee 
			on department.id=employee.department_id;