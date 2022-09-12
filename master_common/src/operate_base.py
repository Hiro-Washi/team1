#!/usr/bin/env python3
#-*- coding: utf -*-
import numpy as np, math
import rospy as r
import tf
from geometry_msgs.msg import Twist, PoseStamped
from std_msgs.msg import 
from nav_msgs.msg import Odometry

tar_dist = 0.0
class OperateBase():
    def __init__(self):
        r.init_node('operate_base', True)
        self.rate = r.Rate(50)
        self.twi_pub = r.Publisher('/vmegarover/diff_drive_controller/cmd_vel', Twist, queue_size=1)
        self.twi = Twist()


    # Max 0.5m/s
#    def limitVelo(self, in_velo):
#        #out_velo = 0.0
#        if in_velo > 0.5: in_velo = 0.5
#           return in_velo
#    def limitDist(self, in_dist):
#        if in_dist > 3.0: in_dist = 3.0
#           return in_dist
    def goForward(self, dist, velo):
        if velo > 0.5: velo = 0.5
        self.1
        if dist > 3.0: dist = 3.0
        tar_time = dist / velo
        
        self.twist_value.linear.x
