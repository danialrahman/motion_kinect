#!/usr/bin/env python  
import roslib
import rospy
import tf
import geometry_msgs.msg
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('motion_tf_reader')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (transRight,rotRight) = listener.lookupTransform('/kinect/user_1/neck', '/kinect/user_1/right_hand', rospy.Time(0))
	    transRightX = transRight[0]
	    transRightY = transRight[1]
	    transRightZ = transRight[2]

	    rotRightX = rotRight[0]
	    rotRightY = rotRight[1]
	    rotRightZ = rotRight[2]
	    rotRightW = rotRight[3]


	    (transLeft,rotLeft) = listener.lookupTransform('/kinect/user_1/neck', '/kinect/user_1/left_hand', rospy.Time(0))
	    transLeftX = transLeft[0]
	    transLeftY = transLeft[1]
	    transLeftZ = transLeft[2]

	    rotLeftX = rotLeft[0]
	    rotLeftY = rotLeft[1]
	    rotLeftZ = rotLeft[2]
	    rotLeftW = rotLeft[3]


	    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
            vel_msg = Twist()
	    vel_msg.linear.x = 0
	    vel_msg.linear.y = 0
	    vel_msg.linear.z = 0
	    vel_msg.angular.x = 0
	    vel_msg.angular.y = 0
	    vel_msg.angular.z = 0
	    speed = 0.15
	    speedAngular = 0.5
	    


	    if(transRightY > 0 and transLeftY > 0):
		print("Straight")
	        vel_msg.linear.x = speed
	    elif(transRightY > 0):
		print("Turn Right")
	    	vel_msg.angular.z = -speedAngular
	    elif(transLeftY > 0):
		print("Turn Left")
	    	vel_msg.angular.z = speedAngular
	    elif(transLeftX >= 0 and transRightX <= 0):
		print("Terminate")
	    	vel_msg.linear.x = 0
	    	vel_msg.linear.y = 0
	    	vel_msg.linear.z = 0
	    	vel_msg.angular.x = 0
	    	vel_msg.angular.y = 0
	    	vel_msg.angular.z = 0
		break
	    else:
		print("Stop")
	    	vel_msg.linear.x = 0
	    	vel_msg.linear.y = 0
	    	vel_msg.linear.z = 0
	    	vel_msg.angular.x = 0
	    	vel_msg.angular.y = 0
	    	vel_msg.angular.z = 0

	   
	    velocity_publisher.publish(vel_msg)

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rate.sleep()
