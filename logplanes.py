#!/usr/bin/python

import MySQLdb, os, datetime

mysql = MySQLdb.connect(host='192.168.1.251',user='aircraft',passwd='Password01',db='aircraft')
mysqlcursor = mysql.cursor()

adsb = os.popen("/home/chuck/src/dump1090/dump1090 --net --aggressive")

while True:
   line = adsb.readline()
   if ( line.find('    Identification ') != -1) :
     now = datetime.datetime.today()
     timestamp = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
     dummy,cs = line.split(':')
     callsign = cs.strip()
     sql = "select id from aircraft where ident = '" + callsign + "'"
     if ( mysqlcursor.execute(sql) == 0L ):
	sql = "insert into aircraft values(NULL, '" + callsign + "', '" + timestamp + "')"
        mysqlcursor.execute(sql)

