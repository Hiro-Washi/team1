#!/usr/bin/env python3
#-*- conding: utf-8 -*-
import rospy as rp, smach as sm



class Enter(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = ['finish'])
    def execute(self, userdata):


class Learning(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = [])
    def execute(self, )

class Test
    def __init__(self):
        sm.State.__init__(self, outcomes = [])

def main():
    sm0 = sm.StateMachine(outcomes = ['succeeded','aborted','preempted']

    with sm0:
        
