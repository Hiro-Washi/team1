#!/usr/bin/env python3
#-*- conding: utf-8 -*-
import rospy as rp, smach as sm

from enter_room.srv import EnterRoom

from ggi_voice
from ggi_graphics

class Enter(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = ['enter_done'])
	self.er = rp.Proxy('/enter_room_server', EnterRoom)
    def execute(self, userdata):
	result = self.er(1.0, 0.3).result
	if result:
	    return 'enter_done'	
        else:#######

class Learn(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = [])
        self.learn_srv = rp.ServiceProxy('/test_phase',GgiLearning)
    def execute(self, userdata):
        self.learn_srv()

class Listen(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = [])
    def execute(self, ):

class Test
    def __init__(self):
        sm.State.__init__(self, outcomes = [])

def main():
    sm0 = sm.StateMachine(outcomes = ['succeeded','aborted','preempted']

    with sm0:
        sm.StateMachine.add('ENTER',Enter(),
                            transitions = {''})

if __name__ == '__main__':
    rp.init_node('team1_ggi_master')
    main()

