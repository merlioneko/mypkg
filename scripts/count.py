#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
	n = random.randint(0,100) % 4
	pub.publish(n)
	rate.sleep()

