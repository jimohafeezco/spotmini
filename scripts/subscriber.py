#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
import numpy as numpy
import matplotlib.pyplot as plt

# counter =0
def callback(data):
    # global counter
  
    rospy.loginfo("I heard %s", data.linear_acceleration.x)
    rospy.loginfo("y is %s",  data.linear_acceleration.y)
    rospy.loginfo("z is %s",data.linear_acceleration.x)
    # rospy.spin()
        # plt.plot(data.linear_acceleration.y, data.linear_acceleration.x)
        # plt.draw()
        # plt.pause(0.000001)
    # counter +=1
    
def listener():
    # counter =0

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("spot/imu_data", Imu, callback)
    # plt.ion()
    # plt.show()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':  
    listener()