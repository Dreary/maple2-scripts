""" trigger/51000001_dg/round_10_skill.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[31001])
        self.set_mesh(trigger_ids=[31002])
        self.set_mesh(trigger_ids=[31003])
        self.set_mesh(trigger_ids=[31004])
        self.set_mesh(trigger_ids=[31005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[110]):
            return 지역랜덤(self.ctx)


class 지역랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[110]):
            return 종료(self.ctx)
        if self.random_condition(weight=20.0):
            self.set_mesh(trigger_ids=[31001], visible=True)
            return A지역(self.ctx)
        if self.random_condition(weight=20.0):
            self.set_mesh(trigger_ids=[31002], visible=True)
            return B지역(self.ctx)
        if self.random_condition(weight=20.0):
            self.set_mesh(trigger_ids=[31003], visible=True)
            return C지역(self.ctx)
        if self.random_condition(weight=20.0):
            self.set_mesh(trigger_ids=[31004], visible=True)
            return D지역(self.ctx)
        if self.random_condition(weight=20.0):
            self.set_mesh(trigger_ids=[31005], visible=True)
            return E지역(self.ctx)


class A지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11001]):
            return 스킬랜덤(self.ctx)


class B지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11002]):
            return 스킬랜덤(self.ctx)


class C지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11003]):
            return 스킬랜덤(self.ctx)


class D지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11004]):
            return 스킬랜덤(self.ctx)


class E지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11005]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='random_buff_box')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[110]):
            return 종료(self.ctx)
        """
        if self.random_condition(weight=20.0): # 소형화 사용 안함
            self.add_buff(box_ids=[199], skill_id=49179081, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        """
        if self.random_condition(weight=40.0):
            # 이속증가
            self.add_buff(box_ids=[199], skill_id=49179051, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=30.0):
            # 무적 20
            self.add_buff(box_ids=[199], skill_id=70000085, level=1, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=15.0):
            # 이속감소 10
            self.add_buff(box_ids=[199], skill_id=49179061, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=15.0):
            # 혼란 10
            self.add_buff(box_ids=[199], skill_id=49179071, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[31001])
        self.set_mesh(trigger_ids=[31002])
        self.set_mesh(trigger_ids=[31003])
        self.set_mesh(trigger_ids=[31004])
        self.set_mesh(trigger_ids=[31005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 시작대기중(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
