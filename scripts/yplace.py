#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

n = 0
y = 0
def cb(message):
    global n 
    n = message.data 

rospy.init_node('yplace')
sub = rospy.Subscriber('count_up', Int32,cb)
pub = rospy.Publisher('yplace', Int32,queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    if n == 2:
     y += 1
    if n == 3:
     y -= 1
    str = "y ... %d" %y
    rospy.loginfo(str)
    pub.publish(y)
    rate.sleep()

