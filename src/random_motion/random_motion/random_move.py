import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class StraightMove(Node):
    def __init__(self):
        super().__init__('straight_move')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.move_straight)  # every 1 sec

    def move_straight(self):
        msg = Twist()

        # Constant forward speed
        msg.linear.x = 0.5   # adjust speed (m/s) as per your robot
        msg.angular.z = 0.0  # no rotation → straight line

        self.publisher.publish(msg)
        self.get_logger().info(f"Moving straight with linear={msg.linear.x:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = StraightMove()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
