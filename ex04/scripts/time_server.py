#! /usr/bin/env python3

import rospy
import actionlib
from ex04.msg import timeAction, timeFeedback, timeResult

class TimeChecking(object):
    def __init__(self,name):
        self._action_name = name
        self._fb = timeFeedback()               
        self._res = timeResult()
        self._as = actionlib.SimpleActionServer(self._action_name, timeAction, execute_cb=self.exec_cb, auto_start=False)
        self._as.start()
        rospy.loginfo('Action server started...')


    def exec_cb(self, goal):
        rate = rospy.Rate(1)
        success = True
        rospy.loginfo('Receiving goal in server')
        rospy.loginfo('%s --- %f'%(self._action_name, goal.time))

        if goal.time % 10 == 0:
            self._fb.feedback = "Yes"
        else:
            self._fb.feedback = "No"

        self._as.publish_feedback(self._fb)
        rate.sleep()

        if success:
            self._res.result_msg = self._fb.feedback
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._res)    

    

if __name__ == '__main__':
    rospy.init_node('time_action')
    server = TimeChecking(rospy.get_name())
    rospy.spin()
    
