class State:
    def __init__(self, args):
        self.name = args[0]
        self.positionCount = args[1]
        self.ticks = [i for i in args[2]]
        self.cropCoordinateX = args[3]
        self.cropCoordinateY = args[4]
        if len(args) == 7:
            self.attackPositions = args[5]
            self.damage = args[6]
        else:
            self.attackPositions = []
            self.damage = 0
        
    def returnCopy(self):
        return (self.name, self.positionCount, self.ticks, self.cropCoordinateX, self.cropCoordinateY, self.attackPositions, self.damage)