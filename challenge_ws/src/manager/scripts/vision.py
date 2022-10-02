#! /usr/bin/env python3

from unittest import result
import rospy
import actionlib
from manager.msg import watchResult, watchGoal, watchFeedback, watchAction
from geometry_msgs.msg import Pose
from manager.srv import *
#ActionServer
#Recibir una poses
#Simular un tiempo de ejecucion (Delay random i guess)

def getInfo_client(name, position):
    rospy.wait_for_service('getInfo')
    try:
        getInfo1 = rospy.ServiceProxy('getInfo', getInfo)
        resp = getInfo1(name, position)

        return resp

    except rospy.ServiceException as e:
        print("Something went wrong: ", e)

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "watches", watchAction, execute_cb=self.execute_cb,auto_start=False)
        self.a_server.start()
        pass

    def execute_cb(self, goal):
        feedback = watchFeedback()
        result = watchResult()
        position = goal.pose
        tag = goal.tag
        feedback.check = "Checking.."
        result = getInfo_client(tag, position)
        self.a_server.set_succeeded(result)
        
if __name__ == "__main__":
    rospy.init_node('action_server')
    s = ActionServer()
    rospy.spin()