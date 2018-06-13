import sys, pygame
import Core
import Models
import Locations

pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
core = Core.Core(Models.StickDummy, Models.BlueStickDummy, Locations.Basic_Location)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            totalstats = open("total stats.txt", 'r')
            hits, kicks = map(int, totalstats.read().split())
            totalstats.close()
            open("total stats.txt", 'w').close()
            lastgame = open("last game.txt", 'r')
            lghits, lgkicks = map(int, lastgame.read().split())
            lastgame.close()
            hits += lghits
            kicks += lgkicks
            hits, kicks = str(hits), str(kicks)
            totalstats = open("total stats.txt", 'w')
            totalstats.write(" ".join([hits, kicks]))
            totalstats.close()            
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