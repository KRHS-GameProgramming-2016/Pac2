import pygame, sys, math
from Wall import *
from Cheese import *
from Pac import *
from PlayerPac import *

class Level():
    def __init__(self, levelFile):
        self.tileSize = 25
        self.loadLevel(levelFile) 
        
    def loadLevel(self, levelFile):        
        f = open("Resources/Levels/"+levelFile, 'r')
        lines = f.readlines()
        f.close()

        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for line in lines:
            print line
        print "________________________"
        
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#':
                    Wall([x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  
                if c == 'p':
                    print "P"
                    PlayerPac(5,
                                       [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  
                
                if c == ' ':
                     Cheese([x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  
                
                if c == 'g':
                    Pac("RedTestPac.png",
                                        [3,3],
                                        [x*self.tileSize + self.tileSize/2,
                                        y*self.tileSize + self.tileSize/2],
                                       self.tileSize)
                                  
