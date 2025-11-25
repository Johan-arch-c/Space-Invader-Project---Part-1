import math
import random
import pygame

SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27

pygame.init()

screen=pygame.display.set_model((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invader")
icon=pygame.image.load('OIP (1).webp')
pygame.display.set_icon(icon)

playerImg=pygame.image.load('download.webp')
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('OIP.webp'))
    enemyX.append(random.randint(0,SCREEN_WIDTH=64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)