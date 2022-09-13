#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import rospy as r
import actionlib as al
from

class EnterRoomAS():
    self.sas = actionlib.SimpleActionServer('enter_room_ac', EnterRoomAction, execute_cb(), False); self.sas.start()
    self.move = 

    def execute_cb(self, goal):
        
