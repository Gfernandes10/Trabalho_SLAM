#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Empty
from std_msgs.msg import String


# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):
    
    if data.buttons[0] == 1:
        rospy.loginfo("iniciou %s")
        pub.publish()
        # takeoff.publish({})
        

        



# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    
    pub = rospy.Publisher('/ardrone/takeoff',Empty,queue_size=10)

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2Dronetakeoff')
    rospy.spin()

if __name__ == '__main__':
    start()