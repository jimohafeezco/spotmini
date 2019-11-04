import rospy
import time
from std_msgs.msg import Float64
import math

def talker():
    pub = rospy.Publisher('/spot/joint10_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i =1.5714

    while not rospy.is_shutdown():
        position = math.sin(i) #in radians not  degrees
        rospy.loginfo(position)
        pub.publish(position)
        i+= 0.1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
