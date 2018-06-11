import Object
from State import State

class Model(Object.Object):
    def __init__(self, imagebox, name, x=0, y=0, isvisible = False):
        Object.Object.__init__(self, imagebox, 24, 32, name)
        self.visible = isvisible
        self.flipped = False
        self.states = dict()
        self.states["Standing"] = State("Standing", 2, [6, 6], 0, 0)
        self.currentState = State("Standing", 2, [6, 6], 0, 0)
        self.currentStatePosition = 0
        
    def update(self):
        if self.currentState.ticks[self.currentStatePosition] > 0:
            self.currentState.ticks[self.currentStatePosition] -= 1
        else:
            self.currentState.cropCoordinateX = (self.currentState.cropCoordinateX + self.width) % (self.width * self.currentState.positionCount)
            self.currentState.ticks[self.currentStatePosition] = self.states[self.currentState.name].ticks[self.currentStatePosition]
            self.currentStatePosition = (self.currentStatePosition + 1) % self.states[self.currentState.name].positionCount            
        
        self.blitx = self.currentState.cropCoordinateX
        self.blity = self.currentState.cropCoordinateY