import Location
import Model

class Core:
    def __init__(self, model1, model2, Location):
        self.location = Location
        self.items = {0 : model1, 1 : model2}
        self.end = False
        self.countDown = 100
        self.model1 = model1
        self.model2 = model2
        self.model1.hp = 100
        self.model2.hp = 100
        self.items[0].x = 200
        self.items[0].y = 100
        self.items[1].x = 1100
        self.items[1].y = 99
        self.items[0].flipped = False
        self.items[1].flipped = True
        
        self.keyBindingsDown = {275 : model1.startRunning,
                                276 : model1.startRunningFlip,
                                44 : model1.lightHit,
                                46 : model1.lightKick,
                                
                                97 : model2.startRunningFlip,
                                100 : model2.startRunning,
                                103 : model2.lightHit,
                                104 : model2.lightKick}
        
        self.keyBindingsUp = {275 : model1.stopRunning,
                              276 : model1.stopRunningFlip,
                              
                              97 : model2.stopRunningFlip,
                              100 : model2.stopRunning}
        
    def update(self):
        for key in self.items.keys():
            if self.items[key].dead:
                if self.countDown > 0:
                    self.countDown -= 1
                else:
                    self.end = True                
            self.items[key].update()
            if self.items[key].currentState.name in self.items[key].attackingStates:
                if self.items[key].currentStatePosition in self.items[key].currentState.attackPositions:
                    if self.areIntersected(key):
                        self.items[1 - key].hp -= self.items[key].currentState.damage
                        self.items[1 - key].x -= 5 * [1 if self.items[key].flipped else -1][0]
                        if self.items[1 - key].x > 1500:
                            self.items[1 - key] = 1500
                        if self.items[1 - key].x < 100:
                            self.items = 100
                        print("HP1 :", self.items[0].hp, "   HP2 :", self.items[1].hp)

    def areIntersected(self, hitting):
        if (0 < (self.model1.x + self.model1.width - self.model2.x - 205) and 200 > (self.model1.x + self.model1.width - self.model2.x - 205) and not self.model1.flipped and hitting == 0):
            return True
        elif (0 < (self.model2.x + self.model2.width - self.model1.x - 205) and 200 > (self.model2.x + self.model2.width - self.model1.x - 205) and not self.model2.flipped and hitting == 1):
            return True
        elif (10 < (self.model1.x - self.model2.x) and 190 > (self.model1.x - self.model2.x) and self.model1.flipped and hitting == 0):
            return True
        elif (10 < (self.model2.x - self.model1.x) and 190 > (self.model2.x - self.model1.x) and self.model2.flipped and hitting == 1):
            return True
        
            