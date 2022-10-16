#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def subscriber():
    sub = rospy.Subscriber('/turtle1/cmd_vel', Twist, cb_func)
    rospy.spin()
    
def cb_func(message):
    # rospy.loginfo("Here's what was subscribed: %s", message)
    print(message.linear.x)

if __name__ == "__main__":
    rospy.init_node("my_subscriber")
    subscriber()

