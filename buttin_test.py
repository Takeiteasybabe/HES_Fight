import sys, pygame
import Button

def quit():
    print('Astolfo')
    pygame.quit()
    sys.exit()    
    
pygame.init()
    
size = width, height = 400, 200
screen = pygame.display.set_mode(size)
testquit = Button.button()
testquit.setPicture("quit_button.png")
testquit.setCords(0, 0, 250, 70)
testquit.setEvent(quit)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if testquit.in_button(event.pos):
                testquit.bEvent()

    screen.blit(testquit.setPicture("quit_button.png"), pygame.Rect(0, 0, 250, 70))
        
    pygame.time.wait(70)
    pygame.display.flip()