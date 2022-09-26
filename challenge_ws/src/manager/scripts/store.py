#! /usr/bin/env python3

from unittest import result
import rospy
import actionlib
from std_msgs.msg import UInt16
from geometry_msgs.msg import Pose
from manager.msg import lockersAction, lockersFeedback, lockersResult
#ActionServer
#Recibir una string
#Actualizar el estado del sistema (ok, not ok)

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

lockers = [definePose(1,1,1,0,0,0,0), definePose(0,1,1,0,0,0,0), definePose(1,1,2,0,0,0,0), definePose(0,1,2,0,0,0,0)]

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "locker_system",lockersAction, execute_cb=self.execute_cb,auto_start=False)
        self.a_server.start()
        pass

    def execute_cb(self, goal):
        
        feedback = lockersFeedback()
        result = lockersResult()
        target = goal.target_locker
        index = lockers.index(target)
        feedback.lockers_opened = "Opening locker " + str(index)

        self.a_server.publish_feedback(feedback)

        pub = rospy.Publisher('locker_open', UInt16, queue_size=10)
        pub.publish(index)
        result.done = True
        self.a_server.set_succeeded(result)
        
if __name__ == "__main__":
    rospy.init_node('store_server')
    s = ActionServer()
    rospy.spin()