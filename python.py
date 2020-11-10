import pygame
import time
import sys
clock = pygame.time.Clock()
import pygame
import time
import sys

win = pygame.display.set_mode((300, 300))
CrossSprite = pygame.image.load('C://Users//Dylan//Documents//python//py vs//sprites//X.png')
NaughtSprite = pygame.image.load('C://Users//Dylan//Documents//python//py vs//sprites//O.png')
pygame.display.set_caption("First Game")

picBlank = "picBlank"
blocks = [picBlank,picBlank,picBlank
        ,picBlank,picBlank,picBlank
        ,picBlank,picBlank,picBlank]

strblocks = [picBlank,picBlank,picBlank
        ,picBlank,picBlank,picBlank
        ,picBlank,picBlank,picBlank]

red = pygame.draw.rect(win, (255, 0, 0), (0, 0, 100, 100), 3) 
green = pygame.draw.rect(win, (0, 255, 0), (100, 0, 100, 100), 3)
blue = pygame.draw.rect(win, (0, 0, 255), (200, 0, 100, 100), 3) 
lightBlue = pygame.draw.rect(win, (0, 255, 255), (0, 100, 100, 100), 3)
yellow = pygame.draw.rect(win, (255, 255, 0), (100, 100, 100, 100), 3)
Darkblue = pygame.draw.rect(win, (0, 100, 100), (200, 100, 100, 100), 3)
Orange = pygame.draw.rect(win, (255, 70, 0), (0, 200, 100, 100), 3)
white = pygame.draw.rect(win, (255, 255, 255), (100, 200, 100, 100), 3)
pink = pygame.draw.rect(win, (231, 95, 248), (200, 200, 100, 100), 3)


naughtcount = 0
run = True
click = False
cross = False
counterXCASE = 0
counterYCASE = 0
def draw(naughtcount):
    inc = -1
    x = 0
    y = 0
    for i in range(0, 3): #FOR Y
        for i2 in range(0, 3): #FOR X 
            inc = inc+ 1
            pic = blocks[inc]
            if pic != "picBlank":
                win.blit(pic, (x, y))
                naughtcount += 1
            x += 100
        x = 0
        y += 100
    if naughtcount >= 3:
        #start checking for winners
        winnerCheckpart1()
    pygame.display.update()

        
def wincheckpart2(a,b,c):
    if a and b and c != picBlank:
            if a == b and a == c:
                print("winner!!")
                return True
            else:
                return False

def winnerCheckpart1():
    for i  in range(0,9,3):#rows
        row1 = strblocks[i]
        row2 = strblocks[i+1]
        row3 =strblocks[i+2]
        rowWinner = wincheckpart2(row1,row2,row3)
        return rowWinner
    #for i  in range(0,3):#collums
        #collum1 = strblocks[i]
        #collum2 = strblocks[i+3]
        #collum3 =strblocks[i+3]
        #collumWinner = wincheckpart2(collum1,collum2,collum3)
        #return collumWinner

        



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

def boxfinder(row, collum, Sprite,cn):
    if row == 1:
        box = row + collum - 2
    elif row == 2:
        box = row +collum
    else:
        box  = row + collum + 2
    blocks[box] = Sprite
    strblocks[box] = cn

while run:
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif click == (1,0,0):#check if left click
            collum = squareCheck(cur, 0)
            row= squareCheck(cur, 1)
            if cross:
                c = "Cross"
                boxfinder(row, collum, CrossSprite, c)
                cross = False
            else:
                n = "Naught"
                boxfinder(row, collum, NaughtSprite, n)
                cross = True
            

    draw(naughtcount)


pygame.QUIT
