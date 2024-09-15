#!/usr/bin/env python3
import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from tf2_msgs.msg import TFMessage
from nav_msgs.msg import Odometry

def pose_callback(msg):
    br = tf2_ros.TransformBroadcaster()

    t = TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = "europalette/base_link"
    
    t.transform.translation.x = msg.pose.pose.position.x
    t.transform.translation.y = msg.pose.pose.position.y
    t.transform.translation.z = msg.pose.pose.position.z
    
    t.transform.rotation.x = msg.pose.pose.orientation.x
    t.transform.rotation.y = msg.pose.pose.orientation.y
    t.transform.rotation.z = msg.pose.pose.orientation.z
    t.transform.rotation.w = msg.pose.pose.orientation.w
    
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('pub_europalette_pose')

    rospy.Subscriber('/europalette/tf', Odometry, pose_callback)
    
    rospy.spin()
