from sprite import Sprite
import pygame
import numpy as np

DEGREES = 360

class Planet (Sprite):
    def __init__ (self):
        self.steps = 0

    def random_walk (self, divisions=90):
        if self.steps > divisions/DEGREES:
            self.steps = 0
            self.direction = -1 if np.random.randint(2) else 1
        self.rotate(1)
        self.steps += 1
