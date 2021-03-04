# Game
import pygame as pg
from observer import Observer
import time

pg.init()
screen = pg.display.set_mode((800,500))

class State(object):

    def __init__(self,surface=None):
        if surface == None:
            self.screen  = pg.display.set_mode((800,500))
        else:
            self.screen = surface

        self.running = True
        
        self.sprites = pg.sprite.Group()
        
        self.event = Observer()
        self.event.on("update",self.get_events)
        self.event.on("update",self.render)
    
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
            print(e)
            self.event.fire("event",e)
            if e.type == pg.QUIT:
                self.quit()
    
    def render(self,delta):
        self.screen.fill((0,0,0))
        pg.draw.circle(screen,(255,0,255),(400,250),100,5)
        pg.display.flip()

state = State()
state.loop()
