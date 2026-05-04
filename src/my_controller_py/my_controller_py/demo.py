import rclpy,math
from rclpy.node import Node
from sensor_msgs.msg import JointState
class N(Node):
 def __init__(self):
  super().__init__('n')
  self.p=self.create_publisher(JointState,'/joint_states',10)
  self.t=0
  self.create_timer(0.05,self.cb)
 def cb(self):
  self.t+=0.05
  m=JointState()
  m.header.stamp=self.get_clock().now().to_msg()
  m.name=['j1','j2','j3']
  m.position=[math.sin(self.t),-0.5,0.5]
  self.p.publish(m)
def main():
 rclpy.init();rclpy.spin(N())
