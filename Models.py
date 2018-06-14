import pygame
from Model import Model

stickdummy_image = pygame.image.load("Pictures/Gjlotnok_All.png")
blue_stickdummy_image = pygame.image.load("Pictures/Shirokov_All.png")

StickDummy = Model(stickdummy_image, "StickDummy")
BlueStickDummy = Model(blue_stickdummy_image, "StickDummy")