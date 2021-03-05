# Game
import pygame as pg
import time

from observer import Observer
from util import *

class State(object):

    def __init__(self,surface=None):
        self.size = (800,500)
        if surface == None:
            self.screen  = pg.display.set_mode(self.size)
        else:
            self.screen = surface

        self.running = True
        
        self.event = Observer()
        self.event.on("update",self.get_events)
        self.event.on("event",gate(self.quit,type=pg.QUIT))

    def quit(self):
        self.running = False
        self.event.fire("quit")
    
    def loop(self):
        now = time.time()
        previous = now
        while self.running:
            now = time.time()
            delta = now - previous

            self.event.fire("update",delta)

            previous = now

    def get_events(self,delta):
        for e in pg.event.get():
            self.event.fire("event",e)

if __name__ == "__main__":
    state = State()
    state.loop()
