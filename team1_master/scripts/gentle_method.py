#!/usr/bin/env python3
# -*- cofing: utf-8 -*-
import rospy as r
import actionlib as al


def enterRoom(dist_msg, velo_msg)
    r.loginfo('Start "EnterRoomAC"')
    er_ac = al.SimpleActionClient('enter_room_ac',EnterRoomAction)
    er_ac.wait_for_server()
    goal.dist = dist_msg
    goal.velo = velo_msg
    
