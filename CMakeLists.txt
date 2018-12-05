cmake_minimum_required(VERSION 2.8.3)
project(motion_kinect)


############### KINECT ##########################################################################################################################
# check c++11 / c++0x
include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
    set(CMAKE_CXX_FLAGS "-std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)
    set(CMAKE_CXX_FLAGS "-std=c++0x")
else()
    message(FATAL_ERROR "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()
##################################################################################################################################################

find_package(catkin REQUIRED COMPONENTS
  rospy
  tf

############### KINECT ##########################################################################################################################
  cmake_modules
  cv_bridge
  geometry_msgs
  image_transport
  kdl_conversions
  roscpp
  roslib
  tf_conversions
  std_msgs
  visualization_msgs
  message_generation
##################################################################################################################################################
)


############### KINECT ##########################################################################################################################
find_package(Eigen REQUIRED)
find_package(cmake_modules REQUIRED)

link_directories(
  ${catkin_LIBRARY_DIRS}
)

include_directories(
    include
    ${catkin_INCLUDE_DIRS}
)

add_message_files(
  DIRECTORY
  msg
  FILES
  user_IDs.msg
  user_points.msg
  bounding_box.msg
)

generate_messages(
    DEPENDENCIES geometry_msgs std_msgs
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES motion_kinect
  CATKIN_DEPENDS cv_bridge geometry_msgs image_transport kdl_conversions roscpp roslib tf tf_conversions visualization_msgs message_runtime
  DEPENDS Eigen
)
##################################################################################################################################################

#catkin_package(
#)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}

############### KINECT ##########################################################################################################################
  ${Eigen_INCLUDE_DIRS}
##################################################################################################################################################

)

############### KINECT ##########################################################################################################################
## Declare a C++ library
add_library(motion_kinect
   src/motion_kinect_node.cpp
)

## Add cmake target dependencies of the library
## as an example, code may need to be generated before libraries
## either from message generation or dynamic reconfigure
# add_dependencies(motion_kinect ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

set(NITE2_DIR ~/.ros/motion_kinect/include/NiTE/)
set(NITE2_LIB ~/.ros/motion_kinect/include/NiTE/Redist/libNiTE2.so)
include_directories(./include/Openni2/)
include_directories(${NITE2_DIR}/Include)
include_directories(./include)
include_directories(${OpenCV_INCLUDE_DIRS}/include)

add_executable(motion_kinect_node src/motion_kinect_node.cpp include/motion_kinect.hpp include/visualization.hpp)
target_link_libraries(motion_kinect_node OpenNI2 ${NITE2_LIB}  ${catkin_LIBRARIES} ${Eigen_LIBRARIES})

add_dependencies(motion_kinect_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS} ${PROJECT_NAME}_generate_messages_cpp)

##################################################################################################################################################
