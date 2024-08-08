use sakila;

select name, name like '%y' as ends_in_y
from category;

select name, name regexp 'y$' as ends_in_y
from category;

use sqlclass_db;
delete from string_tbl;

insert into string_tbl(text_fld)
values('This string was 29 characters');

update string_tbl
set text_fld = concat(text_fld,', but now it is longer');

select text_fld from string_tbl;

use sakila;
select concat(first_name,' ',last_name, 
' has been a customer since ',date(create_date)) as cust_narrative 
from customer;

select insert('goodbye world',9,0,'cruel ') as string;
select insert('goodbye world', 1,7,'hello') as string;

select replace('goodbye world', 'goodbye', 'hello') as replace_str;
select substr('goodbye cruel world',9,5);

select round(72.0909,1), round(72.0909,2), round(72.0909,3);
select truncate(72.0956,1),truncate(72.0956,2),truncate(72.0956,3);

select cast('2019-09-17 15:30:00'as datetime);
select cast('2019-09-17'as date) date_field,
	   cast('108:17:57' as time) time_field;
select cast('20190917153000'as datetime);

select str_to_date('September 17, 2019', '%M %d, %Y') as return_date;

select str_to_date('04/30/2024', '%m/%d/%Y') as date1;
select str_to_date('01,5,2024','%d,%m,%Y')as date2;
select str_to_date('15:35:00', '%H:%i:%s') as time1;