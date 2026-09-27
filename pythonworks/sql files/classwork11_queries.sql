create database school;
use school;
create table student(student_id int not null unique primary key,
 					ID_name varchar(100),age int,gender varchar(10),
                     course varchar(100),marks int,city varchar(100));
insert into student(student_id,ID_name,age,gender,course,marks,city)values
 		     (100,"Aju",18,"male","computer science",80,"Kochi"),
             (101,"Kripa",20,"female","commerce",90,"Klm"),
             (102,"Tom",25,"male","humanities",40,"Tvm"),
             (103,"Meenu",21,"female","computer science",20,"Tvm"),
             (104,"Ram",23,"male","humanities",35,"Kochi"),
             (105,"Kiran",22,"male","computer science",80,"Klm");

	-- 	display all records from the student table
select * from student;    

		-- display name,course and marks for all students 
select ID_name,course,marks from student; 

		-- display name and marks of students who scored more than 80
select ID_name,marks from student where marks>80;  
			-- display all details of students enrolled in computer science
select * from student where course="computer science";       
			-- display names,ages,cities of students whose age between 18 & 22
select ID_name,age,city from student where age between 18 and 22;    
				-- display names,mark and courses of students from kochi 
--                 sorted by marks in descending order
select ID_name,marks,course from student where city="Kochi"order by marks desc; 
					-- count the total number of students in each city
select city,count(*) as total from student group by city; 
				-- 	display the average of marks obtainbed by student 
                -- in each course
select course,avg(marks) from student group by course;
			-- 	display details of students with highest marks
select * from student where marks=(select max(marks) from student); 
				-- insert a new record into the table
insert into student(student_id,ID_name,age,gender,course,marks,city)values
			(106,"Sam",20,"male","computer science",85,"Kochi");
           --  update marks of all students who scored below 50 
           -- by adding 5 bonus marks
    update student set marks = marks + 5 where marks < 50;
		-- 	delete all student records where marks are less than 35 
    delete from student where marks < 35;