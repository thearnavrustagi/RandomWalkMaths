import pygame
from math import sqrt
import numpy as np

class Sprite :
    def __init__ (self, impath, scale : int = 1, direction : int = 1, max_angular_vel : float = 5):

        # Direction can only be +1 or -1 -> For Direction of Angular Velocity.

        self.image = pygame.image.load(impath)
        self.rect = self.image.get_rect()
        self.scale = scale
        self.direction = direction
        self.max_angular_vel = max_angular_vel   
        

    def blit(self,screen):
        screen.blit(self.image, self.rect)

    def rotate(self, degrees : int = 1) : 
        self.image = pygame.transform.rotate(self.image, degrees*self.direction)
        self.rect = self.image.get_rect()
    
    def origin (self):
        self.rect.left=self.position*15
        self.rect.top = self.screen[1]-self.rect.height

def op (o):
    return eval(f"lambda x,y : x {o} y")

def normalise (vector):
    return tuple(map(op("/"),vector, (mag(vector), mag(vector))))

def mag (vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2)
