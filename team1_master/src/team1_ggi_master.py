#!/usr/bin/env python3
#-*- conding: utf-8 -*-
import rospy as rp, smach as sm
from enter_room.srv import EnterRoom
from happymimi_navigation.srv import NaviLocation
from ggi_voice
from ggi_graphics

class Enter(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = ['enter_done'])
		self.er = rp.Proxy('/enter_room_server', EnterRoom)
	def execute(self, userdata):
		result = self.er(1.0, 0.3).result
		if result: return 'enter_done'
        else:######

class Train(smach.State):
	def __init__(self):
		sm.State.__init__(self, outcomes = ['train_done'])
		self.train = rp.ServiceProxy('/ggi_training_phase',Empty)
	def execute(self, userdata):
		rp.loginfo('Executing state')
		self.train()
		return 'train_done'

### if
class SetPosition(sm.State):
	def __init__(self):
		sm.State.__init__(self, outcomes = ['sp_done'])
		self.navi_srv = rp.ServiceProxy('/navi_location_server',NaviLocation)
		self.
	def execute(sm.State):
		rp.loginfo('Executing state: SET POSITION')


class Learn(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = ['learn_done'])
        self.learn_srv = rp.ServiceProxy('/test_phase',GgiLearning)
    def execute(self, userdata):
		rospy.loginfo('Executing state: LEARN')
        self.learn_srv()
		return 'learn_done'

class Listen(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = []
                              input_key = ['lc_count_in'])
    # 3 times
    def execute(self, userdata):
        rp.loginfo('Executing state: LISTEN')
        lc = userdata.lc_count_in
        
        if lc

#class SetPosition(sm.State):
#	def __init__(self):
#		sm.State.__init__(self, outcomes = ['sp_done')

class Test(sm.State):
    def __init__(self):
        sm.State.__init__(self, outcomes = [])
	def execute(self, userdata):
		rp.loginfo('Executing state: TEST')

def main():
    sm0 = sm.StateMachine(outcomes = ['succeeded','aborted','preempted']
    sm0.userdata.listen_count = 0
    with sm0:
        sm.StateMachine.add('ENTER', Enter(),
                            transitions = {'enter_done':'LEARN'})
        sm.StateMachine.add('LEARN', Learn(),
                            transitions = {'learn_done':'SET_POSITION'}
                            remapping = {'lc_in':'listen_count'})
        sm.StateMachine.add('LISTEN', Listen(),
                            transitions = {'':''}
							remapping)
        sm.StateMachine.add('LEARN', Learn(),
                            transitions = {''})
        sm.StateMachine.add('LEARN', Learn(),
                            transitions = {''})
    outcomes = sm0.execute()


if __name__ == '__main__':
    rp.init_node('team1_ggi_master')
    main()

