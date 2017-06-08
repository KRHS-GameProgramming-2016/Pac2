import pygame, sys, math

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Resources/Cheese/frontend-large.png")
        if size: 
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        
        
    def update(self, *args):
        pass
        
        
    
            
