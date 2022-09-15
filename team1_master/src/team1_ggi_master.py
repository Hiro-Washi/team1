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
        sm.State.__init__(self, outcomes = []
                              input_key = ['lc_count_in'])
    # 3 times
    def execute(self, userdata):
        rp.loginfo('Executing state: LISTEN')
        lc = userdata.lc_count_in
        
        if lc

class Test(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = [])

def main():
    sm0 = sm.StateMachine(outcomes = ['succeeded','aborted','preempted']
    sm0.userdata.listen_count = 0
    with sm0:
        sm.StateMachine.add('ENTER', Enter(),
                            transitions = {''})
        sm.StateMachine.add('LEARN', Learn(),
                            transitions = {''}
                            remapping = {'lc_in':'listen_count'})
        sm.StateMachine.add('LISTEN', Listen(),
                            transitions = {''})
        sm.StateMachine.add('LEARN', Learn(),
                            transitions = {''})
        sm.StateMachine.add('LEARN', Learn(),
                            transitions = {''})
    outcomes = sm0.execute()


if __name__ == '__main__':
    rp.init_node('team1_ggi_master')
    main()

