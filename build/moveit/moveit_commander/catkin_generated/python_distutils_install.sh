#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/fhtw_user/catkin_ws/src/fhtw/ROD/src/moveit/moveit_commander"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/fhtw_user/catkin_ws/src/fhtw/ROD/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/fhtw_user/catkin_ws/src/fhtw/ROD/install/lib/python3/dist-packages:/home/fhtw_user/catkin_ws/src/fhtw/ROD/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/fhtw_user/catkin_ws/src/fhtw/ROD/build" \
    "/usr/bin/python3" \
    "/home/fhtw_user/catkin_ws/src/fhtw/ROD/src/moveit/moveit_commander/setup.py" \
    egg_info --egg-base /home/fhtw_user/catkin_ws/src/fhtw/ROD/build/moveit/moveit_commander \
    build --build-base "/home/fhtw_user/catkin_ws/src/fhtw/ROD/build/moveit/moveit_commander" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/fhtw_user/catkin_ws/src/fhtw/ROD/install" --install-scripts="/home/fhtw_user/catkin_ws/src/fhtw/ROD/install/bin"
