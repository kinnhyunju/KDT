use sqlclass_db;

drop table if exists string_tbl;
create table string_tbl
(char_fld char(30),
vchar_fld varchar(30),
text_fld text
);

insert into string_tbl (char_fld, vchar_fld, text_fld)
values ('This is char data',
		'This is varchar data',
		'This is text data');
select * from string_tbl;

# update string_tbl
# set vchar_fld = 'This is a piece of extremely long varchar data';
# SQL Error [1406] [22001]: Data truncation: Data too long for column 'vchar_fld' at row 1
	# strict모드로 예외 발생

# 현재 모드 확인
select @@session.sql_mode;

set sql_mode='ansi';
select @@session.sql_mode;

update string_tbl
set vchar_fld = 'This is a piece of extremely long varchar data';
select vchar_fld from string_tbl;

delete from string_tbl;

insert into string_tbl(char_fld, vchar_fld, text_fld)
values ('This string is 28 characters',
		'This string is 28 characters',
		'This string is 28 characters');
		
select length(char_fld) as char_length,
length(vchar_fld) as varchar_length,
length(text_fld) as text_lenth
from string_tbl;

select position('characters' in vchar_fld) from string_tbl;

select locate('is', vchar_fld, 5) from string_tbl;
select locate('is', vchar_fld, 1) from string_tbl;

delete from string_tbl;

insert into string_tbl(vchar_fld)
values('abcd'),
	  ('xyz'),
	  ('QRSTUV'),
	  ('qrstuv'),
	  ('12345');
	 
select vchar_fld from string_tbl order by vchar_fld;

select strcmp('12345','12345') 12345_12345,
	   strcmp('abcd', 'xyz') abcd_xyz,
	   strcmp('abcd', 'QRSTUV') abcd_QRSTUV,
	   strcmp('qrstuv', 'QRSTUV') qrstuv_QRSTUV,
	   strcmp('12345', 'xyz') 12345_xyz,
	   strcmp('xyz', 'qrstuv') xyz_qrstuv;