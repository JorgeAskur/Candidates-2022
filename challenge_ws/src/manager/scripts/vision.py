#! /usr/bin/env python

from unittest import result
import rospy
import actionlib
from manager.msg import watchResult, watchGoal, watchFeedback,watchAction
from geometry_msgs.msg import Pose

#ActionServer
#Recibir una poses
#Simular un tiempo de ejecucion (Delay random i guess)

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

        # if position == position[tag]
        # then say tag matches
        # else say tag doesnt match
        self.a_server.set_succeeded(result)
        
if __name__ == "__main__":
    rospy.init_node('action_server')
    s = ActionServer()
    rospy.spin()