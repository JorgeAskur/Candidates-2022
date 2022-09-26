#! /usr/bin/env python3

from unittest import result
import rospy
import actionlib
from manager.msg import talkAction, talkFeedback, talkResult
#ActionServer
#Recibir una string
#Actualizar el estado del sistema (ok, not ok)

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "talk_to", talkAction, execute_cb=self.execute_cb,auto_start=False)
        self.a_server.start()
        pass

    def execute_cb(self, goal):
        
        feedback = talkFeedback()
        result = talkResult()
        
        result.status = goal.text
        feedback.progress = "State is changed."
        self.a_server.publish_feedback(feedback)
        
        self.a_server.set_succeeded(result)
        
if __name__ == "__main__":
    rospy.init_node('speech_server')
    s = ActionServer()
    rospy.spin()