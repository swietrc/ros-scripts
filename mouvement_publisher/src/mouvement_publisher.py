#!/usr/bin/env python
# license removed for brevity
import rospy
import serial
from std_msgs.msg import String


ser = serial.Serial('/dev/ttyACM0', 115200)
def talker():
    pub = rospy.Publisher('mouvement_zigbee', String, queue_size=10)
    rospy.init_node('mouvement_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	pub.publish(ser.readline())
       	rate.sleep()
	
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
