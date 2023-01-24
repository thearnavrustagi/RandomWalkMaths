from sprite import Sprite
import pygame
import numpy as np

DEGREES = 360

class Planet (Sprite):
    def random_walk (self, divisions=90, pos:tuple=(0,0)):
        if self.steps > DEGREES/divisions:
            self.steps = 0
            self.direction = -1 if np.random.randint(2) else 1
        self.rotate(1, pos)
        self.steps += 1
