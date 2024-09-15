#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_msgs
import moveit_msgs.msg

def move_robot():
    
    # Initialisierung
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_robot_script', anonymous=True)

    # Initialisiere den RobotCommander und MoveGroupCommander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # Ersetze 'arm' durch den Namen der Move-Gruppe des Roboters
    group_name = "moveit_assem"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    # move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden

    # Zielpose definieren
    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 0.0
    pose_target.position.x = 2.2
    pose_target.position.y = 2.1
    pose_target.position.z = 1.0
    move_group.set_pose_target(pose_target)

    # Bewegung planen und ausführen
    plan = move_group.go(wait=True)

    # Ziele löschen
    move_group.stop()
    move_group.clear_pose_targets()

    # Herunterfahren
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass