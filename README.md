# ros-motion_kinect
Moving a ROS Turtlebot3 using KinectV2 skeleton data.

It is tested and able to move the Turtlebot3 from a a simple gesture to move the Turtlebot3 foward, rotate left and right by reading the tf position published by the kinect_tracker. Movement of the robot are published using cmd_vel to ROS robots.

## Installation

- [Install kinect2_tracker](https://github.com/mcgi5sr2/kinect2_tracker)
  - Follow through all the installation @ [https://github.com/mcgi5sr2/kinect2_tracker](https://github.com/mcgi5sr2/kinect2_tracker)
  - Make sure you have installed [libfreenet2](https://github.com/OpenKinect/libfreenect2/), [NiTE2 & OpenNI2](https://autostudentsite.wordpress.com/2017/05/18/running-and-building-nite2-samples-for-kinect-v2/) and all the dependencies
  
- [Install motion_kinect](https://github.com/danialrahman/motion_kinect)
  - Clone motion_kinect to catkin_ws/src
    ```bash
    $ roscd && cd ../src
    $ git clone https://github.com/danialrahman/motion_kinect.git
    ```
  - Change `TURTLEBOT_IP` & `REMOTE_IP` variables in `kinect_t3_motion.sh`
  
  - Link motion_kinect directory to .ros
    ```bash
    $ roscd motion_kinect
    $ sudo ln -s "$(pwd)" ~/.ros/motion_kinect
    ```
  - Build
    ```bash
    $ roscd && cd ../
    $ catkin_make
    ```

## Turtlebot3 Launch
- Launch `turtlebot3_motion`

  ```bash
  $ roslaunch motion_kinect turtlebot3_motion.launch
  ```
 - Once the terminal output `Kinect2 tracker ready!` it will prompt for `Move(1); Quit(0):`;
 
  - Press 1: Start moving the Turtlebot3 with your hand gesture
    - `Both left and right hand not raised:` Stopping
    - `Left hand raised:` Turn left
    - `Right hand raised:` Turn right
    - `Both left and right hand raised:` Move foward
    
   - Press 0: Quit ROS launch and terminate RVIZ
