#!/usr/bin/env python3

import sys
import rospy
from ex03.srv import my_service

def my_client(a, b):
    rospy.wait_for_service('addTwoInt_srv')
    try:
        myservice = rospy.ServiceProxy('addTwoInt_srv', my_service)
        resp1 = myservice(a, b)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Error: %s"%e)

def usage():
    return "%s [a b]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(a, b))
    print("%s + %s = %s"%(a, b, my_client(a, b)))

