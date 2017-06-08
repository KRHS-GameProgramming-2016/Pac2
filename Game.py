import pygame, sys, math, random

from Cheese import *
from Ghost import *
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
ghosts = pygame.sprite.Group()
hud = pygame.sprite.Group()

PlayerPac.containers = all, players
Cheese.containers = all, cheeses
Wall.containers = all, walls
Ghost.containers = all, ghosts
Score.containers = all, hud

while True:
    level = Level("level1.lvl")
    player = players.sprites()[0]
    score = Score([100, height - 30])

    levNum = 1

    while len(ghosts.sprites()) < levNum + 1:
        s = [0,0]
        while s == [0,0]:
            s = [5 * random.randint(-1,1), 5* random.randint(-1,1)]
        p = [random.randint(25, width-25), random.randint(25, height-25)]
        Ghost("RedTestPac.png", s, p, 25)
        if ghosts.sprites()[-1].detectPlayer(player):
            ghosts.sprites()[-1].kill()
        pygame.sprite.groupcollide(ghosts, walls, True, False)

    while player.living:
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
        
        all.update(size, player)
        
        playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)
        playerHitsCheeses = pygame.sprite.spritecollide(player, cheeses, True)
        playerHitsGhosts = pygame.sprite.spritecollide(player, ghosts, True)
        
        for wall in playerHitsWalls:
            player.bounceWall(wall)
          
        for cheese in playerHitsCheeses:
            score.change(1)
            
        for cheese in playerHitsGhosts:
            player.living = False
            for s in all.sprites():
                s.kill()
            
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
