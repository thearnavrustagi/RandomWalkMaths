import pygame
from math import sqrt
import numpy as np

class Sprite :
    def __init__ (self, impath, size, max_speed=(2,0), acceleration=0.1):
        self.image = pygame.image.load(impath)
        self.rect = self.image.get_rect()
        self.max_speed = max_speed
        self.speed = (0,0)
        self.acceleration=acceleration
        self.position = 0.0

        self.target = None
        self.old_target = (0,0)

        self.screen = size
        self.position = 50
        self.old_position=49

    def blit(self,screen):
        screen.blit(self.image, self.rect)

    def random_walk (self):
        if self.target == None:
            choice = np.random.randint(2)
            self.position += 1 if choice else -1
            self.target = (self.position*15,self.rect.centery)
            print("targetting",self.target)
        else:
            if abs(self.rect.centerx - self.target[0]) < 8:
                self.old_position = self.position
                self.target = None
                self.random_walk()
                return
            self.move_towards(self.target)
        
    def move_towards (self, point):
        #self.origin()
        factor = (self.target[0] - self.rect.centerx,
                  self.target[1] - self.rect.centery)
        factor = normalise(factor)
        """self.speed = tuple(map(
                    op("+"),
                    tuple(map(
                        op("*"),self.acceleration,factor
                        )),
                    self.speed
                    ))"""
        self.speed = tuple(map(op("*"),self.max_speed,factor))
        #self.position = tuple(map(op("+"),self.position, self.speed))
        #self.rect.move(self.position)
        self.rect.move_ip(self.speed[0],self.speed[1])
    
    def origin (self):
        self.rect.left=self.position*15
        self.rect.top = self.screen[1]-self.rect.height

def op (o):
    return eval(f"lambda x,y : x {o} y")

def normalise (vector):
    return tuple(map(op("/"),vector, (mag(vector), mag(vector))))

def mag (vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2)
