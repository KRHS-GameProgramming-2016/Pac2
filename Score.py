import pygame, sys, math 

class Score(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.value = 0
        self.font = pygame.font.Font("Resources/Fonts/PercyPixel.ttf", 51)
        self.image = self.font.render("Score: " + str(self.value), True, (100,0,30))
        self.rect = self.image.get_rect(center = pos)
    
    def change(self, amount = 1):
        self.value += amount
        if self.value <= 0:
            self.value = 0
        self.image = self.font.render("Score: " + str(self.value), True, (100,0,30))
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def setValue(self, amount = 0):
        self.value = amount
        if self.value <= 0:
            self.value = 0
        self.image = self.font.render("Score: " + str(self.value), True, (100,0,30))
        self.rect = self.image.get_rect(center = self.rect.center)
