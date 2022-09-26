#!/usr/bin/env python3
from manager.srv import getObject,getObjectResponse
import rospy

OBJECT_DICT = {
    '12345': 'Arduino',
    '22453': 'Puente H',
    '31512': 'Motor',
    '62232': 'LED',
}

def handle_getObject(req):
    if req.id in OBJECT_DICT:
        return getObjectResponse(OBJECT_DICT[req.id])
    else: return "Not Found"

def getObject_server():
    rospy.init_node('getObject_server')
    s = rospy.Service('getObject', getObject, handle_getObject)
    rospy.spin()

if __name__ == "__main__":
    getObject_server()