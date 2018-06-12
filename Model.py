import Object
from State import State

class Model(Object.Object):
    def __init__(self, imagebox, name, x=0, y=0, isvisible = False):
        Object.Object.__init__(self, imagebox, 24, 32, name)
        self.rightBorder = self.image.get_rect()[2]
        print(self.rightBorder)
        self.visible = isvisible
        self.flipped = False
        self.states = dict()
        self.states["Standing"] = State(["Standing", 2, [5, 5], 0, 0])
        self.states["Running"] = State(["Running", 2, [1, 1], 0, self.height])
        self.states["LightHit"] = State(["LightHit", 3, [2, 2], 0, self.height * 2])
        self.currentState = State(self.states["Standing"].returnCopy())
        self.currentStatePosition = 0
        self.speed = 0
        
    def update(self):
        if self.currentState.ticks[self.currentStatePosition] > 0:
            self.currentState.ticks[self.currentStatePosition] -= 1
        else:
            self.x += self.speed
            if self.flipped:
                self.currentState.cropCoordinateX = self.rightBorder - ((self.currentStatePosition * self.width + self.width) % (self.width * self.currentState.positionCount + 1))
            else:
                self.currentState.cropCoordinateX = (self.currentState.cropCoordinateX + self.width) % (self.width * self.currentState.positionCount)
            
            self.currentState.ticks[self.currentStatePosition] = self.states[self.currentState.name].ticks[self.currentStatePosition]
            self.currentStatePosition = (self.currentStatePosition + 1) % self.states[self.currentState.name].positionCount
        
        self.blitx = self.currentState.cropCoordinateX
        self.blity = self.currentState.cropCoordinateY
        
    def startRunning(self):
        self.currentState = State(self.states["Running"].returnCopy())
        self.speed = 4
        self.currentStatePosition = 0
        self.flipped = False
        
    def startRunningFlip(self):
        self.currentState = State(self.states["Running"].returnCopy())
        self.speed = -4
        self.currentState.cropCoordinateX = self.rightBorder - self.width
        self.currentStatePosition = 0
        self.flipped = True   
    
    def stopRunning(self):
        if self.currentState.name == "Running":
            self.currentState = State(self.states["Standing"].returnCopy())
            self.currentState.cropCoordinateX = 0
            self.currentStatePosition = 0
            self.speed = 0
            
    def stopRunningFlip(self):
        if self.currentState.name == "Running" and self.flipped:
            self.currentState = State(self.states["Standing"].returnCopy())
            self.currentState.cropCoordinateX = self.rightBorder - self.width
            self.currentStatePosition = 0
            self.speed = 0    