#WORKING PROJECT
import pygame,sys
import copy
from sourceText import solve, valid
import time
pygame.init()

board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

cube=copy.deepcopy(board)
temp=copy.deepcopy(board)
bo=solve(board)

def draw_grid(cube):
     #DRAWING GRID
        x,y=0,0
        for row in range(len(cube)):
            if row%3==0 or row==0:
                pygame.draw.line(screen, (255,255,255), (x, y), (540, y), 3)
                pygame.draw.line(screen, (255,255,255), (y, x), (y, 540), 3)
            
                
            else:
                pygame.draw.line(screen, (255,255,255), (x, y), (540, y), 1)
                pygame.draw.line(screen, (255,255,255), (y, x), (y, 540), 1)
                           
            x=0
            y=y+w

        pygame.draw.line(screen, (255,255,255), (0, 540), (540, 540), 3)
        pygame.draw.line(screen, (255,255,255), (540, 0), (540, 540), 3) 

        #DRAWING TEXT
        fnt = pygame.font.SysFont("comicsans", 35)
        for i in range(len(cube)):
            for j in range (len(cube[0])):
                x1=j*w
                y1=i*w
                
                if cube[i][j]!=0:
                    #print('WHYY CUBE=',cube[i][j])
                    text = fnt.render(str(cube[i][j]), 1, (255, 255, 255))
                    screen.blit(text, (x1 + (w/2 - text.get_width()/2), y1 + (w/2 - text.get_height()/2)))

                elif cube[i][j]==0 and temp[i][j]!=0:                 
                    text = fnt.render(str(temp[i][j]), 1, (128,128,128))
                    screen.blit(text, (x1+5, y1+5))
                    #print('hii')

                
        '''
                sel=0
                for i in range(len(selected)):
                    for j in range(len(selected[0])):
                        if selected[i][j]==True:
                            sel=i,j
                if sel!=0:
                    x1=(clicked[1]*w)
                    y1=(clicked[0]*w) 
                    pygame.draw.rect(screen, (255,0,0), (x1,y1, w ,w), 5) '''
        #DRAWING TIME
        '''fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render("Time: " + format_time(time.time()), 1, (255,255,255))
        screen.blit(text, (540 - 160, 560))  '''


def redraw_window(screen, cube,times):
    screen.fill((0,0,0))
    # Draw time
    '''fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render("Time: " + format_time(times), 1, (255,255,255))
    screen.blit(text, (540 - 160, 560))'''
    # Draw grid and board
    draw_grid(cube)
    #Draw strikes
    fnt = pygame.font.SysFont("comicsans", 30)
    text1 = fnt.render("Strikes: ", 1, (255,255,255))
    text2 = fnt.render("X"*strikes, 1, (255,0,0))
    screen.blit(text1, (540 - 260, 560))
    screen.blit(text2, (540 - 180, 560))

