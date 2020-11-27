import pygame, sys, random, time
from pygame.locals import *


pygame.init()

win = pygame.display.set_mode((0, 0), pygame.RESIZABLE|pygame.DOUBLEBUF)
pygame.display.set_caption("Kito")

menu = True
stone = True
player = False
buttonStart = False
ButtonStop = False
start = False
counter = 0
screen_shake = 0
clock=pygame.time.Clock()



StartSprite1 = pygame.image.load('C://Users//Dylan//Documents//python//pygame game//Sprites//start button 1.png')
StartSpritePushed= pygame.image.load('C://Users//Dylan//Documents//python//pygame game//Sprites//start button pushed.png')
StopSprite1 = pygame.image.load('C://Users//Dylan//Documents//python//pygame game//Sprites//stop button 1.png')
StopSpritePushed= pygame.image.load('C://Users//Dylan//Documents//python//pygame game//Sprites//stop button pushed.png')
bgStart= pygame.image.load('C://Users//Dylan//Documents//python//pygame game//Sprites//bg.png')


#<---------------PLAYER SPRITES------------------>

playerStone= pygame.image.load('C://Users//Dylan//Documents//python//pygame game//Sprites//PLAYER//PLAYERSTONE.png')
playerNormal= pygame.image.load('C://Users//Dylan//Documents//python//pygame game//Sprites//PLAYER//PLAYERNORMAL.png')

#<---------------PLAYER SPRITES------------------>
#C:\Users\Dylan\Documents\python\pygame game\Sprites



#-------------------MENU------------------------->
while menu:
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    x,y = pygame.mouse.get_pos()
    if 50 < x < 350 and 300 < y < 450:
        win.blit(StartSpritePushed,(50,300))
        win.blit(StopSprite1,(1500,300))
        if click == (1,0,0):
            menu = False
    elif 1500 < x < 1800 and 300 < y < 450:
        win.blit(StartSprite1,(50,300))
        win.blit(StopSpritePushed,(1500,300))
        if click == (1,0,0):
            pygame.quit()
    else:
        win.blit(StartSprite1,(50,300))
        win.blit(StopSprite1,(1500,300))
    pygame.display.update()

win.fill((0,0,0))
pygame.display.update()
x = 1050
y = 480

#<-------------------MENU------------------------->




#<------------------GAME-------------------------->
def draw(x,y,renderOffset):
    win.blit(bgStart,renderOffset)
    win.blit(playerNormal,(x,y))
    pygame.display.update()


Game = True
while Game:
    keys=pygame.key.get_pressed()
    if stone:
        win.blit(playerStone,(1050,480))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
    if start:
        if keys[pygame.K_d]:
            x += 5
        if keys[pygame.K_a]:
            x -= 5
        renderOffset = [0,0]
        draw(x,y,renderOffset)
        


    if stone:
        if counter != 200:
            if counter == 50:
                time.sleep(2)
            if counter == 75:
                time.sleep(2)

            if event.type == KEYDOWN:
                screen_shake = 30
                counter += 1

            if screen_shake >0:
                screen_shake -=1

            renderOffset = [0,0]
            if screen_shake:
                renderOffset[0] = random.randint(0,8) - 4
                renderOffset[1] = random.randint(0,8) - 4
            win.blit(bgStart,renderOffset)
            pygame.display.update()
        else:
            stone = False
            start = True
    


    clock.tick(60)
pygame.quit()
#<------------------GAME-------------------------->