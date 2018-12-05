#!/bin/sh
# VARIABLES
TURTLEBOT_IP="192.168.1.2"
REMOTE_IP="192.168.1.1"


# TURTLEBOT3 REMOTE BRINGUP & KINECTV2 LAUNCH
echo ""
echo "-------------------------------------------------"
echo ""

# TURTLEBOT3 ROBOT BRINGUP
gnome-terminal --tab -e "sshpass -p napelturbot ssh turtlebot3@$TURTLEBOT_IP -t 'source ~/catkin_ws/devel/setup.bash; export ROS_MASTER_URI=http://$REMOTE_IP:11311; export ROS_HOSTNAME=$TURTLEBOT_IP; roslaunch turtlebot3_bringup turtlebot3_robot.launch'"
echo "Bringing Up Turtlebot3 Robot..."
sleep 5 

echo ""
echo "-------------------------------------------------"
echo ""

# RVIZ LAUNCH
gnome-terminal -e "rviz -d motion_kinect/rviz/kinect2_tracker.rviz &"
echo "Launching RVIZ..."
sleep 2 

echo ""
echo "-------------------------------------------------"
echo ""

echo "Kinect2 tracker ready!"

echo ""
echo "--------------------------------------------------------------"
echo ""
while true; do
    read -p "Move(1); Quit(0): " yn
    case $yn in
        [0] ) 
		killall -9 rosmaster; 
		killall -9 rviz; 
		break;;
        [1] ) 
		# MOTION TF READER LAUNCH
		gnome-terminal --tab -e "roslaunch motion_kinect tf_reader.launch";
		echo "Motion reader launched!";
		sleep 2;;
        * ) ;;
    esac
done






