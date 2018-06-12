class State:
    def __init__(self, args):
        self.name = args[0]
        self.positionCount = args[1]
        self.ticks = [i for i in args[2]]
        self.cropCoordinateX = args[3]
        self.cropCoordinateY = args[4]     
        
    def returnCopy(self):
        return (self.name, self.positionCount, self.ticks, self.cropCoordinateX, self.cropCoordinateY)