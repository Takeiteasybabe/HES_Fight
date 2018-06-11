import sys, pygame
import Core
import Models
import Locations

pygame.init()

size = width, height = 900, 600
screen = pygame.display.set_mode(size)
core = Core.Core(Models.StickDummy, Locations.Basic_Location)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    cells = core.update()
    screen.blit(core.location.picture, core.location.picture.get_rect())
    for i in core.items:
        if i.visible:
            placeRect = (i.x + 100, i.y + 100, i.width, i.height )
            cropRect = (i.blitx, i.blity, i.width, i.height)
            screen.blit(i.image, placeRect, cropRect)

    pygame.time.wait(100)
    pygame.display.flip()