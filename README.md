# Spot
Repository for my Spot Mini projects.

##Installation

To make spotmini-ros part of your workspace, follow these steps (assuming your workspace is setup following the standard conventions):
```
cd ~/catkin_ws/src
git clone hhttps://github.com/jimohafeezco/spotmini.git
cd ~/catkin_ws
catkin_make
roslaunch spotmini display.launch 

```

The robot designed has 2DOF of revolute joints on each legs making a total of 8DOF. It also has a prismatic joint on top of its base link with 3DOF in addition to the primatic joint. It can use these sets of links to pick and drop objects and achieve different tasks.

After running the commands above, you can play with the the joint states variables and see the differnt joints moving.



Click below to view the pictorial representation of the robot.
![alt text](https://github.com/jimohafeezco/spotmini/blob/master/Screenshot%20from%202019-10-05%2019-31-24.png
![alt text](/media/robot_move.gif)






P.S: This work would continually be improved upon and the whole of the robot would move , detect obstacles and change direction of motion.
