#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_msgs
import moveit_msgs.msg

def move_shift():
    
    # Initialisierung
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_robot_script', anonymous=True)

    # Initialisiere den RobotCommander und MoveGroupCommander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # Ersetze 'arm' durch den Namen der Move-Gruppe des Roboters
    group_name = "moveit_shift"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    # move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden




    ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
    ## trajectories in Rviz:
    display_trajectory_publisher = rospy.Publisher(
        "/move_group/display_planned_path",
        moveit_msgs.msg.DisplayTrajectory,
        queue_size=20,
    )


    # We can get the name of the reference frame for this robot:
    planning_frame = move_group.get_planning_frame()
    print("============ Planning frame: %s" % planning_frame)

    # We can also print the name of the end-effector link for this group:
    eef_link = move_group.get_end_effector_link()
    print("============ End effector link: %s" % eef_link)


    ## TODO

    #   def go_to_joint_state(self):
    #   def go_to_pose_goal(self):
    #   def plan_cartesian_path(self):
    #   def display_trajectory(self, plan):
    #   def execute_plan(self, plan):
    #   def wait_for_state_update(self, box known, box attached, timeout)
    #   def add_box(self, timeout)
    #   def attach_box(self)
    #   def detach_box(self)

    # Zielpose definieren
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 0.0
    pose_target.position.x = 2.2
    pose_target.position.y = 2.1
    pose_target.position.z = 1.0
    move_group.set_pose_target(pose_target)

    # Bewegung planen und ausführen
    plan = move_group.go(wait=True)

    # Zielpose definieren
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 0.0
    pose_target.position.x = 5.0
    pose_target.position.y = 4.0
    pose_target.position.z = 2.0
    move_group.set_pose_target(pose_target)

    # Bewegung planen und ausführen
    plan = move_group.go(pose_target, wait=True)



    # Ziele löschen
    move_group.stop()
    move_group.clear_pose_targets()

    # Herunterfahren
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        move_shift()
    except rospy.ROSInterruptException:
        pass