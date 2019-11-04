#!/usr/bin/env python 
import numpy as np
from matplotlib import pyplot as plt
import rospy
from sensor_msgs.msg import Imu

def plot_x(msg):
    global counter
    if counter % 10 == 0:
        stamp = msg.header.stamp
        time = stamp.secs + stamp.nsecs * 1e-9
        plt.plot(msg.linear_acceleration.y, msg.linear_acceleration.y)
        # plt.axis("equal")
        # plt.draw()
        plt.pause(0.00000000001)

    counter += 1

if __name__ == '__main__':
    counter = 0

    rospy.init_node("plotter")
    rospy.Subscriber("spot/imu_data", Imu, plot_x)
    # plt.ion()
    plt.show()
    rospy.spin()