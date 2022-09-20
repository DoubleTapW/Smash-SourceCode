import pygame , random
from pygame import display
from pygame.locals import *
import math

# MY CLASSES

from backround import Backround_Cosmatics
from enemy import Enemy
from player import Player
import wepons

# Initiate Pygame
pygame.init()

# Visual Window
DisplayInfo = pygame.display.Info()
SCREEN_WIDTH = DisplayInfo.current_w
SCREEN_HEIGHT = DisplayInfo.current_h
Win = pygame.display.set_mode(( SCREEN_WIDTH , SCREEN_HEIGHT ) , FULLSCREEN)
display.set_caption("SMASH!")
Icon = pygame.image.load('images/Icon.png')
pygame.display.set_icon(Icon)

# imageLoader
player_base = pygame.image.load('images/Player/player_base.png')
player_base = pygame.transform.scale( player_base , ( 64 , 64 ))
player_default_eyes = pygame.image.load('images/Player/eyes/default_eyes.png')
player_default_eyes = pygame.transform.scale( player_default_eyes , ( 64 , 64 ))
playerJoined = True

enemy_img = pygame.image.load('images/enemy.png')
enemy_img = pygame.transform.scale( enemy_img , ( 64 , 64 ))

flower = pygame.image.load('images/backround/flower.png')
flower_overlay = pygame.image.load('images/backround/flower_overlay.png')
stone = pygame.image.load('images/backround/stone.png')
grass1 = pygame.image.load('images/backround/grass1.png')
grass2 = pygame.image.load('images/backround/grass2.png')

flower = pygame.transform.scale( flower , ( 48 , 32 ))
flower_overlay = pygame.transform.scale( flower_overlay , ( 48 , 32 ))
stone = pygame.transform.scale( stone , ( 42 , 30 ))
grass1 = pygame.transform.scale( grass1 , ( 36 , 16 ))
grass2 = pygame.transform.scale( grass2 , ( 36 , 16 ))

pistol = pygame.image.load('images/wepons/pistol.png')
#pistol = pygame.transform.scale( pistol , ( 96 , 28 ))

# Clock
clock = pygame.time.Clock()

# Variables
Red = ( 255 , 0 , 0 )
Green = ( 0 , 255 , 0 )
Blue = ( 0 , 0 , 255 )
Black = ( 0 , 0 , 0 )
White = ( 255 , 255 , 255 )
Grey = (200, 200, 200)

PlayerPos = [ 500 , 500 ]
player_right = False
player_left = False
player_up = False
player_down = False
player_speed = 7
player_alive = True

enemy_cap = 20
enemy_speed = 3
enemies_list = []

Backround_cosmetics_cap = 15
Backround_cosmatics_list = []

playerList = []
playerWeponList = []

# Cosmetics
player_eyes = player_default_eyes

# wepons
weponlist = [ pistol , 1 , 2 ]
currentWepon = weponlist[0]
    
##### main loop #####

Running = True
while Running:

    Win.fill(( 39 , 188 , 39 ))
  

    for event in pygame.event.get():
        if event.type == QUIT:
            Running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_up = True

            if event.key == pygame.K_s:
                player_down = True

            if event.key == pygame.K_a:
                player_left = True

            if event.key == pygame.K_d:
                player_right = True      

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_up = False

            if event.key == pygame.K_s:
                player_down = False

            if event.key == pygame.K_a:
                player_left = False

            if event.key == pygame.K_d:
                player_right = False  
                
    if player_up:
        PlayerPos[1] -= player_speed

    if player_down:
        PlayerPos[1] += player_speed

    if player_right:
        PlayerPos[0] += player_speed

    if player_left:
        PlayerPos[0] -= player_speed

    if PlayerPos[0] <= 0 :
        PlayerPos[0] = 0

    if PlayerPos[0] >= SCREEN_WIDTH - 64 :
        PlayerPos[0] = SCREEN_WIDTH - 64

    if PlayerPos[1] <= 0 :
        PlayerPos[1] = 0

    if PlayerPos[1] >= SCREEN_HEIGHT - 64 :
        PlayerPos[1] = SCREEN_HEIGHT - 64

    # Test Code (BETA)

    #######****************#######

    # Cosmatic List
    if len(Backround_cosmatics_list) <= Backround_cosmetics_cap:
        cosmatic = Backround_Cosmatics(0 , SCREEN_WIDTH , SCREEN_HEIGHT , flower , stone , grass1 , grass2)
        Backround_cosmatics_list.append(cosmatic)
    for cosmatic in Backround_cosmatics_list:
        cosmatic.DrawCosmatics( Win )

    # Enemy List
    if len(enemies_list) <= 20:
        enemy = Enemy(random.randint( 0 , SCREEN_WIDTH  ) , random.randint( -100 , 0 ) , enemy_speed , enemy_img )
        enemies_list.append( enemy )
    for enemy in enemies_list:
        enemy.draw_enemy( Win )
        enemy.movement(PlayerPos[0] , PlayerPos[1])

    # Player
    if playerJoined:
        player = Player(True , player_base , player_default_eyes)
        playerWepon = wepons.Wepons(currentWepon)
        playerWeponList.append(playerWepon)
        playerList.append(player)
        playerJoined = False

    for player in playerList:
        player.playerDraw(Win , PlayerPos[0] , PlayerPos[1])

    for playerWepon in playerWeponList:
        playerWepon.drawWepon(Win , PlayerPos[0]  , PlayerPos[1])

    pygame.display.update()
    clock.tick(60)  #FPS