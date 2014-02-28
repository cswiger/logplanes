#!/usr/bin/python

import MySQLdb, os, datetime

mysql = MySQLdb.connect(host='192.168.1.251',user='aircraft',passwd='Password01',db='aircraft')
mysqlcursor = mysql.cursor()

adsb = os.popen("/home/chuck/src/dump1090/dump1090 --net --aggressive")

while True:
   line = adsb.readline()
   if ( line.find('    Identification ') != -1) :
     now = datetime.datetime.today()
     hrago = now + datetime.timedelta(0,0,0,0,0,-1,0)     # adding -1 hour
     timestamp = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
     hrago_timestamp = str(hrago.year) + '-' + str(hrago.month) + '-' + str(hrago.day) + ' ' + str(hrago.hour) + ':' + str(hrago.minute) + ':' + str(hrago.second)
     dummy,cs = line.split(':')
     callsign = cs.strip()
     sql = "select id from aircraft where ident = '" + callsign + "' and spotted > '" + hrago_timestamp + "'"
     if ( mysqlcursor.execute(sql) == 0L ):
	sql = "insert into aircraft values(NULL, '" + callsign + "', '" + timestamp + "')"
        mysqlcursor.execute(sql)

