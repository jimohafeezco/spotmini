
# import rospy
# # ROS Image message
# from sensor_msgs.msg import Image
# # ROS Image message -> OpenCV2 image converter
# from cv_bridge import CvBridge, CvBridgeError
# # OpenCV2 for saving an image
# import cv2
# import matplotlib.pyplot as plt

# # Instantiate CvBridge
# # bridge = CvBridge()

# def image_callback(msg):
#     # rospy.loginfo(msg.data)
#     plt.imread(msg.data)
#     plt.show()
#     plt.pause(10)
 
# def main():
#     rospy.init_node('image_listener')
#     # Define your image topic
#     image_topic = "/spot/camera1/image_raw"
#     # Set up your subscriber and define its callback
#     rospy.Subscriber(image_topic, Image, image_callback)
#     # Spin until ctrl + c
#     rospy.spin()

# if __name__ == '__main__':
#     main()

print(4)