FROM ubuntu:14.04
MAINTAINER Strigidaeinsomnie

RUN apt-get update && \
    apt-get install -y wget apt-file && \

#---------------- Edit repository

    apt-file update && \
    apt-file search add-apt-repository && \
    apt-get install -y software-properties-common && \
    add-apt-repository universe && \
    add-apt-repository multiverse && \
    add-apt-repository restricted && \

#---------------- Install ROS


    sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list' && \
    wget http://packages.ros.org/ros.key -O - | sudo apt-key add - && \
    apt-get update && \

    apt-get install -y ros-indigo-desktop && \
    rosdep init && \
    rosdep update && \
    echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc && \
    source ~/.bashrc && \
    apt-get install -y python-rosinstall && \

#---------------- Install Rospeex

    mkdir -p ~/catkin_ws/src && \
    cd ~/catkin_ws/src && \
    catkin_init_workspace && \
    cd ~/catkin_ws && \
    catkin_make_isolated && \
    source devel_isolated/setup.bash && \
    cd ~/catkin_ws/src && \
    git clone https://bitbucket.org/rospeex/rospeex.git && \
    rosdep update && \
    rosdep install -y --from-paths ~/catkin_ws/src/rospeex --ignore-src && \
    cd ~/catkin_ws && \
    catkin_make_isolated
