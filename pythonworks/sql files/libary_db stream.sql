create database library_db;
use library_db;
create table book(id int not null auto_increment primary key,
		title varchar(30),
        author varchar(30),
        price int,
        pages int,
        language varchar(30));
insert into book(title,author,price,pages,language) values
				("Your Dreams","Ravinder",300,120,"eng");


create database vehicle_db;
use vehicle_db;
create table vehicle(id int not null auto_increment primary key,
		brand varchar(30),
        model varchar(30),
        type varchar(30),
        price int,
        year int);
insert into vehicle(brand,model,type,price,year) values
				("Honda","nexa","b-6",50000,2020);
