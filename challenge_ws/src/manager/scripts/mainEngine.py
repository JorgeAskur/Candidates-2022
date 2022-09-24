#! /usr/bin/env python

from http import client
from unittest import result
import rospy
import actionlib
from geometry_msgs.msg import Pose
from manager.msg import navigateAction, navigateGoal, talkGoal, talkAction

pose2send = Pose()

pose2send.position.x = 1
pose2send.position.y = 0
pose2send.position.z = 1

'''
def feedback_cb_nav(msg):
    print("Feedback recieved: ", msg)


def call_server_nav():
    client = actionlib.SimpleActionClient('navigate_to', navigateAction)
    client.wait_for_server()

    goal = navigateGoal()
    goal.target_pose = pose2send

    client.send_goal(goal,feedback_cb=feedback_cb_nav)

    client.wait_for_result()

    result = client.get_result()

    return result
    
'''

def feedback_cb(msg):
    print(msg)

def call_server_speech():
    client = actionlib.SimpleActionClient('talk_to', talkAction)
    client.wait_for_server()

    goal = talkGoal()
    goal.text = "System is ok"

    client.send_goal(goal,feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

if __name__ == '__main__':
    try:
        rospy.init_node('action_client')
        #result = call_server_nav()
        result = call_server_speech()
        print("The result is", result)
    except rospy.ROSInterruptException as e:
        print("Something went wrong: ", e)