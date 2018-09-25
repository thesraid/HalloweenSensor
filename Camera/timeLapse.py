#!/usr/bin/env python

"""
Take a photo every 10 seconds
https://learn.pimoroni.com/tutorial/tanya/make-a-timelapse-with-octocam
"""
import time
import picamera
import sys

# Makes a shorter name for the Pi camera, and sets the resolution.
# Change the resolution if you want better/lower quality.
# A resolution of 1920 x 1080 is approx 1.1MB per photo.

camera = picamera.PiCamera()
camera.resolution=(1920, 1080)

# Gets the camera on and allows it time to detect light levels

#camera.start_preview()
time.sleep(5)

# A loop that takes pictures and names them with the time and date.
# The timestamp has to be in the loop so it takes a current time for each photo.
# The image is then saved with the name img-timestamp.jpg.

try:
   while True:
      ts=time.strftime("%Y-%m-%d-%H%M%S", time.gmtime())
      camera.capture('img-'+ts+'.jpg')
      time.sleep(10)

except KeyboardInterrupt:
   #camera.stop_preview()
   sys.exit()
