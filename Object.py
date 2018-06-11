class Object:
    def __init__(self, image, width, height, name, x = 0, y = 0):
        self.width = width
        self.height = height
        self.SetImage(image)
        self.SourceArea = (0, 0)
        self.roomID = 0
        self.name = name
        self.x = x
        self.y = y
        self.blitx = 0
        self.blity = 0

    def SetImage(self, image):
        self.image = image

    def SetCoordinates(self, x , y):
        self.x = x
        self.y = y

    def GetImage(self):
        return self.image

    def GetCoordinates(self):
        return self.y, self.x
