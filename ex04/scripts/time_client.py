#! /usr/bin/env python3

import rospy
import actionlib
from ex04.msg import timeAction, timeGoal, timeResult
import time

def client_check_time():
    client = actionlib.SimpleActionClient('time_action', timeAction)
    rospy.loginfo('Waiting for action server...')
    client.wait_for_server()

    ts = time.time()
    goal = timeGoal(time=ts)
    client.send_goal(goal)
    rospy.loginfo ('Goal sent...')

    for i in range (0,10):
        print('Doing something else during while the server doing the processing...')
        rospy.sleep(2)

    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('time_sender')
        result = client_check_time()
        print(result.result_msg)
    except rospy.ROSInterruptException:
        print('program interrupted before completion')

