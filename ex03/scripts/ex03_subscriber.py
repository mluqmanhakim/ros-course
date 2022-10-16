#!/usr/bin/env python3

import rospy
from ex03.msg import my_message

def subscriber():
    sub = rospy.Subscriber('ex03_topic', my_message, cb_func)
    rospy.spin()
    
def cb_func(message):
    string_received = message.data
    counter_received = message.counter
    rospy.loginfo("I received: %d"%counter_received)    

if __name__ == "__main__":
    rospy.init_node("my_subscriber")
    subscriber()

