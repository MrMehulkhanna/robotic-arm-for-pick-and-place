from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
import os
def generate_launch_description():
 p=get_package_share_directory('my_robot_description')
 urdf=Path(os.path.join(p,'urdf','arm.urdf')).read_text()
 return LaunchDescription([
  Node(package='robot_state_publisher',executable='robot_state_publisher',parameters=[{'robot_description':urdf}]),
  Node(package='my_controller_py',executable='demo_sequence'),
  Node(package='rviz2',executable='rviz2')
 ])
