import Location
import Model

class Core:
    def __init__(self, model1, model2, Location):
        self.location = Location
        self.items = {"pl1" : model1, "pl2" : model2}
        self.items["pl1"].x = 100
        self.items["pl1"].y = 100
        self.items["pl2"].x = 500
        self.items["pl2"].y = 100
        self.items["pl1"].flipped = False
        self.items["pl2"].flipped = True
        for key in self.items.keys():
            self.items[key].visible = True
        
        self.keyBindingsDown = {275 : model1.startRunning,
                                276 : model1.startRunningFlip,
                                44 : model1.lightHit,
                                46 : model1.lightKick,
                                
                                97 : model2.startRunningFlip,
                                100 : model2.startRunning}
        
        self.keyBindingsUp = {275 : model1.stopRunning,
                              276 : model1.stopRunningFlip,
                              
                              97 : model2.stopRunningFlip,
                              100 : model2.stopRunning}
        
    def update(self):
        for key in self.items.keys():
            self.items[key].update()
            