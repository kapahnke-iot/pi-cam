from picamera import PiCamera
import time
import datetime


camera = PiCamera()

# #####################################################################
# camera settings start
# #####################################################################

# rotation:
# possible parameters are 0, 90, 180 or 270 degree. Default is 0 degree
camera.rotation = 0


# transparency of the preview by setting the alpha level
# alpha can be any value between 0 and 255. Default is 255
camera.start_preview(alpha=255)
camera.stop_preview()

# #####################################################################
# camera settings end
# ##################################################################### 



# #####################################################################
# capture a picture with the current timestamp
# #####################################################################
# to capture a picture you need to wait minimum 2 seconds before capturing,
# to give the sensor time to set its light levels
# currently I save the picture on the Desktop, need to be changed.
camera.start_preview(alpha=255)
time.sleep(2)
timestamp = (time.strftime("%d-%m-%Y_%H:%M:%S"))
camera.capture("/home/pi/Desktop/image_captured_door_cam1"+ timestamp + ".jpg")
camera.stop_preview()



# #####################################################################
# Record a video for 5 seconds and store with the current timestamp
# #####################################################################
camera.start_preview(alpha=255)
time.sleep(5)
timestamp = (time.strftime("%d-%m-%Y_%H:%M:%S"))

# currently I save the video on the Desktop, need to be changed.
camera.start_recording("/home/pi/Desktop/video_door_cam1_"+ timestamp + ".h264")
camera.stop_preview()

# print hint
print ("To play the video on the RP use the omxplayer")
