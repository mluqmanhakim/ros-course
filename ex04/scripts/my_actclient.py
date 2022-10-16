#! /usr/bin/env python3

import rospy
import actionlib
from ex04.msg import my_actionAction, my_actionGoal, my_actionResult

def cnt_client():
    client = actionlib.SimpleActionClient('cnt_action',my_actionAction)
    rospy.loginfo('Waiting for action server...')
    client.wait_for_server()

    goal = my_actionGoal(cnt = 10)
    print(goal)
    client.send_goal(goal)
    rospy.loginfo ('Goal sent...')
    # if we want a blocking type of communication then we need to use:
    # client.wait_for_result()

    for cnt_idx in range (0,10):
        print('Doing something else during while the server doing the processing...')
        rospy.sleep(2)

    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('mycounter_ac')
        result = cnt_client()
        rospy.loginfo(result.result_msg)
    except rospy.ROSInterruptException:
        print('program interrupted before completion')

