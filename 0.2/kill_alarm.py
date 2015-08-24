import psutil
from subprocess import Popen
import MySQLdb
import os

host=""
user=""
passwd=""
dbname=""
db=MySQLdb.connect(host,user,passwd,dbname)
cursor=db.cursor()

def TURN_OFF(name):
  sql="UPDATE `DEVICE` SET `Status` =False WHERE Name =\'%s\'"%name
  cursor.execute(sql)
  db.commit()
  return "ok"


for i in psutil.pids():
 process = psutil.Process(i)
 if process.cmdline() == ['python', '/home/pi/Desktop/lazyroom/alarm.py']:
        print('Process found. Terminating it.')
        process.kill()
        TURN_OFF("Main_Alarm")