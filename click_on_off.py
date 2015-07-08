import psutil
from subprocess import Popen

for i in psutil.pids():
 process = psutil.Process(i)
 if process.cmdline() == ['python', '/home/pi/Desktop/test2.py']:
        print('Process found. Terminating it.')
        process.kill()
        break
else:
    print('Process not found: starting it.')
    Popen(['python', '/home/pi/Desktop/test2.py'])
