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
three = pygame.image.load('3.jpg')
two = pygame.image.load('2.jpg')
one = pygame.image.load('1.jpg')




pygame.display.set_caption("Astroid Field!")
#DISPLAYSURF.fill(WHITE)
box = []
coords = []
i = 0
click = False
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

start_time = pygame.time.get_ticks() 
while True:
    restart = False
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(mouse, (mousex-20, mousey))
    counting_time = (pygame.time.get_ticks() - start_time)/1000
    string = "Time: %s" % (counting_time)
    fontObj = pygame.font.SysFont('Bahaus 93', 35)
    textSurfaceObj = fontObj.render( string , True, WHITE, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (75,75)
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
            done = "Game over! Your survived for %s seconds." % (counting_time)
            fontObj = pygame.font.SysFont('Ravie', 20)
            textSurfaceObj = fontObj.render(done , True, WHITE, BLACK)
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

        
