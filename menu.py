import sys, pygame
import Core
import Models
import Locations
import Button

def erase():
    open("total stats.txt", 'w').close()
    open("last game.txt", 'w').close()
    open("clicks_stats.txt", 'w').close()
    
def goback():
    menu()
    #pygame.quit() 
    
def readstats():
    #totalstats = open("total stats.txt", 'r')
    #hits, kicks = map(int, totalstats.read().split())
    #totalstats.close()
    #lastgame = open("last game.txt", 'r')
    #lghits, lgkicks = map(int, lastgame.read().split())
    #lastgame.close()
    #buttonstats = open("clicks_stats.txt", 'r')
    #qbutton, pbutton, sbutton = map(int, buttonstats.read().split())
    #buttonstats.close()
    #print("Total: " + str(hits) + " hits and " + str(kicks) + " kicks")
    #print("Last game: " + str(lghits) + " hits and " + str(lgkicks) + " kicks")
    #print("Buttons clicked: QUIT - " + str(qbutton) + " times, PLAY - " + str(pbutton) + " times, STATS - " + str(sbutton) + " times")
    Stats()

def quit():
    clicks = open("clicks_stats.txt", 'r')
    a, b, c = map(int, clicks.read().split())
    clicks.close()
    open("clicks_stats.txt", 'w').close()
    a += 1
    a, b, c = str(a), str(b), str(c)
    clicks = open("clicks_stats.txt", 'w')
    clicks.write(" ".join([a, b, c]))
    clicks.close()    
    pygame.quit()
    sys.exit()  
    
def play():
    clicks = open("clicks_stats.txt", 'r')
    a, b, c = map(int, clicks.read().split())
    clicks.close()
    open("clicks_stats.txt", 'w').close()
    b += 1
    a, b, c = str(a), str(b), str(c)
    clicks = open("clicks_stats.txt", 'w')
    clicks.write(" ".join([a, b, c]))
    clicks.close()       
    game()
    
def stats():
    clicks = open("clicks_stats.txt", 'r')
    a, b, c = map(int, clicks.read().split())
    clicks.close()
    open("clicks_stats.txt", 'w').close()
    c += 1
    a, b, c = str(a), str(b), str(c)
    clicks = open("clicks_stats.txt", 'w')
    clicks.write(" ".join([a, b, c]))
    clicks.close()       
    readstats()

def game():
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    core = Core.Core(Models.StickDummy, Models.BlueStickDummy, Locations.Basic_Location)
    open("last game.txt", 'w').close()
    lastgame = open("last game.txt", 'w')
    lastgame.write('0 0')
    lastgame.close()
    
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
                menu()
           
            if event.type == pygame.KEYDOWN:
                if event.key in core.keyBindingsDown.keys():
                    core.keyBindingsDown[event.key]()
                    
            if event.type == pygame.KEYUP:
                if event.key in core.keyBindingsUp.keys():
                    core.keyBindingsUp[event.key]()          
                    
        core.update()
        screen.blit(core.location.picture, core.location.picture.get_rect())
        for i in core.items.values():
            if i.visible:
                placeRect = (i.x, i.y, i.width, i.height)
                cropRect = (i.blitx, i.blity, i.width, i.height)
                screen.blit(pygame.transform.flip(i.image, i.flipped, False), placeRect, cropRect)
    
        pygame.time.wait(70)
        pygame.display.flip()
        
def menu():
    size = width, height = 250, 210
    screen = pygame.display.set_mode(size)
    testquit = Button.button()
    testquit.setPicture("quit_button.png")
    testquit.setCords(0, 0, 250, 70)
    testquit.setEvent(quit)
    testplay = Button.button()
    testplay.setPicture("play_button.png")
    testplay.setCords(0, 70, 250, 70)
    testplay.setEvent(play)
    teststats = Button.button()
    teststats.setPicture("stats_button.png")
    teststats.setCords(0, 140, 250, 70)
    teststats.setEvent(stats)
    screen.blit(testplay.setPicture("play_button.png"), pygame.Rect(0, 70, 250, 70))
    screen.blit(testquit.setPicture("quit_button.png"), pygame.Rect(0, 0, 250, 70))
    screen.blit(teststats.setPicture("stats_button.png"), pygame.Rect(0, 140, 250, 70))
    pygame.display.update()
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if testquit.in_button(event.pos):
                    testquit.bEvent()
                if testplay.in_button(event.pos):
                    testplay.bEvent()   
                if teststats.in_button(event.pos):
                    teststats.bEvent()
                    
def Stats():
    totalstats = open("total stats.txt", 'r')
    hits, kicks = map(int, totalstats.read().split())
    totalstats.close()
    lastgame = open("last game.txt", 'r')
    lghits, lgkicks = map(int, lastgame.read().split())
    lastgame.close()
    buttonstats = open("clicks_stats.txt", 'r')
    qbutton, pbutton, sbutton = map(int, buttonstats.read().split())
    buttonstats.close()
    
    hitstats = ("Total: " + str(hits) + " hits and " + str(kicks) + " kicks")
    laststats = ("Last game: " + str(lghits) + " hits and " + str(lgkicks) + " kicks")
    buttons = ("Buttons clicked: QUIT - " + str(qbutton) + " times, PLAY - " + str(pbutton) + " times, STATS - " + str(sbutton) + " times")
    
    size = width, height = 600, 250
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    basicfont = pygame.font.SysFont('Arial', 20)
    text1 = basicfont.render(hitstats, True, (0, 0, 0))
    #print(hitstats)
    text1rect = text1.get_rect()
    text1rect.centerx = screen.get_rect().centerx
    text1rect.centery = 20
    text2 = basicfont.render(laststats, True, (0, 0, 0))
    text2rect = text2.get_rect()
    text2rect.centerx = screen.get_rect().centerx
    text2rect.centery = 40
    text3 = basicfont.render(buttons, True, (0, 0, 0))
    text3rect = text3.get_rect()
    text3rect.centerx = screen.get_rect().centerx
    text3rect.centery = 60
    clear = Button.button()
    clear.setPicture("clear_stats.png")
    clear.setCords(175, 100, 250, 70)
    clear.setEvent(erase)
    
    back = Button.button()
    back.setPicture("menu.png")
    back.setCords(175, 170, 250, 70)
    back.setEvent(goback)
    
    screen.blit(text1, text1rect)
    screen.blit(text2, text2rect)
    screen.blit(text3, text3rect)
    screen.blit(clear.setPicture("clear_stats.png"), pygame.Rect(175, 100, 250, 70))
    screen.blit(back.setPicture("menu.png"), pygame.Rect(175, 170, 250, 70))
    
    pygame.display.update()
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clear.in_button(event.pos):
                    clear.bEvent()
                if back.in_button(event.pos):
                    back.bEvent()     

pygame.init()

menu()
