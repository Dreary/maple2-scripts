""" 11000040: Rovey """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000020$
            # - Everyone wants to join the Royal Guard, but very few are actually qualified. It is imperative that Royal Guard members be strong in body and spirit, for we are the Empress's last line of defense. Hmm, I must admit, you do seem fairly strong.
            return 1
        elif index == 1:
            # functionID=1
            # $script:0831180610000021$
            # - We're always looking for great swordsmen with the strength to protect the Empress and her palace. How'd you like to join the Royal Guard?
            return -1
        return -1
