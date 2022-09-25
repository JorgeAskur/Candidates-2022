#! /usr/bin/env python

from http import client
from unittest import result
import rospy
import actionlib
from geometry_msgs.msg import Pose
from manager.msg import navigateAction, navigateGoal, talkGoal, talkAction
from manager.srv import *

pose2send = Pose()

pose2send.position.x = 1
pose2send.position.y = 0
pose2send.position.z = 1

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


def getTarget_client(objective):
    rospy.wait_for_service('getTarget')
    try:
        getTarget1 = rospy.ServiceProxy('getTarget', getTarget)
        resp = getTarget1(objective)

        return resp.target

    except rospy.ServiceException as e:
        print("Something went wrong: ", e)


def getObject_client(id):
    rospy.wait_for_service('getObject')
    try:
        getObject1 = rospy.ServiceProxy('getObject', getObject)
        resp = getObject1(id)

        return resp.name

    except rospy.ServiceException as e:
        print("Something went wrong: ", e)


if __name__ == '__main__':
    rospy.init_node('main_engine')
    while True:
        go = input("pon algo: ")
        if go == '1':
            try:
                #Navigtion
                #nav_result = call_server_nav()
                #print("Navigation says:", nav_result)

                #Speech
                #talk_result = call_server_speech()
                #print("Speech says:", talk_result)

                #getTarget
                #location = getTarget_client('Arduino')
                #print(location)

                #getObject
                name = getObject_client('31512')
                print(name)

            except rospy.ROSInterruptException as e:
                print("Something went wrong: ", e)
        elif go == 'q':
            break