import sys, pygame
import Core
import Models
import Locations

pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
core = Core.Core(Models.StickDummy, Locations.Basic_Location)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #import buttin_test
            sys.exit()
       
        if event.type == pygame.KEYDOWN:
            if event.key in core.keyBindingsDown.keys():
                core.keyBindingsDown[event.key]()
                
        if event.type == pygame.KEYUP:
            if event.key in core.keyBindingsUp.keys():
                core.keyBindingsUp[event.key]()          
                
    cells = core.update()
    screen.blit(core.location.picture, core.location.picture.get_rect())
    for i in core.items.values():
        if i.visible:
            placeRect = (i.x, i.y, i.width, i.height)
            cropRect = (i.blitx, i.blity, i.width, i.height)
            screen.blit(pygame.transform.flip(i.image, i.flipped, False), placeRect, cropRect)

    pygame.time.wait(70)
    pygame.display.flip()