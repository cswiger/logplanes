logplanes
=========

Simple python wrapper for dump1090 to save aircraft in a mysql db

Setup MySQL db with:

mysql > create database aircraft;

mysql > create user 'aircraft'@'192.168.1.252' identified by 'Password01';

mysql > grant all on aircraft.* to 'aircraft'@'192.168.1.235';

$ mysql -h 192.168.1.251 -u aircraft -p aircraft
Enter password:
Welcome ....
mysql> create table aircraft (id INT AUTO_INCREMENT primary key, ident char(10), spotted timestamp);
Query OK, 0 rows affected (0.36 sec)
