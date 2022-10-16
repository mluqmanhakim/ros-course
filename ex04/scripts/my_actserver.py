#! /usr/bin/env python3

import rospy
import actionlib
from ex04.msg import my_actionAction, my_actionFeedback, my_actionResult

class MyCounter(object):
    _fb = my_actionFeedback()               
    _res = my_actionResult()                
    
    def __init__(self,name):
        self._action_name = name

        self._as = actionlib.SimpleActionServer(self._action_name, my_actionAction, execute_cb= self.exec_cb, auto_start = False)

        self._as.start()
        rospy.loginfo('Action server started...')
        
    def exec_cb(self,goal):
        rate = rospy.Rate(1)
        success = True
        self._fb.cnt_elapsed = 0

        rospy.loginfo('%s is counting to %i with frequency of 1s'%(self._action_name,goal.cnt))

        for cnt_idx in range(0,goal.cnt):
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._as.set_preempted()
                success = False
                break

            self._fb.cnt_elapsed = cnt_idx
            self._as.publish_feedback(self._fb)
            rate.sleep()

        if success:
            self._res.result_msg = 'Successfully completed action'
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._res)        

if __name__ == '__main__':
    rospy.init_node('cnt_action')
    server = MyCounter(rospy.get_name())
    rospy.spin()
    
