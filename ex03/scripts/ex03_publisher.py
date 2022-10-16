#!/usr/bin/env python3
import rospy
from ex03.msg import my_message

def publisher():
    pub = rospy.Publisher('ex03_topic', my_message, queue_size=10)
    rate = rospy.Rate(1)
    msg2send = my_message()
    counter = 0

    while not rospy.is_shutdown():
        string2send = "Publishing %d"%counter
        counter += 1

        msg2send.data = string2send
        msg2send.counter = counter
        pub.publish(msg2send)

        rospy.loginfo(string2send)
        rate.sleep()

if __name__ == "__main__":
    rospy.init_node("my_publisher")
    publisher()
