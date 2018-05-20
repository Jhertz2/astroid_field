import random, pygame, sys
from random import *
from pygame.locals import *

def play_end_animation():
    DISPLAYSURF.blit(boom, (mousex-20, mousey))
    pygame.display.update()
    pygame.time.wait(500)
    for i in range(4):
        DISPLAYSURF.fill(WHITE)
        pygame.display.update()
        pygame.time.wait(200)
        DISPLAYSURF.fill(BLACK)
        pygame.display.update()
        pygame.time.wait(200)
    done = "Game over! Your survived for %s seconds." % (counting_time)
    fontObj = pygame.font.SysFont('Ravie', 20)
    textSurfaceObj = fontObj.render(done , True, WHITE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400,300)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    

def play_start_animation():
    DISPLAYSURF.fill(BLACK)
    pygame.display.update()
    DISPLAYSURF.blit(three, (250,200))
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.fill(BLACK)
    pygame.display.update()
    DISPLAYSURF.blit(two, (250,200))
    pygame.display.update()
    pygame.time.wait(1000)
    DISPLAYSURF.blit(one, (250,200))
    pygame.display.update()
    pygame.time.wait(1000)

    


FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
BOXSIZE = 40

RED = (255, 0, 0 )
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0 , 0 ,0 )
YELLOW = (255, 255, 0)
highscore = 0

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
three = pygame.image.load('3.jpg')
two = pygame.image.load('2.jpg')
one = pygame.image.load('1.jpg')




pygame.display.set_caption("Astroid Field!")
#DISPLAYSURF.fill(WHITE)
box = []
coords = []
i = 0
click = False
restart = False
mouse = pygame.image.load('space.jpg')
mouse = pygame.transform.scale(mouse, (40, 40))
boom = pygame.image.load('BOOM.jpg')
boom = pygame.transform.scale(boom, (80,80))



start = "Using your mouse, you must navigate through the astroid"
start1= "field without hitting any of the incoming astroids."
start2 = "Click the screen to begin"
fontObj = pygame.font.SysFont('Ravie', 20)
textSurfaceObj = fontObj.render(start , True, WHITE, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400,300)
DISPLAYSURF.blit(textSurfaceObj,textRectObj)
textSurfaceObj1 = fontObj.render(start1 , True, WHITE, BLACK)
textRectObj1 = textSurfaceObj.get_rect()
textRectObj1.center = (400,330)
DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
textSurfaceObj2 = fontObj.render(start2 , True, WHITE, BLACK)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (400,360)
DISPLAYSURF.blit(textSurfaceObj2,textRectObj2)

# Game starts here

pygame.display.update()

# to wait for mouse click to start
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            click = True
    if click == True:
        break


mousex = 400
mousey = 550
j = 0

play_start_animation()

start_time = pygame.time.get_ticks() 
while True:

    if restart == True:
        box = []
        coords = []
        i = 0
        click = False
        restart = False
        start_time = pygame.time.get_ticks()
        pygame.display.update()
    
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(mouse, (mousex-20, mousey))
    counting_time = (pygame.time.get_ticks() - start_time)/1000
    string = "Time: %s" % (counting_time)
    fontObj = pygame.font.SysFont('Bahaus 93', 35)
    textSurfaceObj = fontObj.render( string , True, WHITE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (75,75)

    if highscore == 0:
        
        string1 = "Highscore: %s" % (counting_time)
    elif counting_time > highscore:
        string1 = 'Highscore %s' % (counting_time)
    else:
        string1 = "Highscore: %s" % (highscore)
        
    fontObj1 = pygame.font.SysFont('Bahaus 93', 35)
    textSurfaceObj1 = fontObj1.render(string1 , True, WHITE, BLACK)
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (100,100)
    x = randrange(0,800)
    y = randrange(0,50)

    # this loop prevents the degredation of performance. When the lists were getting
    # too big (around 15 seconds) the program began running slowly. 
    if i%100 == 0 and i!= 0:
        del coords [:45]
        del box [:45]
        i -= 45
        j -= 45
        
    
    box.append(pygame.Rect(x, y, BOXSIZE, BOXSIZE))

    point1 = list(box[i].bottomleft)
    point2 = list(box[i].bottomright)
    coords.append([point1,point2])
    
    pygame.time.wait(10)
    for j in range(len(box)):

        if restart == True:
            break
    
        pygame.draw.rect(DISPLAYSURF, YELLOW, box[j])
        box[j].centery +=10
        coords[j][0][1] +=10

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
        DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
        if ( (coords[j][0][0]<= mousex <=coords[j][1][0]) and (coords[j][0][1]-30 <= mousey <= coords[j][0][1]-10)):
            play_end_animation()
            click = False
            while 1 and restart == False:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == MOUSEMOTION:
                        mousex, mousey = event.pos

                again = "Play Again?" 
                fontObj1 = pygame.font.SysFont('Ravie', 20)
                textSurfaceObj1 = fontObj1.render(again , True, WHITE, BLACK)
                textRectObj1 = textSurfaceObj1.get_rect()
                textRectObj1.center = (400,350)
                DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
                pygame.display.update()
                
                while (300<= mousex <= 400 and 350<=mousey <=400) and restart == False:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEMOTION:
                            mousex, mousey = event.pos
                        elif event.type == MOUSEBUTTONUP:
                            click = True
                            
                    again = "Play Again?" 
                    fontObj1 = pygame.font.SysFont('Ravie', 20)         
                    textSurfaceObj1 = fontObj1.render(again , True, WHITE, YELLOW)
                    textRectObj1 = textSurfaceObj1.get_rect()
                    textRectObj1.center = (400,350)
                    DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
                    pygame.display.update()

                    if click == True:
                        restart = True
                        highscore = counting_time
                        play_start_animation()
                        start_time = 0
                        break
                    
                    else:
                        
                        continue
                   
            
             #pygame.quit()
             #sys.exit()
        
    i+=1
    #pygame.time.wait(500)
    pygame.display.update()
    FPSCLOCK.tick(FPS)




        
