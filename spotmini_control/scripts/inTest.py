#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
import numpy as numpy
import matplotlib.pyplot as plt
import unittest
import rostest
from std_msgs.msg import Float64
import math
from FKine import *

class MyTestCase(unittest.TestCase):



    def callback(self, data):
        self.data1 = data.linear_acceleration.x
        self.data2 = data.linear_acceleration.y
        self.data3 = data.linear_acceleration.z

        self.assertNotAlmostEqual(self.data1,0)
        self.assertNotAlmostEqual(self.data2,0)
        self.assertNotAlmostEqual(self.data3,0)

        # rospy.loginfo("I heard %s :", self.data)
 
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("spot/imu_data", Imu, MyTestCase().callback)
    rospy.spin()



if __name__ == '__main__':  
    listener()
    rostest.rosrun("tutorial", "test_code", MyTestCase)
 