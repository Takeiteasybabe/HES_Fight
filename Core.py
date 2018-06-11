import Location
import Model

class Core:
    def __init__(self, model1, Location):
        self.location = Location
        self.items = [model1]
        model1.x = 100
        model1.y = 500
        model1.flipped = False
        for i in range(len(self.items)):
            self.items[i].visible = True
        
    def update(self):
        for i in self.items:
            i.update()
            