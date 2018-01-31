#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

speed = 1
distance = 1

def move():
    # Start new node
    rospy.init_note('robot_twist', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0

    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    velocity_publisher.publish(vel_msg)

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    move()
