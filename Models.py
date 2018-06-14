import pygame
from Model import Model

stickdummy_image = pygame.image.load("Hero_Parody1_Borders.png")
blue_stickdummy_image = pygame.image.load("Hero_Parody2.png")

StickDummy = Model(stickdummy_image, "StickDummy")
BlueStickDummy = Model(blue_stickdummy_image, "StickDummy")