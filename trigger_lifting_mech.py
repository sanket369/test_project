#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from move_base_msgs.msg import MoveBaseActionResult

def move_base_result_callback(data):
    if data.status.status == 3 and data.status.text == "Goal reached.":
        # Publish the message on the /lifting_mech topic
        lifting_mech_pub.publish(1)

if __name__ == '__main__':
    rospy.init_node('lifting_mech_publisher')

    # Create a publisher for the /lifting_mech topic
    lifting_mech_pub = rospy.Publisher('/lifting_mech', Int32, queue_size=20)

    # Subscribe to the /move_base/result topic
    move_base_result_sub = rospy.Subscriber('/move_base/result', MoveBaseActionResult, move_base_result_callback)

    rospy.spin()
