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
    group_name = "moveit_shift"  # Ersetzen Sie 'moveit_assem' durch den tatsächlichen Gruppenamen
    move_group = moveit_commander.MoveGroupCommander(group_name)
    
    # Geschwindigkeit setzen
    move_group.set_max_velocity_scaling_factor(1.0)  
    move_group.set_max_acceleration_scaling_factor(1.0)  
    
    # Box hinzufügen
    add_object(scene, -0.854457, 0.43213, 0.3, "box_1")
    add_object(scene, -0.854457, 0.43213+0.4, 0.3, "box_2")
    add_object(scene, -0.854457, 0.43213+0.8, 0.3, "box_3")
    add_object(scene, -0.854457-0.3, 0.43213, 0.3, "box_4")
    add_object(scene, -0.854457-0.3, 0.43213+0.4, 0.3, "box_5")
    add_object(scene, -0.854457-0.3, 0.43213+0.8, 0.3, "box_6")


    # Zielpose für "Pick" definieren
    move_group.set_named_target("pre_pick")
    move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden
    
    # Bewegung zum Pick-Punkt planen und ausführen
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    print("reached Pick Position")
    rospy.sleep(2)

    # Zielpose für "Pick" definieren
    move_group.set_named_target("pick")
    move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden
    
    
    # Bewegung zum Place-Punkt planen und ausführen
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    print("Reached Place Position")
    rospy.sleep(2)

    # Objekt greifen (Attach)
    grasp_object(robot, move_group, scene, "box_1")
    print("grasped object")

    move_group.set_named_target("pre_pick")
    move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden
    
    # Bewegung zum Pick-Punkt planen und ausführen
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    rospy.sleep(2)

    move_group.set_named_target("pre_place")
    move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden
    
    # Bewegung zum Pick-Punkt planen und ausführen
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    rospy.sleep(2)

    move_group.set_named_target("place")
    move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden
    
    # Bewegung zum Pick-Punkt planen und ausführen
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    rospy.sleep(2)

    # Objekt ablegen (Detach)
    release_object(move_group, scene, "box_1")
    print("Object released")

    move_group.set_named_target("pre_place")
    move_group.set_planning_time(10)  # Setze die Planungszeit auf 10 Sekunden
    
    # Bewegung zum Pick-Punkt planen und ausführen
    move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    rospy.sleep(2)

    grasp_object(robot, move_group, scene, "box_2")

    # Herunterfahren
    moveit_commander.roscpp_shutdown()

def grasp_object(robot, move_group, scene, name):
    # Fügen Sie hier den Code hinzu, um das Objekt an das Werkzeug zu "attachen"
    # Zum Beispiel eine Box als Platzhalter für das Objekt hinzufügen und anhängen
    box_name = name
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = move_group.get_end_effector_link()
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = 0.2  # Höhe relativ zum Endeffektor
    scene.add_box(box_name, box_pose, size=(0.2, 0.2, 0.2))

    # Warten, bis die Box in der Szene hinzugefügt wurde
    rospy.sleep(1)

    # Anhängen der Box an den Roboter
    eef_link = move_group.get_end_effector_link()
    touch_links = robot.get_link_names(group=move_group.get_name())
    scene.attach_box(eef_link, box_name, touch_links=touch_links)


def add_object(scene, x, y, z, name):
    # Definiere den Namen des Objekts
    box_name = name

    # Position des Objekts in der Welt (angepasst an die tatsächliche Position in Ihrer Simulation)
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "world"  # Oder ein anderer Referenzrahmen, z.B. das Förderband
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.x = x  # Setzen Sie die tatsächlichen Koordinaten des Objekts
    box_pose.pose.position.y = y
    box_pose.pose.position.z = z  # Höhe über dem Boden oder dem Förderband

    # Objekt zur Szene hinzufügen
    scene.add_box(box_name, box_pose, size=(0.2, 0.2, 0.2))

    # Warten, bis das Objekt in der Szene hinzugefügt wurde
    rospy.sleep(1)

    # # Warten, bis das Objekt angehängt wurde


def release_object(move_group, scene, name):
    # Objekt vom Werkzeug "detachen"
    box_name = name

    # Box zu World attachen

    scene.remove_attached_object(move_group.get_end_effector_link(), name=box_name)

    # Warten, bis die Box entfernt wurde
    rospy.sleep(1)

    # Box aus der Szene löschen
    # scene.remove_world_object(box_name)

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
