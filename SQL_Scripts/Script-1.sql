use mysql;

select user, host from user;

create user 'member1'@'%' identified by '1234';
grant all privileges on *.* to 'member1'@'%';
grant grant options on *.* to 'member1'@'%';
flush privileges;

drop user 'member1'@'%';
flush privileges; 
