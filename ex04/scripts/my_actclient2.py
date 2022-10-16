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
    client.send_goal(goal, active_cb=callback_active, feedback_cb=callback_feedback,done_cb=callback_done)
    rospy.loginfo ('Goal sent...')
    # if we want a blocking type of communication then we need to use:
    # client.wait_for_result()

    for cnt_idx in range (0,2):
        print('Doing something else during while the server doing the processing...')
        rospy.sleep(0.5)
    done_intime=client.wait_for_result(rospy.Duration.from_sec(1.0))
    if done_intime:
        result=client.get_result()
        return result.result_msg

    else:
        print('Time is up')
        return -1

def callback_active():
    rospy.loginfo("Action server is processing the goal")

def callback_done(state, result):
    rospy.loginfo("Action server is done. State: %s, result: %s" % (str(state), str(result)))

def callback_feedback(feedback):
    rospy.loginfo("Feedback:%s" % str(feedback))


if __name__ == '__main__':
    try:
        rospy.init_node('mycounter_ac')
        rospy.loginfo(cnt_client())
    except rospy.ROSInterruptException:
        print('program interrupted before completion')

