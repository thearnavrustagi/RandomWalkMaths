from sprite import Sprite
import pygame
import numpy as np

DEGREES = 360

class Planet (Sprite):
    def origin (self,pos:tuple=(0,0)):
        self.rotate(0, pos)
