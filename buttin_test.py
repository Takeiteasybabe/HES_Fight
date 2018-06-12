import sys, pygame
import Button

def quit():
    print('Astolfo')
    pygame.quit()
    sys.exit()  
    
def play():
    print('GAY')
    import main
    pygame.quit()
    
pygame.init()
    
size = width, height = 400, 200
screen = pygame.display.set_mode(size)
testquit = Button.button()
testquit.setPicture("quit_button.png")
testquit.setCords(0, 0, 250, 70)
testquit.setEvent(quit)
testplay = Button.button()
testplay.setPicture("play_button.png")
testplay.setCords(0, 70, 250, 70)
testplay.setEvent(play)


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

    screen.blit(testplay.setPicture("play_button.png"), pygame.Rect(0, 70, 250, 70))
    screen.blit(testquit.setPicture("quit_button.png"), pygame.Rect(0, 0, 250, 70))
        
    pygame.time.wait(70)
    pygame.display.flip()