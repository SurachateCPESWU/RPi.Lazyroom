import RPi.GPIO as GPIO
import MySQLdb
import os
###############################	
host=""
user=""
passwd=""
dbname=""
db=MySQLdb.connect(host,user,passwd,dbname)
cursor=db.cursor()
sql="SELECT * FROM `DEVICE` WHERE 1"
cursor.execute(sql)
PIN_temp=cursor.fetchall()
PIN=PIN_temp[0][0],PIN_temp[1][0],PIN_temp[2][0],PIN_temp[3][0]

###############################
for i in range(1,5):
        temp=PIN[i-1]
        os.system("gpio mode %d out"%temp)

def TURN_ON(name):
	sql="SELECT * FROM `DEVICE` WHERE Name=\'%s\'"%name
	cursor.execute(sql)
	temp=cursor.fetchall()
	if temp[0][2]==0:
		os.system("gpio write %d 0"%temp[0][0])
		sql="UPDATE `DEVICE` SET `Status` = True WHERE Name =\'%s\'"%name
		cursor.execute(sql)
		db.commit()
		return "ok"
	else : return "ERROR"

def TURN_OFF(name):
	sql="SELECT * FROM `DEVICE` WHERE Name=\'%s\'"%name
	cursor.execute(sql)
	temp=cursor.fetchall()
	if temp[0][2]==1:
		os.system("gpio write %d 1"%temp[0][0])
		sql="UPDATE `DEVICE` SET `Status` =False WHERE Name =\'%s\'"%name
		cursor.execute(sql)
		db.commit()
		return "ok"
	else : return "ERROR"
	
