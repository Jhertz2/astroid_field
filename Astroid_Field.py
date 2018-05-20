import random, pygame, sys
from random import *
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
BOXSIZE = 40

RED = (255, 0, 0 )
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0 , 0 ,0 )
YELLOW = (255, 255, 0)


pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))



pygame.display.set_caption("Avoider!")
#DISPLAYSURF.fill(WHITE)
box = []
coords = []
i = 0
start_time = pygame.time.get_ticks() 
click = False
mouse = pygame.image.load('space.jpg')
mouse = pygame.transform.scale(mouse, (40, 40))
boom = pygame.image.load('BOOM.jpg')
boom = pygame.transform.scale(boom, (80,80))

start = "You must navigate through the screen without having"
start1= "your mouse touch any of the red boxes."
start2 = "Click the screen to begin"
fontObj = pygame.font.SysFont('arial', 20)
textSurfaceObj = fontObj.render(start , True, WHITE, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400,300)
DISPLAYSURF.blit(textSurfaceObj,textRectObj)
textSurfaceObj1 = fontObj.render(start1 , True, WHITE, BLUE)
textRectObj1 = textSurfaceObj.get_rect()
textRectObj1.center = (400,325)
DISPLAYSURF.blit(textSurfaceObj1,textRectObj1)
textSurfaceObj2 = fontObj.render(start2 , True, WHITE, BLUE)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.center = (400,350)
DISPLAYSURF.blit(textSurfaceObj2,textRectObj2)
pygame.display.update()
restart = False

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

while True:
    restart = False
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(mouse, (mousex-20, mousey))
    counting_time = (pygame.time.get_ticks() - start_time)/1000
    string = "Time: %s" % (counting_time)
    fontObj = pygame.font.SysFont('arial', 20)
    textSurfaceObj = fontObj.render( string , True, WHITE, BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (50,50)
    x = randrange(0,800)
    y = randrange(0,50)
    box.append(pygame.Rect(x, y, BOXSIZE, BOXSIZE))

    point1 = list(box[i].bottomleft)
    point2 = list(box[i].bottomright)
    coords.append([point1,point2])
    
    pygame.time.wait(10)
    for j in range(len(box)):

        

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
        if ( (coords[j][0][0]<= mousex <=coords[j][1][0]) and (coords[j][0][1]-30 <= mousey <= coords[j][0][1]-10)):
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
            done = "Game over! Your Score was %s seconds" % (counting_time)
            fontObj = pygame.font.SysFont('arial', 20)
            textSurfaceObj = fontObj.render(done , True, WHITE, BLUE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (400,300)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.quit()
            sys.exit()

            
            
            
           
        
        





    i+=1
    #pygame.time.wait(500)
    pygame.display.update()
    FPSCLOCK.tick(FPS)

        
