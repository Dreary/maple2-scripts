""" trigger/02000298_bf/door_11.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=211, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3111], visible=True)
        self.set_mesh(trigger_ids=[3112], visible=True)
        self.set_agent(trigger_ids=[9111], visible=True)
        self.set_agent(trigger_ids=[9112], visible=True)
        self.set_agent(trigger_ids=[9113], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[111]):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=211, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3111], fade=5.0)
        self.set_mesh(trigger_ids=[3112], fade=5.0)
        self.set_agent(trigger_ids=[9111])
        self.set_agent(trigger_ids=[9112])
        self.set_agent(trigger_ids=[9113])


initial_state = 시작
