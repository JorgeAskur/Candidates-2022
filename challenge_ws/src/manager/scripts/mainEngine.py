#! /usr/bin/env python3

from http import client
from unittest import result
import rospy
import actionlib
from geometry_msgs.msg import Pose
from manager.msg import navigateAction, navigateGoal, talkGoal, talkAction, lockersAction, lockersFeedback, lockersResult, lockersGoal
from manager.srv import *

def definePose(x,y,z,ox,oy,oz,q):
    p = Pose()
    p.position.x = x
    p.position.y = y
    p.position.z = z
    p.orientation.x = ox 
    p.orientation.y = oy
    p.orientation.z = oz
    p.orientation.w = q
    return p

def feedback_cb_nav(msg):
    print("Feedback recieved: ", msg)


def call_server_nav(position):
    client = actionlib.SimpleActionClient('navigate_to', navigateAction)
    client.wait_for_server()

    goal = navigateGoal()
    goal.target_pose = position

    client.send_goal(goal,feedback_cb=feedback_cb_nav)

    client.wait_for_result()

    result = client.get_result()

    return result


def feedback_cb_speech(msg):
    print(msg)


def call_server_speech():
    client = actionlib.SimpleActionClient('talk_to', talkAction)
    client.wait_for_server()

    goal = talkGoal()
    goal.text = "Moving"

    client.send_goal(goal,feedback_cb=feedback_cb_speech)

    client.wait_for_result()

    result = client.get_result()

    return result

def feedback_cb_store(msg):
    print(msg)

def call_server_store(target):
    client = actionlib.SimpleActionClient('locker_system', lockersAction)
    client.wait_for_server()

    goal = lockersGoal()
    goal.target_locker = target

    client.send_goal(goal,feedback_cb=feedback_cb_store)

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
                objeto = input("Que buscas? (ID): ")
                #getObject
                name = getObject_client('objeto')
                
                #Speech
                talk_result = call_server_speech()
                print("Speech says:", talk_result)

                #getTarget
                location = getTarget_client(name)

                #Navigtion
                nav_result = call_server_nav(location)

                #Store
                store_result = call_server_store(location)
                print("Storage:", store_result)

            except rospy.ROSInterruptException as e:
                print("Something went wrong: ", e)
        elif go == 'q':
            break