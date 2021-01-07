#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

n = 0
x = 0

def cb(message):
    global n 
    n = message.data 

rospy.init_node('xplace')
sub = rospy.Subscriber('count_up', Int32,cb)
pub = rospy.Publisher('xplace', Int32,queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    if n == 0:
     x += 1
    if n == 1:
     x -= 1
    str = "x ... %d" %x
    rospy.loginfo(str)
    pub.publish(x)
    rate.sleep()

