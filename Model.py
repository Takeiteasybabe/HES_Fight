import Object

class Model(Object.Object):
    def __init__(self, imagebox, x=0, y=0, isvisible = False):
        Object.Object.__init__(self, imagebox, 24, 32, x, y)
        self.visible = isvisible
        self.state = ["stand", 6, 0, 0, 48]
        
    def update(self):
        print("hey")
        if self.state[0] == "stand":
            if self.state[1] > 0:
                print("ho")
                self.state[1] -= 1
            else:
                print("hi")
                self.state[2] = (self.state[2] + self.width) % self.state[4]
                self.state[1] = 6
        self.blitx = self.state[2]
        self.blity = self.state[3]