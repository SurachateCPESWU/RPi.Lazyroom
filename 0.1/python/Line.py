from line import LineClient, LineGroup, LineContact
import time
from device_v2 import *
USERNAME = ''
PASSWORD = ''
#optional
COMPUTERNEME = ''
TOKEN = ''
#TOKEN2 = ''
########################

def check_state(sender):
	sender.sendMessage("Online.")

try :
        client = LineClient(id=USERNAME, password=PASSWORD, authToken=TOKEN, com_name=COMPUTERNEME)
        print "Login succeed"
except:
        print "Error to login."

while 1:
     for op in client.longPoll():
             sender   = op[0]
             receiver = op[1]
             message  = op[2]
             if message.text == "status":
                    check_state(sender)
             elif message.text == "On1":
                    sys_do=TURN_ON("DEVICE1")
                    print sys_do
             elif message.text == "Off1":
                    sys_do=TURN_OFF("DEVICE1")
                    print sys_do
             elif message.text == "On2":
                    sys_do=TURN_ON("DEVICE2")
                    print sys_do
             elif message.text == "Off2":
                    sys_do=TURN_OFF("DEVICE2")
                    print sys_do
             elif message.text == "On3":
                    sys_do=TURN_ON("DEVICE3")
                    print sys_do
             elif message.text == "Off3":
                    sys_do=TURN_OFF("DEVICE3")
                    print sys_do
             elif message.text == "On4":
                    sys_do=TURN_ON("DEVICE4")
                    print sys_do
             elif message.text == "Off4":
                    sys_do=TURN_OFF("DEVICE4")
                    print sys_do
