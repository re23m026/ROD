#!/usr/bin/env python3

import rospy
import tf
from geometry_msgs.msg import TransformStamped
import math

def publish_brick_transform():
    rospy.init_node('brick_mover')

    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():

        t = rospy.Time.now().to_sec()
        x = 2 
        y = 2
        z = 2.1
        
        br.sendTransform((x, y, z), 
                         tf.transformations.quaternion_from_euler(0, 0, 0), 
                         rospy.Time.now(), 
                         "brick/brick", 
                         "world")

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_brick_transform()
    except rospy.ROSInterruptException:
        pass
