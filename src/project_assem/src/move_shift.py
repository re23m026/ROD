#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import moveit_msgs.msg
from moveit_commander import PlanningSceneInterface
from moveit_msgs.msg import CollisionObject
from shape_msgs.msg import SolidPrimitive
from std_msgs.msg import Header
from std_msgs.msg import String
import rospkg
import os
from tf.transformations import quaternion_from_euler

def add_mesh_object(scene, x, y, z, roll, pitch, yaw, name, mesh_path):
    
    # Definiere den Namen des Objekts
    mesh_name = name

    # Position des Objekts in der Welt (angepasst an die tatsächliche Position in Ihrer Simulation)
    mesh_pose = geometry_msgs.msg.PoseStamped()
    mesh_pose.header.frame_id = "world"  # Oder ein anderer Referenzrahmen, z.B. das Förderband
    mesh_pose.pose.position.x = x  # Setzen Sie die tatsächlichen Koordinaten des Objekts
    mesh_pose.pose.position.y = y
    mesh_pose.pose.position.z = z  # Höhe über dem Boden oder dem Förderband

    # Setze die Orientierung mithilfe von Roll, Pitch, Yaw (in Radiant)
    q = quaternion_from_euler(roll, pitch, yaw)
    mesh_pose.pose.orientation.x = q[0]
    mesh_pose.pose.orientation.y = q[1]
    mesh_pose.pose.orientation.z = q[2]
    mesh_pose.pose.orientation.w = q[3]

    # Mesh zur Szene hinzufügen
    scene.add_mesh(mesh_name, mesh_pose, mesh_path)

    # Warten, bis das Mesh in der Szene hinzugefügt wurde
    rospy.sleep(1)




def move_robot():
    # Initialisierung
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_robot_script', anonymous=True)

    # Initialisiere den RobotCommander und MoveGroupCommander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "moveit_shift"  
    move_group = moveit_commander.MoveGroupCommander(group_name)
    
    # Geschwindigkeit setzen
    move_group.set_max_velocity_scaling_factor(1.0)  
    move_group.set_max_acceleration_scaling_factor(1.0)  
    
    # Euro-Palette hinzufügen
    rospack = rospkg.RosPack()
    mesh_file_path = os.path.join(rospack.get_path('environment'), 'meshes', 'europalette', 'Europoolpalette_scaled.stl')
    
    # Position (x, y, z) und Orientierung (roll, pitch, yaw in Radiant)
    add_mesh_object(scene, -0.854457-0.15, 0.43213+0.3, 0.1, 0.0, 0.0, 1.57, "europalette", mesh_file_path)  

    # Conveyor
    rospack = rospkg.RosPack()
    mesh_file_path = os.path.join(rospack.get_path('environment'), 'meshes', 'conveyor', 'conveyor_simple.stl')
    
    # Position (x, y, z) und Orientierung (roll, pitch, yaw in Radiant)
    add_mesh_object(scene, 1.0, 0.0, -0.5, 1.57, 0.0, 1.57, "conveyor_1", mesh_file_path)  
    add_mesh_object(scene, 1.0, -1.0, -0.5, 1.57, 0.0, 1.57, "conveyor_2", mesh_file_path)  
    add_mesh_object(scene, 1.0, -2.0, -0.5, 1.57, 0.0, 1.57, "conveyor_3", mesh_file_path) 
    add_mesh_object(scene, 1.0, -3.0, -0.5, 1.57, 0.0, 1.57, "conveyor_4", mesh_file_path) 
    add_mesh_object(scene, 1.4, 0.0, -0.5, 1.57, 0.0, 1.57, "conveyor_5", mesh_file_path)  
    add_mesh_object(scene, 1.4, -1.0, -0.5, 1.57, 0.0, 1.57, "conveyor_6", mesh_file_path) 
    add_mesh_object(scene, 1.4, -2.0, -0.5, 1.57, 0.0, 1.57, "conveyor_7", mesh_file_path) 
    add_mesh_object(scene, 1.4, -3.0, -0.5, 1.57, 0.0, 1.57, "conveyor_8", mesh_file_path)  


    # Box hinzufügen
    add_object(scene, -0.854457, 0.43213, 0.35, "box_1")
    add_object(scene, -0.854457, 0.43213+0.3, 0.35, "box_2")
    add_object(scene, -0.854457, 0.43213+0.6, 0.35, "box_3")
    add_object(scene, -0.854457-0.3, 0.43213, 0.35, "box_4")
    add_object(scene, -0.854457-0.3, 0.43213+0.3, 0.35, "box_5")
    add_object(scene, -0.854457-0.3, 0.43213+0.6, 0.35, "box_6")


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
