#!/usr/bin/env python3
from geometry_msgs.msg import Pose
from manager.srv import getInfo, getInfoResponse
import rospy

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

TARGETS_DICT = {
    'Arduino'  : definePose(1,1,1,0,0,0,0),
    'Puente H' : definePose(0,1,1,0,0,0,0),
    'Motor'    : definePose(1,1,2,0,0,0,0),
    'LED'      : definePose(0,1,2,0,0,0,0),
}

def handle_getInfo(req):
    id = req.name
    location = req.position
    if TARGETS_DICT[id] == location:
        return "The locker is in the correct postion"
    else:
        return "The locker is not in the correct postion"

def getInfo_server():
    rospy.init_node('getInfo_server')
    s = rospy.Service('getInfo', getInfo, handle_getInfo)
    rospy.spin()

if __name__ == "__main__":
    getInfo_server()