import sys, pygame
import Button

def readstats():
    totalstats = open("total stats.txt", 'r')
    hits, kicks = map(int, totalstats.read().split())
    totalstats.close()
    lastgame = open("last game.txt", 'r')
    lghits, lgkicks = map(int, lastgame.read().split())
    lastgame.close()
    buttonstats = open("clicks_stats.txt", 'r')
    qbutton, pbutton, sbutton = map(int, buttonstats.read().split())
    buttonstats.close()
    print("Total: " + str(hits) + " hits and " + str(kicks) + " kicks")
    print("Last game: " + str(lghits) + " hits and " + str(lgkicks) + " kicks")
    print("Buttons clicked: QUIT - " + str(qbutton) + " times, PLAY - " + str(pbutton) + " times, STATS - " + str(sbutton) + " times")  

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
    import main
    pygame.quit()
    
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
    
pygame.init()
    
size = width, height = 250, 210
screen = pygame.display.set_mode(size)
testquit = Button.button()
testquit.setPicture("quit_button.png")
testquit.setCords(0, 0, 250, 70)
testquit.setEvent(quit)
testplay = Button.button()
testplay.setPicture("Pictures/play_button.png")
testplay.setCords(0, 70, 250, 70)
testplay.setEvent(play)
teststats = Button.button()
teststats.setPicture("Pictures/stats_button.png")
teststats.setCords(0, 140, 250, 70)
teststats.setEvent(stats)


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

    screen.blit(testplay.setPicture("Pictures/play_button.png"), pygame.Rect(0, 70, 250, 70))
    screen.blit(testquit.setPicture("Pictures/quit_button.png"), pygame.Rect(0, 0, 250, 70))
    screen.blit(teststats.setPicture("Pictures/stats_button.png"), pygame.Rect(0, 140, 250, 70))
        
    pygame.time.wait(70)
    pygame.display.flip()