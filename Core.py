import Location
import Model

class Core:
    def __init__(self, model1, Location):
        self.location = Location
        self.items = [model1]
        for i in range(len(self.items)):
            self.items[i].visible = True
        
    def update(self):
        for i in self.items:
            i.update()
            