from sprite import Sprite
import pygame
import numpy as np
from utils import SIZE

# Add a rect var and set to fixed pos


class Arrow (Sprite):
    def __init__(self, impath, alt_path : str, scale: int = 1, direction: int = 1, xpadding: int = 0, ypadding: int = 0, steps: int = 0, rect : tuple = (0,0)):
        self.alt_img = pygame.image.load(alt_path)
        super().__init__(impath, scale, direction, xpadding, ypadding, steps, rect)

    def press(self) :
        self.image, self.alt_img = self.alt_img, self.image
        
    def animate(self) : 
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
