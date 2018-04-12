#!/usr/bin/env python
# license removed for brevity
import rospy
import serial
import threading
import time
from std_msgs.msg import String

ser = serial.Serial('/dev/ttyACM0', 115200)
send_data = True

timer = None

def reset_timer():
    global send_data, timer
    send_data = True
    timer.cancel()

def callback(data):
    global send_data, timer
    if send_data == True:
        rospy.loginfo("Sending coordinates via LoRa")
        ser.write(b'1\r\n')
    send_data = False
    timer = threading.Timer(30.0, reset_timer)
    timer.start()

if __name__ == '__main__':
    rospy.init_node('lora_gps', anonymous=True)
    rospy.Subscriber("mouvement_zigbee", String, callback)
    while not rospy.is_shutdown():
        pass 
	
