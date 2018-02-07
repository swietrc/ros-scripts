#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry



class RobotMove:
    DRIVE_SPEED = 0.2
    DRIVE_SPEED_FACTOR = 0.80
    ROT_SPEED = 0.5
    ROT_SPEED_FACTOR = 0.5
    CMD_VEL_TIME_FACTOR = 0.625
    
    # Start new node
    rospy.init_node('robot_twist', anonymous=True) 
    cmd_vel = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10) 
    # odom = rospy.Subscriber('/odom', Odometry, cb)

    def cb(self, data):
        print(data.pose.pose.orientation)

    def line(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0.3
        self._move_wheels(2, vel_msg)

    def _move_wheels(self, time, twist):
        """Move wheels for 'time' with 'twist'.

        :type twist: Twist
        """
        num = int(time / self.CMD_VEL_TIME_FACTOR)

        for _ in range(num):
            self.cmd_vel.publish(twist)
            rospy.sleep(self.CMD_VEL_TIME_FACTOR)

        # stop
        self.cmd_vel.publish(Twist())

    def _rotate(self, angle, speed=ROT_SPEED):
        """Rotate `angle`."""
        time = abs(angle / (speed * self.ROT_SPEED_FACTOR))

        twist = Twist()
        twist.angular.z = math.copysign(speed, angle)
        self._move_wheels(time, twist)

    def square(self):
        # Start new node
        vel_msg = Twist()
        
        vel_msg.linear.x = 0.5
     #   self._move_wheels(2, vel_msg)

        for i in range(1,5):
            self._move_wheels(2, vel_msg)
            self._rotate(math.pi/2)


    def triangle(self):
        # Start new node
        vel_msg = Twist()
        
        vel_msg.linear.x = 0.5
    #   self._move_wheels(2, vel_msg)

        for i in range(1,3):
           # self._rotate((math.pi*2)/3)
            self._move_wheels(2, vel_msg)
            self._rotate((math.pi*2)/3)


if __name__ == '__main__':
    mv = RobotMove()
    mv.square()
