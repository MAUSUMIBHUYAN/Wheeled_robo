import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random
import math
import time

class RandomMove(Node):
    def __init__(self):
        super().__init__('random_move')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.move_random)  # every 1 sec

    def move_random(self):
        msg = Twist()

        # Random linear velocity (forward/backward)
        msg.linear.x = random.uniform(0.0, 1.0)

        # Random angular velocity (turning)
        msg.angular.z = random.uniform(-1.0, 1.0)

        self.publisher.publish(msg)
        self.get_logger().info(f"Moving with linear={msg.linear.x:.2f}, angular={msg.angular.z:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = RandomMove()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
