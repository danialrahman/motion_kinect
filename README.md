# Motion Kinectic
Moving a ROS Turtlebot3 using KinectV2 skeleton data.

It is tested and able to move the Turtlebot3 from a a simple gesture to move the Turtlebot3 foward, rotate left and right by reading the tf position published by the kinect_tracker. Movement of the robot are published using cmd_vel to ROS robots.

## Installation

- [Install libfreenect2](https://github.com/OpenKinect/libfreenect2/)
  - Make sure to install all the optional stuff, including **OpenCL** and **OpenNI2**
  - When you build the library, do not follow the instructions there, instead run
    ```bash
    mkdir build && cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=/usr/
    make
    sudo make install
    ```


  
- [Install motion_kinect](https://github.com/danialrahman/motion_kinect)
  - Clone motion_kinect to catkin_ws/src
    ```bash
    $ roscd && cd ../src
    $ git clone https://github.com/danialrahman/motion_kinect.git
    ```
  - Change `TURTLEBOT_IP` & `REMOTE_IP` variables in `/launch/kinect_t3_motion.sh`
  
  - Source setup.bash in the `motion_kinect` directory to link the base directory and NiTE to .ros directories 
    ```bash
    $ source setup.bash
    ```
  - Build
    ```bash
    $ roscd && cd ../
    $ catkin_make -j8
    ```

## Turtlebot3 Launch
- Switch on Turtlebot3 and make sure it can be access by the remote PC through SSH
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
    - `Cross hand:` Terminate
    
   - Press 0: Quit ROS launch and terminate RVIZ
