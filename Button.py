import sys, pygame

class button(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def setCords(self, x, y, z, a):
        self.topleft = x, y
        self.bottomright = x + z, y + a
        
    def setEvent(self, function):
        self.event = function
        
    def setPicture(self, image_name):
        self.image = pygame.image.load(image_name)
        return pygame.image.load(image_name)
    
    def bEvent(self):
        self.event()

    def in_button(self, mouse):
        if mouse[0] > self.topleft[0]:
            if mouse[1] > self.topleft[1]:
                if mouse[0] < self.bottomright[0]:
                    if mouse[1] < self.bottomright[1]:
                        return True
        return False