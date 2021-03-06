# An example world, not doing much but extending the base class and logging events

import core
from util import *
import pygame as pg

# Always named State for consistency
class State(core.State):
    def __init__(self,surface=None):
        super().__init__(surface)
        self.event.on("event",lambda e : print(e))

if __name__ == "__main__":
    pg.init()
    state = State()
    state.loop()
