""" trigger/99999841/boss_hp.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(var_id=200) == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=911, is_relative=True) <= 70:
            return 프로70(self.ctx)


class 프로70(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=210, value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=911, is_relative=True) <= 50:
            return 프로50(self.ctx)


class 프로50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=220, value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=911, is_relative=True) <= 30:
            return 프로30(self.ctx)


class 프로30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=230, value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=911, is_relative=True) <= 10:
            return 프로10(self.ctx)


class 프로10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dungeon_variable(var_id=240, value=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
