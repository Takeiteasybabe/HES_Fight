class Object:
    def __init__(self, image, width, height, name, x = 0, y = 0):
        self.width = width
        self.height = height
        self.setImage(image)
        self.name = name
        self.x = x
        self.y = y
        self.blitx = 0
        self.blity = 0

    def setImage(self, image):
        self.image = image

    def setCoordinates(self, x , y):
        self.x = x
        self.y = y

    def getImage(self):
        return self.image

    def getCoordinates(self):
        return self.y, self.x
