#!/usr/bin/env python3

import rospy
from ex03.srv import my_service, my_serviceResponse

def srv_handler(req):
    print("Returning [%s + %s = %s]"%(req.A, req.B, (req.A + req.B)))
    return my_serviceResponse(req.A + req.B)

def my_server():
    rospy.init_node('my_srv_server')
    s = rospy.Service('addTwoInt_srv', my_service, srv_handler)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    my_server()

