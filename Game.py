import pygame, sys, math, random

from Cheese import *
from Pac import *
from PlayerPac import *
from Wall import *
from Level import *
from Score import *

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 67, 75, 198

all = pygame.sprite.OrderedUpdates()
players = pygame.sprite.Group()
cheeses = pygame.sprite.Group()
walls = pygame.sprite.Group()
pacs = pygame.sprite.Group()
hud = pygame.sprite.Group()

PlayerPac.containers = all, players
Cheese.containers = all, cheeses
Wall.containers = all, walls
Pac.containers = all, pacs
Score.containers = all, hud

level = Level("level1.lvl")
player = players.sprites()[0]
score = Score([100, height - 30])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_LEFT:
                player.go("left")
            if event.key == pygame.K_RIGHT:
                player.go("right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
    
    all.update(size)
    
    playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)
    playerHitsCheeses = pygame.sprite.spritecollide(player, cheeses, True)
    
    for wall in playerHitsWalls:
        player.bounceWall(wall)
      
    for cheese in playerHitsCheeses:
        score.change(1)
        
    bgColor = r,g,b
    screen.fill(bgColor)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
    
