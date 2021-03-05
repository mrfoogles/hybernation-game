
class Observer(object):

    def __init__(self):
        self.listeners = {}
    
    def on(self,event,fn):
        if event in self.listeners:
            self.listeners[event].append(fn)
        else:
            self.listeners[event] = [fn]
    
    def fire(self,event,*args):
        if event in self.listeners:
            for fn in self.listeners[event]:
                fn(*args)
    
    def remove(self,event,fn):
        if event in self.listeners:
            self.listeners[event].remove(fn)
        else:
            raise Exception(f"Tried to remove {event}: {fn}, but that connection does not exist.")
