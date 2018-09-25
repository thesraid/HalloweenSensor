# Halloween Sensor Project
# thesraid@gmail.com
# 29 Oct 2016

# This library is for running operating system commands
import os
# This library is for talking to the GPIO pins on the raspberry pi
import RPi.GPIO as GPIO
# This is to tell the time
import time
# This is to be able to pick a random video from a list
import random

# Set the list of videos to choose from
videos = ["11217.m4v", "14905.m4v", "17161.m4v", "21178.m4v", "2288.m4v", "25006.m4v", "25238.m4v", "1467.m4v", "15359.m4v", "19173.m4v", "22063.m4v", "23924.m4v", "25065.m4v", "31227.m4v"] 
# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set a variable to hold the GPIO Pin identity
# This is the pin the sensor is attached to. Have a look at the GPIO diagram for your pi
PinPIR = 17
print("PIR Module Test (CTRL-C to exit)")

# Set pin as input
GPIO.setup(PinPIR, GPIO.IN)

# Variables to hold the current and last states
Current_State = 0
Previous_State = 0
try:
        print("Waiting for PIR to settle ...")
        # Loop until PIR output is 0
        while GPIO.input(PinPIR)==1:
                Current_State = 0

        print(" Ready")
        # Loop until users quits with CTRL-C
        while True:
                # Read PIR state
                Current_State = GPIO.input(PinPIR)
                # If the PIR is triggered
                if Current_State==1 and Previous_State==0:
                        print(" Motion detected!")
			# This runs the Wemo cli to turn on my wemo smart switch. It's IP is 192.168.0.20. I installed https://www.npmjs.com/package/belkin-wemo-command-line-tools to get this cli. 
			# It's connected to the monitor. THis hides the monitor at night as there is no light bleed. 
			system("wemo --host 192.168.0.20 --action ON")
			# This is the command to flip the video on it's side, centre it and play it. My screen is in portrait mode. 
                        PlayVideoString = "omxplayer -o both --win 0,0,800,1280 --aspect-mode fill --orientation 180 /home/john/Videos/%s" % random.choice(videos)
                        os.system(PlayVideoString)
			# Turn off the switch/screen
                       	os.system("wemo --host 192.168.0.20 --action OFF")
			# Wait for 90 seconds
                        print("So sleepy")
                        time.sleep(90.01)
                        # Record previous state
                        Previous_State=1
                # If the PIR has returned to ready state
                elif Current_State==0 and Previous_State==1:
                        print(" Ready")
                        Previous_State=0
                
                # Wait for 10 milliseconds
		# I can't remeber why I did this. MAy not be needed. 
                time.sleep(0.01)

# When I hit Ctrl & C to shit it down, try to do so gracefully. 
except KeyboardInterrupt:
        print(" Quit")
        # Reset GPIO settings
        GPIO.cleanup()

