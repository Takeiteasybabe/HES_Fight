import Object
from State import State

class Model(Object.Object):
    def __init__(self, imagebox, name, x=0, y=0, isvisible = False):
        Object.Object.__init__(self, imagebox, 24, 32, name)
        self.rightBorder = self.image.get_rect()[2]
        self.health = 100
        self.visible = isvisible
        self.flipped = False
        self.states = dict()
        self.states["Standing"] = State(["Standing", 2, [5, 5], 0, 0])
        self.states["Running"] = State(["Running", 2, [1, 1], 0, self.height])
        self.states["LightHit"] = State(["LightHit", 3, [1, 2, 1], 0, self.height * 2, [1], 5])
        self.states["LightKick"] = State(["LightKick", 3, [2, 2, 1], 0, self.height * 3, [1], 7])
        self.currentState = State(self.states["Standing"].returnCopy())
        self.cyclingStates = set(["Standing", "Running"])
        self.attackingStates = set(["LightHit", "LightKick"])
        self.currentStatePosition = 0
        self.speed = 0
        
    def update(self):       
        if self.currentState.ticks[self.currentStatePosition] > 0:
            self.currentState.ticks[self.currentStatePosition] -= 1
        else:
            self.currentStatePosition += 1
            if self.currentState.name in self.cyclingStates or self.currentStatePosition <= self.currentState.positionCount - 1:
                self.currentStatePosition %= self.states[self.currentState.name].positionCount
                self.x += self.speed
                #print(self.currentState.name, self.currentState.cropCoordinateX, self.currentStatePosition)
                if self.flipped:
                    self.currentState.cropCoordinateX = self.rightBorder - ((self.currentStatePosition * self.width + self.width) % (self.width * (self.currentState.positionCount + 1)))
                else:
                    self.currentState.cropCoordinateX = (self.currentState.cropCoordinateX + self.width) % (self.width * self.currentState.positionCount)
            else:
                self.currentState = State(self.states["Standing"].returnCopy())
                self.currentStatePosition = 0
                self.currentState.cropCoordinateX = (self.rightBorder - self.width) * self.flipped
                
            self.currentState.ticks[self.currentStatePosition] = self.states[self.currentState.name].ticks[self.currentStatePosition] - 1
            
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
        if self.currentState.name == "Running" and not self.flipped:
            self.currentState = State(self.states["Standing"].returnCopy())
            self.currentState.cropCoordinateX = (self.rightBorder - self.width) * self.flipped
            self.currentStatePosition = 0
            self.speed = 0
            
    def stopRunningFlip(self):
        if self.currentState.name == "Running" and self.flipped:
            self.currentState = State(self.states["Standing"].returnCopy())
            self.currentState.cropCoordinateX = (self.rightBorder - self.width) * self.flipped
            self.currentStatePosition = 0
            self.speed = 0    
            
    def lightHit(self):
        if self.currentState.name in self.cyclingStates:
            self.speed = 0
            self.currentState = State(self.states["LightHit"].returnCopy())
            self.currentState.cropCoordinateX = (self.rightBorder - self.width) * self.flipped  
            self.currentStatePosition = 0
            gamestats = open("last game.txt", 'r')
            hits, kicks = map(int, gamestats.read().split())
            gamestats.close()
            open("last game.txt", 'w').close()
            hits += 1
            hits, kicks = str(hits), str(kicks)
            gamestats = open("last game.txt", 'w')
            gamestats.write(" ".join([hits, kicks]))
            gamestats.close()
            
        
    def lightKick(self):
        if self.currentState.name in self.cyclingStates:
            self.speed = 0
            self.currentState = State(self.states["LightKick"].returnCopy())
            self.currentState.cropCoordinateX = (self.rightBorder - self.width) * self.flipped  
            self.currentStatePosition = 0
            gamestats = open("last game.txt", 'r')
            hits, kicks = map(int, gamestats.read().split())
            gamestats.close()
            open("last game.txt", 'w').close()
            kicks += 1
            hits, kicks = str(hits), str(kicks)
            gamestats = open("last game.txt", 'w')
            gamestats.write(" ".join([hits, kicks]))
            gamestats.close()
