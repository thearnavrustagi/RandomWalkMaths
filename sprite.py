import pygame
from math import sqrt
import numpy as np

class Sprite :
    def __init__ (self, impath, scale : int = 1, direction : int = 1):
        # Direction can only be +1 or -1 
        self.impath = impath
        self.image = pygame.image.load(self.impath)
        self.rect = self.image.get_rect()
        self.scale = scale
        self.direction = direction
        self.steps = 0
        self.net_rotation = 0
        
    def blit(self,screen):
        screen.blit(self.image,self.rect)

    def rotate(self, degrees : int = 1) : 
        self.image = pygame.image.load(self.impath)
        self.net_rotation += degrees * self.direction
        self.image = pygame.transform.rotate(self.image, self.net_rotation)
        self.rect = self.image.get_rect(center=self.rect.center)
    

def op (o):
    return eval(f"lambda x,y : x {o} y")

def normalise (vector):
    return tuple(map(op("/"),vector, (mag(vector), mag(vector))))

def mag (vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2)
