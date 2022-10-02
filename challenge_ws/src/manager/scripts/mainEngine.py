#! /usr/bin/env python3

from http import client
from unittest import result
import rospy
import actionlib
from geometry_msgs.msg import Pose
from manager.msg import navigateAction, navigateGoal, talkGoal, talkAction, lockersAction, lockersFeedback, lockersResult, lockersGoal, watchAction, watchFeedback, watchResult, watchGoal
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
    print("Time left: ", msg.time_left)


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
    print(msg.progress)


def call_server_speech():
    client = actionlib.SimpleActionClient('talk_to', talkAction)
    client.wait_for_server()

    goal = talkGoal()
    goal.text = "Moving"

    client.send_goal(goal,feedback_cb=feedback_cb_speech)

    client.wait_for_result()

    result = client.get_result()

    return result.status

def feedback_cb_store(msg):
    print(msg.lockers_opened)

def call_server_store(target):
    client = actionlib.SimpleActionClient('locker_system', lockersAction)
    client.wait_for_server()

    goal = lockersGoal()
    goal.target_locker = target

    client.send_goal(goal,feedback_cb=feedback_cb_store)

    client.wait_for_result()

    result = client.get_result()

    return result.done

def feedback_cb_vision(msg):
    print(msg.check)

def call_server_vision(name, position):
    client = actionlib.SimpleActionClient('watches', watchAction)
    client.wait_for_server()

    goal = watchGoal()
    goal.tag = name
    goal.pose = position

    client.send_goal(goal,feedback_cb=feedback_cb_store)

    client.wait_for_result()

    output = client.get_result()

    return output.result

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
        go = input("Quieres Abrir/Cerrar un casillero: ")
        if go == '1':
            try:
                objeto = input("Que buscas? (ID): ")
                #getObject
                name = getObject_client(objeto)
                
                if name != "Not Found":
                    #Speech
                    talk_result = call_server_speech()
                    print("New State:", talk_result)

                    #getTarget
                    location = getTarget_client(name)

                    #Vision
                    vision = call_server_vision(name,location)
                    print(vision)

                    #Navigtion
                    nav_result = call_server_nav(location)

                    #Store
                    store_result = call_server_store(location)
                    print("Finished:", store_result)
                else:
                    print("ID: " + objeto + " does not exist.")

            except rospy.ROSInterruptException as e:
                print("Something went wrong: ", e)
        elif go == 'q':
            break