def click(pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < 540 and pos[1] < 540:
            gap = 60
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None
    
def select(selected,clicked):
        row, col=clicked
        # Reset all other
        for i in range(len(selected)):
            for j in range (len(selected[0])):
                '''if selected[i][j]==True:
                    x1=(j*w)
                    y1=(i*w) 
                    pygame.draw.rect(screen, (255,255,255), (x1,y1, w ,w), 3) '''
                selected[i][j]=False

        redraw_window(screen, cube,play_time)
        selected[row][col] = True
        x1=(clicked[1]*w)
        y1=(clicked[0]*w) 
        pygame.draw.rect(screen, (255,0,0), (x1,y1, w ,w), 5)    

def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat 

def clear(clicked):
        row, col = clicked
        if cube[row][col] == 0:
            temp[row][col]=0
        redraw_window(screen, board,play_time)

def place(val,sel):
        row, col = sel
        '''print('placeee1')
        print('CUBE=',cube[row][col])
        print('TEMP=',temp[row][col])'''
        if cube[row][col]== 0:

            cube[row][col]=val
    
            cube2=copy.deepcopy(cube)
            if valid(cube, val, (row,col)) and solve(cube2):
                return True
            else:
                print('FALSE')
                cube[row][col]=0
                temp[row][col]=0
                #self.update_model()
                return False

def is_finished():
        if(strikes>=10):
            return 2
        for i in range(len(cube)):
            for j in range (len(cube[0])):
                if cube[i][j]== 0:
                    return False
        return 1

def game_over(x):
    if x==1:
        fnt1 = pygame.font.SysFont("comicsans", 60)
        text = fnt1.render("You WON! :)", 1, (255,255,255))
        screen.blit(text, (135, 163))

        fnt = pygame.font.SysFont("comicsans", 30)
        text = fnt.render("Time Taken: "+format_time(start) , 1, (255,255,255))
        screen.blit(text, (145, 244))
    elif x==2:
        fnt1 = pygame.font.SysFont("comicsans", 60)
        text = fnt1.render("You LOST! :(", 1, (255,255,255))
        screen.blit(text, (135, 163))

        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render("Time Taken: "+format_time(start) , 1, (255,255,255))
        screen.blit(text, (155, 244))

    pygame.draw.rect(screen, (255,255,255), (180,325, 180 ,60), 2)
                

    fnt3 = pygame.font.SysFont("comicsans", 40)
    text = fnt3.render("QUIT", 1, (255,255,255))
    x1=180
    y1=325
    screen.blit(text, (x1 + (180/2 - text.get_width()/2), y1 + (60/2 - text.get_height()/2)))

def redraw_over(x):
    screen.fill((0,0,0))
    game_over(x) 

def sketch(val):
        row, col = sel
        temp[row][col]=val
        redraw_window(screen, cube,play_time)

def main_page():
    fnt1 = pygame.font.SysFont("comicsans", 60)
    text = fnt1.render("Sudoko Game", 1, (255,255,255))
    screen.blit(text, (135, 163))

    fnt2 = pygame.font.SysFont("comicsans", 20)
    text = fnt2.render("Welcome to the Sudoko game where you have to solve the given ", 1, (255,255,255))
    text1 = fnt2.render("problem within 10 strikes", 1, (255,255,255))
    screen.blit(text, (68, 244))
    screen.blit(text1, (202, 270))

    pygame.draw.rect(screen, (255,255,255), (180,325, 180 ,60), 2)
                

    fnt3 = pygame.font.SysFont("comicsans", 40)
    text = fnt3.render("START", 1, (255,255,255))
    x1=180
    y1=325
    screen.blit(text, (x1 + (180/2 - text.get_width()/2), y1 + (60/2 - text.get_height()/2)))

def redraw():
    screen.fill((0,0,0))
    main_page()




if __name__=="__main__":
    
    fnt = pygame.font.SysFont("ariel", 30)
    grid =[[1]*9 for n in range(9)]
    selected=grid

    #NO CUBE SELECTED
    for i in range(len(selected)):
        for j in range (len(selected[0])):
            selected[i][j]=False

    strikes=0
    w=60
    x,y=0,0
    screen = pygame.display.set_mode((540,600))
    pygame.display.set_caption("SUDOKO")
    screen.fill((0,0,0))
    start = time.time()
    #cube=board
    #temp=board1
    key=None
    sel=0


    #FIRST WELCOME PAGE
    run=True
    while run:       

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < 360 and pos[1] < 385 and pos[0]>180 and pos[1]>325:
                    run=False

        redraw()
        pygame.display.update()


    #PROBLEM PAGE
    draw_grid(cube)
    play_time = round(time.time() - start)
    redraw_window(screen, cube,play_time)
    #pygame.draw.rect(screen,(0,0,0),(x,y,420,420))
    run=True
    while run:
        play_time = round(time.time() - start)

        for i in range(len(selected)):
                    for j in range(len(selected[0])):
                        if selected[i][j]==True:
                            sel=i,j

        

        for event in pygame.event.get():
        
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:               
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:                    
                    clear(sel)
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = sel
                    if temp[i][j] != 0:
                        #print('temp!=0')
                        if place(temp[i][j],sel):
                            redraw_window(screen, cube,play_time)
                            text = fnt.render('Correct', 1, (0,255,0))
                            screen.blit(text, (20, 560))
                        else:
                            clear(sel)
                            strikes += 1
                            print('Strikes=',strikes) 
                            redraw_window(screen, cube,play_time)    
                            text = fnt.render('Wrong', 1, (255,0,0))
                            screen.blit(text, (20, 560))               

                        if is_finished():
                            start=play_time  #FINAL TIME TAKEN
                            run=False
                            print("FINISHED=",is_finished())
                        
                    key = None

        #WHEN A CUBE IS CLICKED
            if event.type == pygame.MOUSEBUTTONDOWN:           
                pos = pygame.mouse.get_pos()
                clicked = click(pos)
                #print(clicked[0],"   ",clicked[1])
                if clicked:
                    #print('MOUSE CLICKED')
                    select(selected,clicked)
                    key=None

        if sel and key != None:
            #print('sketchhhhh')
            sketch(key)

        
        pygame.display.update()   

    run=True
    while run:       

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] < 360 and pos[1] < 385 and pos[0]>180 and pos[1]>325:
                    run=False

        redraw_over(is_finished())
        pygame.display.update()

        
               
                    