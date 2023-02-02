import pygame
from math import sqrt, pi
import numpy as np
import utils
from random import randint

class Sprite :
    def __init__ (self, impath, scale : int = 1, direction : int = 1, xpadding : int = 0, ypadding : int = 0, steps : int = 0, rect : tuple = (0,0)):
        # Direction can only be +1 or -1 
        self.impath = impath
        self.SRC_IMAGE = pygame.image.load(self.impath)
        self.image = self.SRC_IMAGE.copy()
        self.rect = self.image.get_rect() if rect == (0,0) else rect
        self.scale = scale
        self.direction = direction
        self.steps = steps
        self.net_rotation = 0
        self.paddingx = xpadding
        self.paddingy = ypadding
        self.spritesheets = []
        self.frames = 1
        self.current_frame = 0

        self.position = utils.START
        self.new_position = utils.START
        self.angle = utils.START * (360/utils.STEPS)
        self.new_angle = self.angle
        
    def blit(self,screen):
        screen.blit(self.image, self.rect)

    def initialise_spritesheets (self,frames,basename=""):
        self.frames = frames
        for i in range(till):
            self.spritesheets.append(pygame.image.load(f"{basename}{i}.png"))

    def animate (self):
        #self.current_frame = self.current_frame%self.frames
        #self.image = self.spritesheets[self.current_frame].copy()
        #self.image = pygame.transform.flip(self.image.copy(),True,False)
        center = tuple(map(lambda x,y:x-y,self.rect.center,utils.CENTER))
        image = self.SRC_IMAGE.copy()
        if not (center[1] and center[0]): return
        mul = -1
        sign = lambda x: x / abs(x)
        add = -90
        if (center[0]) > 0: 
            mul = -1
            add = 180
            if center[1] < 0:
                image = pygame.transform.flip(image, True, True)
            center = (center[1],center[0])

        theta=utils.get_angle(center)*(180/pi) + add
        theta = theta*mul if theta < 0 else theta
        image = pygame.transform.flip(image,True if self.choice < 0 else False,False)
        self.image = pygame.transform.rotate(image,theta)
        self.rect = self.image.get_rect(center=self.rect.center)

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

    def random_walk(self,steps):
        if self.angle == self.new_angle:
            self.position = self.new_position
            self.choice= 1 if randint(0,1) else -1
            self.steps += self.choice
            self.new_position = self.position + self.choice
            self.new_angle = (self.new_position*(360/utils.STEPS))
            self.reach()
            return self.new_position
        self.reach()
        return -1

    def reach (self):
        if self.new_angle > self.angle: self.move(1)
        else: self.move(-1)

    def move (self, direction):
        self.angle = self.angle+direction
        self.rect.center = utils.get_point_on_earth(utils.CENTER, self.angle,360,utils.RADIUS+14)

def op (o):
    return eval(f"lambda x,y : x {o} y")

def normalise (vector):
    return tuple(map(op("/"),vector, (mag(vector), mag(vector))))

def mag (vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2)
