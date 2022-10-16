#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def moving_publisher():
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    moving_msg = Twist()
    speed = 2

    moving_msg.linear.z = 0
    
    moving_msg.angular.x = 0
    moving_msg.angular.y = 0
    moving_msg.angular.z = 0

    dist = 2

    while not rospy.is_shutdown():
        moving_msg.linear.x = speed
        moving_msg.linear.y = 0
        t0 = rospy.Time.now().to_sec()
        cur_dist = 0
        while(cur_dist < dist):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_dist = speed * (t1 - t0)

        moving_msg.linear.x = 0
        moving_msg.linear.y = speed
        t0 = rospy.Time.now().to_sec()
        cur_dist = 0
        while(cur_dist < dist):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_dist = speed * (t1 - t0)

        moving_msg.linear.x = -speed
        moving_msg.linear.y = 0
        t0 = rospy.Time.now().to_sec()
        cur_dist = 0
        while(cur_dist < dist):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_dist = speed * (t1 - t0)

        moving_msg.linear.x = 0
        moving_msg.linear.y = -speed
        t0 = rospy.Time.now().to_sec()
        cur_dist = 0
        while(cur_dist < dist):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_dist = speed * (t1 - t0)

        moving_msg.linear.y = 0
        vel_publisher.publish(moving_msg)
        

def moving_publisher_2():
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    moving_msg = Twist()
    speed = 2

    moving_msg.linear.z = 0
    moving_msg.angular.x = 0
    moving_msg.angular.y = 0
    moving_msg.angular.z = 0

    t = 2

    while not rospy.is_shutdown():
        moving_msg.linear.x = speed
        moving_msg.linear.y = 0
        t0 = rospy.Time.now().to_sec()
        cur_t = 0
        while(cur_t <= t):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_t = t1 - t0

        moving_msg.linear.x = 0
        moving_msg.linear.y = speed
        t0 = rospy.Time.now().to_sec()
        cur_t = 0
        while(cur_t <= t):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_t = t1 - t0
        
        moving_msg.linear.x = -speed
        moving_msg.linear.y = 0
        t0 = rospy.Time.now().to_sec()
        cur_t = 0
        while(cur_t <= t):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_t = t1 - t0
        
        moving_msg.linear.x = 0
        moving_msg.linear.y = -speed
        t0 = rospy.Time.now().to_sec()
        cur_t = 0
        while(cur_t <= t):
            vel_publisher.publish(moving_msg)
            t1 = rospy.Time.now().to_sec()
            cur_t = t1 - t0
        
        moving_msg.linear.y = 0
        vel_publisher.publish(moving_msg)
        

if __name__ == "__main__":
    rospy.init_node("moving_publisher")
    moving_publisher_2()
