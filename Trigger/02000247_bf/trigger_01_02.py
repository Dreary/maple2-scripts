""" trigger/02000247_bf/trigger_01_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[401]):
            return 버튼눌림(self.ctx)
        if self.user_detected(box_ids=[405]):
            return 사라짐(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[401]):
            return 대기(self.ctx)
        if self.user_detected(box_ids=[405]):
            return 사라짐(self.ctx)


class 사라짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301])


initial_state = 대기
