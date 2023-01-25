import pygame
from math import sqrt
import numpy as np

class Sprite :
    def __init__ (self, impath, scale : int = 1, direction : int = 1, xpadding : int = 0, ypadding : int = 0):
        # Direction can only be +1 or -1 
        self.impath = impath
        self.SRC_IMAGE = pygame.image.load(self.impath)
        self.image = self.SRC_IMAGE.copy()
        self.rect = self.image.get_rect()
        self.scale = scale
        self.direction = direction
        self.steps = 0
        self.net_rotation = 0
        self.paddingx = xpadding
        self.paddingy = ypadding
        self.spritesheets = []
        self.frames = 1
        self.current_frame = 0
        
    def blit(self,screen):
        screen.blit(self.image, self.rect)

    def initialise_spritesheets (self,frames,basename=""):
        self.frames = frames
        for i in range(till):
            self.spritesheets.append(pygame.image.load(f"{basename}{i}.png"))

    def animate (self):
        self.current_frame = self.current_frame%self.frames
        self.image = self.spritesheets[self.current_frame].copy()
        self.image = pygame.transform.flip(self.image.copy(),True,False)

    def animate_and_blit (self, screen):
        self.animate()
        self.blit(screen)

    def rotate(self, degrees : int = 1, pos : tuple = (0,0)) : 
        self.image = self.SRC_IMAGE.copy()
        self.image = pygame.transform.scale(self.image,(100*self.scale,100*self.scale))
        self.rect.center = tuple([pos[0]//2, pos[1]//2 + self.paddingy])
        self.net_rotation += degrees * self.direction
        self.image = pygame.transform.rotate(self.image, self.net_rotation)
        self.rect = self.image.get_rect(center=self.rect.center)
    

def op (o):
    return eval(f"lambda x,y : x {o} y")

def normalise (vector):
    return tuple(map(op("/"),vector, (mag(vector), mag(vector))))

def mag (vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2)
