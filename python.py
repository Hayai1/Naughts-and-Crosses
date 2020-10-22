import pygame
import time
clock = pygame.time.Clock()
pygame.init()

#, 'orange','yellow',"green",'blue','white'
win = pygame.display.set_mode((500, 480))
#C:\Users\Dylan\Documents\python\py vs
pygame.display.set_caption("First Game")

#blocks = [picBlank,picBlank,picBlank,picBlank,picBlank,picBlank,picBlank,picBlank,picBlank,]
#picBlank
#picCross
#picNought.png
red = pygame.draw.rect(win, (255, 0, 0), (0, 0, 100, 100), 3) 
green = pygame.draw.rect(win, (0, 255, 0), (100, 0, 100, 100), 3)
blue = pygame.draw.rect(win, (0, 0, 255), (200, 0, 100, 100), 3) 
lightBlue = pygame.draw.rect(win, (0, 255, 255), (0, 100, 100, 100), 3)
yellow = pygame.draw.rect(win, (255, 255, 0), (100, 100, 100, 100), 3)
Darkblue = pygame.draw.rect(win, (0, 100, 100), (200, 100, 100, 100), 3)
Orange = pygame.draw.rect(win, (255, 70, 0), (0, 200, 100, 100), 3)
white = pygame.draw.rect(win, (255, 255, 255), (100, 200, 100, 100), 3)
pink = pygame.draw.rect(win, (231, 95, 248), (200, 200, 100, 100), 3)



xb = 0
yb = 0
run = True
click = False
cross = False
counterXCASE = 0
counterYCASE = 0
def draw():
    #for i in 3: FOR Y
    #x = 0
    # y = 0
    # for i2 in 3: FOR X 
        #win.blit(blocks[COUNTER+=1], (x, y))
        # X += 100
    #X = 0
    # Y += 100
    

    
    pygame.display.update()

def putdown(row, collum):
    if cross:
        #row + collum - 2 = postion in array (array of blocks)



def squareCheck(cur, x):
    x = cur[x]
    if x < 100:
        #topRow = True        
        return 1
    elif x < 200:
        #middleRow = True
        return 2
    else:
        #bottomRow = True        
        return 3


while run:
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clock.tick(60)
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif click == (1,0,0):#check if left click
            collum = squareCheck(cur, 0)
            row= squareCheck(cur, 1)
            if cross:
                print("put a cross","row =", row,"collum = ",collum)
                cross = False
            else:
                print("put a nort","row =", row,"collum = ",collum)
                cross = True
            
            #check what square has been clicked

        

    draw()


pygame.QUIT
