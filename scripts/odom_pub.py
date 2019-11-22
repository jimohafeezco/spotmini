#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
import numpy as numpy
import matplotlib.pyplot as plt

# counter =0
def callback(data):
  
    rospy.loginfo("I heard %s", data.orientation.x)
    rospy.loginfo("y is %s",   data.orientation.y)
    rospy.loginfo("z is %s", data.orientation.z)
    rospy.loginfo("w is %s", data.orientation.w)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("spot/imu_data", Imu, callback)

   # plt.ion()
    # plt.show()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':  
    listener()