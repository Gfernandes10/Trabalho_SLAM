#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Empty


# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):
    twist = Twist()
    # vertical left stick axis = andar para frente e para trás eixo x
    twist.linear.x = 0.5*data.axes[1]
    # horizontal left stick axis = andar para direita e para esquerda eixo y
    twist.linear.y = 0.5*data.axes[0]
    # vertical right stick axis = andar para direita e para esquerda eixo y
    twist.linear.z = 0.5*data.axes[4]
    # horizontal right stick axis = turn rate
    twist.angular.z = 0.5*data.axes[3]
    pub.publish(twist)
    if data.buttons[0] == 1:
        pub2.publish()
    if data.buttons[1] == 1:
        pub3.publish()

        



# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub
    global pub2
    global pub3
    pub = rospy.Publisher('/cmd_vel', Twist,queue_size=10)
    pub2 = rospy.Publisher('/ardrone/takeoff',Empty,queue_size=10)
    pub3 = rospy.Publisher('/ardrone/land',Empty,queue_size=10)

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2Drone')
    rospy.spin()

if __name__ == '__main__':
    start()
