import Location
import Model

class Core:
    def __init__(self, model1, Location):
        self.location = Location
        self.items = {"pl1" : model1}
        self.items["pl1"].x = 100
        self.items["pl1"].y = 500
        self.items["pl1"].flipped = False
        for key in self.items.keys():
            self.items[key].visible = True
        
        self.keyBindingsDown = {275 : model1.startRunning}
        
        self.keyBindingsUp = {275 : model1.stopRunning}
        
    def update(self):
        for key in self.items.keys():
            self.items[key].update()
            