#!/usr/bin/env python3
# -*- cofing: utf-8 -*-
import rospy as r
import actionlib as al
from master_common import e
tts_srv = rospy.ServiceProxy('/tts', StrTrg)
wave_srv = rospy.ServiceProxy('/waveplay_srv', StrTrg)

def speak(data):
    tts_srv(data)
def wavePlay(data):
    wave_srv(data)
def enterRoom(dist_msg, velo_msg):
    r.loginfo('Start "EnterRoomAC"')
    er_ac = al.SimpleActionClient('enter_room_ac',EnterRoomAction)
    er_ac.wait_for_server()
    goal.dist = dist_msg
    goal.velo = velo_msg
    
