import os

# For immediate shutdown
os.system("shutdown /s /t 1")

# Shutdown with timer 
timer = 7
os.system("shutdown /s /t {}".format(timer))

# For immediate restart 
os.system("shutdown /r /t 1")

# Restart with timer 
os.system("shutdown /r /t {}".format(timer))

# Timer Code 
import time
import sys

for remainingTime in range(timer, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining to shutdown/ restart".format(remainingTime)) 
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rShutting Down The System                    \n")