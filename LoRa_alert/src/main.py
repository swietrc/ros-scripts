#!/usr/bin/env python
# license removed for brevity
import rospy
import serial
from std_msgs.msg import String


ser = serial.Serial('/dev/ttyACM0', 9600)
send_data = True
timer = Threading.Timer(5.0, reset_timer)
	
def reset_timer():
    send_data = True
    timer.stop()

def callback(self, data):
    rospy.loginfo("Sending coordinates via LoRa")
    ser.write(b'1\r\n')
    send_data = False
    timer.start()

if __name__ == '__main__':
    rospy.Subscriber("mouvement_zigbee", String, self.callback)
