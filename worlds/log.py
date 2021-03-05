# An example world, not doing much but extending the base class and logging events

# Necessary to import files from the parent directory (yes, I tried adding __init__.py files)
# prints 'ImportError: attempted relative import with no known parent package' without this
# from stackoverflow
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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