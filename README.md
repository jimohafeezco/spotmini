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

### Unit Test

Forward Kinematics was implemneted for 6 joints robotic system as a model in FKine.py.

In FKtest.py, some teste cases were tested using the function from FKine and their actual expected values compared with the solution using numpy asserts.
Several test cases can be added to implement thus unit test.
To test this unit test implementation, simply clone thr repository and navigate to script directory where we have the forward kinematics implementation and its unit test. Thereafter from the terminal, run the script using


```python FKtest.py```


### Integration Test


The integration tests is a continuation of the joint movement/control task.
Firstly, from previous task, some joints poitions are published to robot joints. In other to get the actual joint position, an IMU sensor was added to the urdf file as a Gazebo plugin. Thereafter a subscriber was implemneted to determine if actual movement takes place which is determined by reading accelearation information from the robot joint. The integration test confirms if actual movement takes place when some joint positions are published. 


TO test the functionality, first from the terminal we :
1) ```roslaunch spotmini display_gazebo.launch```
Open a new terminal and navigae to the script directory and run:
2) ```python inTest.py```
