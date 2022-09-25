#! /usr/bin/env python

import random
from unittest import result
import rospy
import actionlib
from manager.msg import navigateAction, navigateFeedback, navigateGoal, navigateResult
from geometry_msgs.msg import Pose
#ActionServer
#Recibir una pose
#Simular un tiempo de ejecucion (Delay random i guess)

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "navigate_to", navigateAction, execute_cb=self.execute_cb,auto_start=False)
        self.a_server.start()
        pass

    def execute_cb(self, goal):
        success = False
        time = random.randint(5, 20)
        time_left = time
        feedback = navigateFeedback()
        result = navigateResult()

        for i in range(0, time):
            time_left = time - i
            feedback.time_left = time_left
            self.a_server.publish_feedback(feedback)
            rospy.sleep(1)
        pass
        
        success = True
        result.done = success
        self.a_server.set_succeeded(result)
        
if __name__ == "__main__":
    rospy.init_node('nav_server')
    s = ActionServer()
    rospy.spin()