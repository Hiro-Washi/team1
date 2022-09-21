#!/usr/bin/env python3
# -*- cofing: utf-8 -*-
import rospy as rp
import actionlib as al

from master_common import enter_room_ac####
tts_srv = rp.ServiceProxy('/tts', StrTrg)
wave_srv = rp.ServiceProxy('/waveplay_srv', StrTrg)

def speak(data): tts_srv(data)
def wavePlay(data): wave_srv(data)

# g:float32/velo,dist rs:bool/result fb:string/state,float32/dist
def enterRoom(dist_msg, velo_msg):
    rp.loginfo('Start "EnterRoomAC"')
    er_ac = al.SimpleActionClient('enter_room_ac',EnterRoomAction)
    er_ac.wait_for_server()
    goal.dist = dist_msg
    goal.velo = velo_msg

# g:location rs:bool/result fb:string/state
def navi(location_msg):

def searchLocation
