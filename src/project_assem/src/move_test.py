#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import moveit_msgs.msg
from std_msgs.msg import String

def move_robot():
    # Initialisierung
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_robot_script', anonymous=True)

    # Initialisiere den RobotCommander und MoveGroupCommander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "moveit_assem"  # Ersetzen Sie 'moveit_assem' durch den tatsächlichen Gruppenamen
    move_group = moveit_commander.MoveGroupCommander(group_name)
    move_group.set_max_velocity_scaling_factor(1.0)  # Setzen Sie 1.0 für maximale Geschwindigkeit (100%)
    move_group.set_max_acceleration_scaling_factor(1.0)  # Setzen Sie 1.0 für maximale Beschleunigung (100%)

    # Create a DisplayTrajectory ROS publisher for Rviz
    display_trajectory_publisher = rospy.Publisher(
        "/move_group/display_planned_path",
        moveit_msgs.msg.DisplayTrajectory,
        queue_size=20,
    )

    # Zielpose für "Pick" definieren
    pick_pose = geometry_msgs.msg.Pose()
    pick_pose.orientation.w = 1.0
    pick_pose.position.x = 2.2
    pick_pose.position.y = 2.1
    pick_pose.position.z = 1.0
    move_group.set_pose_target(pick_pose)

    # Bewegung zum Pick-Punkt planen und ausführen
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    print("reached Pick Position")

    # Objekt greifen (Attach)
    grasp_object(robot, move_group, scene)

    print("grasped object")

    # Zielpose für "Place" definieren
    place_pose = geometry_msgs.msg.Pose()
    place_pose.orientation.w = 1.0
    place_pose.position.x = 3.0
    place_pose.position.y = 1.2
    place_pose.position.z = 2.0
    move_group.set_pose_target(place_pose)
    move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden

    # Bewegung zum Place-Punkt planen und ausführen
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    print("Reached Place Position")

    # Objekt ablegen (Detach)
    release_object(move_group, scene)
    print("Object released")

    # Herunterfahren
    moveit_commander.roscpp_shutdown()

def add_object(scene):
    # Fügen Sie hier den Code hinzu, um das Objekt an das Werkzeug zu "attachen"
    # Zum Beispiel eine Box als Platzhalter für das Objekt hinzufügen und anhängen
    box_name = "object"
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = move_group.get_end_effector_link()
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = 0.1  # Höhe relativ zum Endeffektor
    scene.add_box(box_name, box_pose, size=(0.05, 0.05, 0.05))

    # Warten, bis die Box in der Szene hinzugefügt wurde
    rospy.sleep(1)

    # Anhängen der Box an den Roboter
    eef_link = move_group.get_end_effector_link()
    touch_links = robot.get_link_names(group=move_group.get_name())
    scene.attach_box(eef_link, box_name, touch_links=touch_links)


def grasp_object(robot, move_group, scene):
    # Definiere den Namen des Objekts
    box_name = "object"

    # Position des Objekts in der Welt (angepasst an die tatsächliche Position in Ihrer Simulation)
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "world"  # Oder ein anderer Referenzrahmen, z.B. das Förderband
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.x = 2.2  # Setzen Sie die tatsächlichen Koordinaten des Objekts
    box_pose.pose.position.y = 2.1
    box_pose.pose.position.z = 0.5  # Höhe über dem Boden oder dem Förderband

    # Objekt zur Szene hinzufügen
    scene.add_box(box_name, box_pose, size=(0.05, 0.05, 0.05))

    # Warten, bis das Objekt in der Szene hinzugefügt wurde
    rospy.sleep(1)

    # # Objekt greifen: Anhängen des Objekts an den Endeffektor
    eef_link = move_group.get_end_effector_link()
    touch_links = robot.get_link_names(group=move_group.get_name())

    # # Anhängen des Objekts
    scene.attach_box(eef_link, box_name, touch_links=touch_links)

    # # Warten, bis das Objekt angehängt wurde
    rospy.sleep(1)


def release_object(move_group, scene):
    # Objekt vom Werkzeug "detachen"
    box_name = "object"
    scene.remove_attached_object(move_group.get_end_effector_link(), name=box_name)

    # Warten, bis die Box entfernt wurde
    rospy.sleep(1)

    # Box aus der Szene löschen
    scene.remove_world_object(box_name)

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
