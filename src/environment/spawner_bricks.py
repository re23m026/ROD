#!/usr/bin/env python3
import rospy
import os
import rospkg
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from nav_msgs.msg import Odometry

class BrickPaketSpawner:
    def __init__(self):
        rospy.init_node('spawn_bricks_relative_to_europalette')

        # Wait for the Gazebo service to be available
        rospy.wait_for_service('/gazebo/spawn_urdf_model')
        self.spawn_model = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)

        # Subscribe to the europalette tf topic
        rospy.Subscriber("/europalette/tf", Odometry, self.europalette_callback)

        # Initialize europalette pose and orientation
        self.europalette_pose = Pose()

        # Flag to ensure that the brick package is only spawned once
        self.brick_paket_spawned = False

    def europalette_callback(self, data):
        # Extract pose and orientation from the europalette /tf topic
        self.europalette_pose = data.pose.pose

        # Spawn the brick package relative to the europalette's position and orientation
        self.spawn_brick_paket()

    def spawn_brick_paket(self):
        # Check if the brick package has already been spawned
        if not self.brick_paket_spawned:

            # Get the path to the URDF file for the brick package
            rospack = rospkg.RosPack()
            urdf_path = os.path.join(rospack.get_path('environment'), 'urdf', 'brick_paket.urdf')

            # Read the URDF file
            with open(urdf_path, 'r') as urdf_file:
                brick_paket_urdf = urdf_file.read()

            # Set the position relative to the europalette
            brick_paket_pose = Pose()
            brick_paket_pose.position.x = self.europalette_pose.position.x
            brick_paket_pose.position.y = self.europalette_pose.position.y
            brick_paket_pose.position.z = self.europalette_pose.position.z + 0.2  # Adjust height above the europalette

            # Use the europalette's orientation (in quaternion form)
            orientation_q = self.europalette_pose.orientation
            orientation_euler = euler_from_quaternion([orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w])

            # Use the same orientation for the brick package as the europalette
            brick_orientation_q = quaternion_from_euler(orientation_euler[0], orientation_euler[1], orientation_euler[2])

            brick_paket_pose.orientation.x = brick_orientation_q[0]
            brick_paket_pose.orientation.y = brick_orientation_q[1]
            brick_paket_pose.orientation.z = brick_orientation_q[2]
            brick_paket_pose.orientation.w = brick_orientation_q[3]

            try:
                # Call the Gazebo service to spawn the brick package
                self.spawn_model("brick_paket", brick_paket_urdf, '', brick_paket_pose, 'world')
                rospy.loginfo("Spawned brick_paket over the europalette.")
                self.brick_paket_spawned = True  # Ensure it spawns only once
            except rospy.ServiceException as e:
                rospy.logerr(f"Failed to spawn brick_paket: {e}")

if __name__ == '__main__':
    try:
        spawner = BrickPaketSpawner()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
