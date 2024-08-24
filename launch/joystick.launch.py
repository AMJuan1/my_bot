from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess


def generate_launch_description():

    joy_params = os.path.join(get_package_share_directory('my_bot'),'config','joystick.yaml')

    joy_node = Node(
            package='joy',
            executable='joy_node',
            parameters=[joy_params],
         )
    
    teleop_drive_node = Node(
            package='teleop_twist_joy', 
            executable='teleop_node',
            name = 'teleop_drive_node',
            parameters=[joy_params],
            remappings=[('/cmd_vel', '/diff_cont/cmd_vel_unstamped')]
            )
    
    joy_teleop_node = Node(
            package='joy_teleop',
            executable='joy_teleop',
            name='joy_teleop_node',
            parameters=[joy_params],
            remappings=[('/camera_cmd', '/camera_joint/velocity_controller/command')]
            )
    
    servo_server_client = ExecuteProcess(
        cmd=['python3', '/home/ubuntu-dev/dev_ws/src/my_bot/launch/servo_client_2.py'],  # Replace with the correct path to servo_server.py
        output='screen'
    )
#...

# And add to launch description at the bottom

    return LaunchDescription([
        servo_server_client,
        joy_node,
        teleop_drive_node,
        joy_teleop_node       
    ])