execute_process(COMMAND "/home/fhtw_user/catkin_ws/src/fhtw/ROD/build/moveit/moveit_core/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/fhtw_user/catkin_ws/src/fhtw/ROD/build/moveit/moveit_core/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
