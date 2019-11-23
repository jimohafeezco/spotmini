

[![Build Status](https://travis-ci.org/jimohafeezco/spotmini.svg?branch=travis_ci)](https://travis-ci.org/jimohafeezco/spotmini)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://travis-ci.org/jimohafeezco/spotmini.svg?branch=travis_ci)
[![Inline docs](http://inch-ci.org/github/jimohafeezco/spotmini.svg?branch=travis_ci)](http://inch-ci.org/github/jimohafeezco/spotmini)

# Spot

Repository for my Spot Mini projects.

##  Launching in RVIZ

To make spotmini-ros part of your workspace, follow these steps (assuming your workspace is setup following the standard conventions):
```
cd ~/catkin_ws/src
git clone hhttps://github.com/jimohafeezco/spotmini.git
cd ~/catkin_ws
catkin_make
roslaunch spotmini display.launch 

```


## Launching in Gazebo

First be in the catkin workspace root, 

```
i)    catkin_make
ii)   source devel/setup.bash
iii)  roslaunch spotmini display_gazebo.launch 

```


The robot designed has 2DOF of revolute joints on each legs making a total of 8DOF. It also has a prismatic joint on top of its base link with 3DOF in addition to the primatic joint. It can use these sets of links to pick and drop objects and achieve different tasks.

After running the commands above, you can play with the the joint states variables and see the differnt joints moving.




## Pictorial View of Robot in RVIZ
![alt text](/media/image.png)


## Controller for Robot

A control yaml file was written which specify the various PID value for each joints in the robot. This keeps the robor stable in the simulation world.

## Publisher Node for Robot
In other to move the robot, a python script was written to publish joint positions to the controller. This is made possible by publishing to the topic of the joints which is ```/spot/joint10_position_controller/command in this case```. A node name is specified in the python script which is refernced in the launch file so that the robot and the publisher can talk to oe another. 

### Animation for Control Action on Robot in Gazebo
![alt text](/media/robot_move.gif)


### Sensing

Two sensors namely the IMU sensor cand the Camera sensor have been included in the Gazebo model. This sensors subscribes to the robot joint topic and read information from it.

To get Camera Images,run: 
"rosrun image_view image_saver image:=/camera1/image_raw" on the terminal and Images of the camera would be saved automatically in the Gazebo model workspace.
A python script, ```takePhoto.py``` was written as a subscriber node to save the image automatically and the publisher node included in the Gazebo model launch file.

P.S: This work would continually be improved upon and the whole of the robot would move , detect obstacles and change direction of motion.
