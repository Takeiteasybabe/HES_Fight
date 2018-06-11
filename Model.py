import Object

class Model(Object.Object):
    def __init__(self, imagebox, name, x=0, y=0, isvisible = False):
        Object.Object.__init__(self, imagebox, 24, 32, name)
        self.visible = isvisible
        self.flipped = False
        self.state = ["stand", 6, 0, 0, 48]
        
    def update(self):
        if self.state[0] == "stand":
            if self.state[1] > 0:
                self.state[1] -= 1
            else:
                self.state[2] = (self.state[2] + self.width) % self.state[4]
                self.state[1] = 6
        self.blitx = self.state[2]
        self.blity = self.state[3]