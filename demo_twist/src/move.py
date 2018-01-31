#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


class RobotMove:
    DRIVE_SPEED = 0.2
    DRIVE_SPEED_FACTOR = 0.80
    ROT_SPEED = 1.2
    ROT_SPEED_FACTOR = 0.7
    CMD_VEL_TIME_FACTOR = 0.625
    
    # Start new node
    rospy.init_note('robot_twist', anonymous=True)
    cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=10)

def line():
    vel_msg = Twist()
    
    vel_msg.linear.x = 0.3
    _move_wheels(3, vel_msg)

def square():
    # Start new node
    rospy.init_note('robot_twist', anonymous=True)
    vel_msg = Twist()
    
    vel_msg.linear.x = 0.3
    _move_wheels(3, vel_msg)

    for i in range(1,4)

	vel_msg = Twist()

	vel_msg.angular.x = 1,57*i
	_move_wheels(1, vel_msg)

	vel_msg = Twist()
    
	vel_msg.linear.x = 0.3
	_move_wheels(3, vel_msg)


def triangle():
    # Start new node
    rospy.init_note('robot_twist', anonymous=True)
    vel_msg = Twist()
    
    vel_msg.linear.x = 0.3
    _move_wheels(3, vel_msg)

    for i in range(1,3)

	vel_msg = Twist()

	vel_msg.angular.x = 1,05*i
	_move_wheels(1, vel_msg)

	vel_msg = Twist()
    
	vel_msg.linear.x = 0.3
	_move_wheels(3, vel_msg)


def _move_wheels(time, twist):
    """Move wheels for 'time' with 'twist'.

    :type twist: Twist
    """
    num = int(time / self.CMD_VEL_TIME_FACTOR)

    for _ in range(num):
	velocity_publisher.publish(twist)
	rospy.sleep(self.CMD_VEL_TIME_FACTOR)

    # stop
    velocity_publisher.publish(Twist())

if __name__ == '__main__':
    move()
