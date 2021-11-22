#testpygame.py is the working project
import pygame,sys
from sourceText import solve, valid
import time
pygame.init()

def game_over(x):

    if x==1:
        fnt1 = pygame.font.SysFont("comicsans", 60)
        text = fnt1.render("You WON! :)", 1, (255,255,255))
        screen.blit(text, (135, 82))

        fnt1 = pygame.font.SysFont("comicsans", 20)
        text = fnt1.render("No of strikes:", 1, (255,0,0))
        screen.blit(text, (135, 140))

        fnt = pygame.font.SysFont("comicsans", 30)
        text = fnt.render("Time Taken: " , 1, (255,255,255))
        screen.blit(text, (68, 173))
    
    '''fnt2 = pygame.font.SysFont("comicsans", 20)
    text = fnt2.render("Welcome to the Sudoko game where you have to solve the given ", 1, (255,255,255))
    text1 = fnt2.render("problem within 10 strikes", 1, (255,255,255))
    screen.blit(text, (68, 244))
    screen.blit(text1, (202, 270))

    pygame.draw.rect(screen, (255,255,255), (180,325, 180 ,60), 2)
                

    fnt3 = pygame.font.SysFont("comicsans", 40)
    text = fnt3.render("START", 1, (255,255,255))
    x1=180
    y1=325
    screen.blit(text, (x1 + (180/2 - text.get_width()/2), y1 + (60/2 - text.get_height()/2)))'''

def redraw():
    screen.fill((0,0,0))
    game_over(1)#main_page()


if __name__=="__main__":
    screen = pygame.display.set_mode((540,650))
    pygame.display.set_caption("Sudoku")
    #screen.fill((0,0,0))
    run=True
    while run:       

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        run=False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pos[0] < 270 and pos[0]>270 :
                            game_over(1)
                        if pos[0]>270 :
                            game_over(2)

                redraw()
                pygame.display.update()
            