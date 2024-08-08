use sakila;

show tables;

use sqlclass_db;

drop table if exists person;

create table person
	(person_id smallint unsigned,
	fname varchar(20),
	lname varchar(20),
	eye_color enum('BR', 'BL', 'GR'),
	birth_date date,
	street varchar(30),
	city varchar(20),
	state varchar(20),
	country varchar(20),
	postal_code varchar(20),
	primary key (person_id)
	);
	
# person 테이블 구성 확인
desc person;

drop table if exists favorite_food;
create table favorite_food
	(person_id smallint unsigned,
	food varchar(20),
	primary key (person_id, food),
	foreign key (person_id) references person(person_id)
	);
	
# favorite_food 테이블 구성 확인
desc favorite_food;

set foreign_key_checks=0;
alter  table person modify person_id smallint unsigned auto_increment;
set foreign_key_checks=1;

# person 테이블 구성 확인
desc person;

insert into person
	(person_id, fname, lname, eye_color, birth_date)
	values (null, 'William', 'Turner', 'BR', '1972-05-27');
	
select * from person;

select person_id, fname, lname, birth_date from person;

select person_id, fname,lname,birth_date from person where lname='Turner';

insert into favorite_food (person_id, food) values(1,'pizza');
insert into favorite_food (person_id, food) values(1,'cookies');
insert into favorite_food (person_id, food) values(1,'nachos');
select * from favorite_food;

delete from favorite_food where person_id=1;
select * from favorite_food;

insert into favorite_food(person_id, food) values (1,'pizza'), (1,'cookie'), (1,'nachos');
select * from favorite_food;

select food from favorite_food where person_id=1 order by food;

insert into person
(person_id, fname, lname, eye_color, birth_date, street, city, state, country, postal_code)
values (null, 'Susan', 'Smith', 'BL', '1975-11-02', '23 Maple St.', 'Arlington', 'VA', 'USA','20220');

select person_id, fname, birth_date from person;

update person
set street='1225 Tremon St.',
	city = 'Boston',
	state = 'MA',
	country = 'USA',
	postal_code = '02138'
where person_id=1;
select * from person;

delete from person where person_id=2;

select * from person;