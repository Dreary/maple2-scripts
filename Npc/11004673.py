""" 11004673: NPCNAME_11004673_NAME:[F]Event """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0
