"""Launch an example driver that communicates using TCP"""

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    container = launch_ros.actions.ComposableNodeContainer(
        name='novatel_gps_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            launch_ros.descriptions.ComposableNode(
                package='novatel_gps_driver',
                namespace='lexus3/gps/nova',
                plugin='novatel_gps_driver::NovatelGpsNode',
                name='novatel_gps',
                parameters=[{
                    'connection_type': 'tcp',
                    'device': '192.168.10.12:3001',
                    'verbose': False,
                    'imu_sample_rate': -1.0,
                    'use_binary_messages': True,
                    'publish_novatel_positions': False,
                    'publish_imu_messages_': True,
                    'publish_novatel_utm_positions': True,
                    'publish_imu_messages': True,
                    'publish_novatel_velocity': False,
                    'publish_novatel_psrdop2': False,
                    'imu_frame_id': '/lexus3/nova/imu',
                    'frame_id': '/lexus3/gps/nova',
                    'publish_novatel_dual_antenna_heading': True,
                    'x_coord_offset': -697237.0, # map_gyor_0
                    'y_coord_offset': -5285644.0, # map_gyor_0
                }]
            )
        ],
        output='screen'
    )

    return LaunchDescription([container])
