#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import click     

def moving_publisher():
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    moving_msg = Twist()
    speed = 2
    t = 2

    while not rospy.is_shutdown():
        cmd = click.getchar()
        click.echo()

        if cmd == "w":
            moving_msg.linear.x = speed
            moving_msg.linear.y = 0
            moving_msg.linear.z = 0
            moving_msg.angular.x = 0
            moving_msg.angular.y = 0
            moving_msg.angular.z = 0

        elif cmd == "s":
            moving_msg.linear.x = -speed
            moving_msg.linear.y = 0
            moving_msg.linear.z = 0
            moving_msg.angular.x = 0
            moving_msg.angular.y = 0
            moving_msg.angular.z = 0

        elif cmd == "a":
            t = 1
            moving_msg.linear.x = 0
            moving_msg.linear.y = 0
            moving_msg.linear.z = 0
            moving_msg.angular.x = 0
            moving_msg.angular.y = 0
            moving_msg.angular.z = 2

        elif cmd == "d":
            t = 1
            moving_msg.linear.x = 0
            moving_msg.linear.y = 0
            moving_msg.linear.z = 0
            moving_msg.angular.x = 0
            moving_msg.angular.y = 0
            moving_msg.angular.z = -2

        elif cmd == " ":
            moving_msg.linear.x = 0
            moving_msg.linear.y = 0
            moving_msg.linear.z = 0
            moving_msg.angular.x = 0
            moving_msg.angular.y = 0
            moving_msg.angular.z = 0

        t0 = rospy.Time.now().to_sec()
        cur_t = 0
        while(cur_t <= t):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_t = t1 - t0

        moving_msg.linear.x = 0
        moving_msg.linear.y = 0
        vel_publisher.publish(moving_msg)
        


if __name__ == "__main__":
    rospy.init_node("rm_mf5jdy")
    moving_publisher()
