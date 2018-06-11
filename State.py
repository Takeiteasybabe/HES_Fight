class State:
    def __init__(self, name, posCnt, ticks, cropCorX, cropCorY):
        self.name = name
        self.positionCount = posCnt
        self.ticks = [i for i in ticks]
        self.cropCoordinateX = cropCorX
        self.cropCoordinateY = cropCorY
        
    def return_copy(self):
        return [self.name, self.positionCount, self.ticks, self.cropCoordinates]