import sys, pygame
from pygame.locals import *
from planet import Planet
from sprite import Sprite
from animal import Animal
from numpy import random
import matplotlib.pyplot as plt
from math import sin, cos, pi
from utils import *

size = width, height = SIZE
scale = SCALE
steps = STEPS
radius = RADIUS
background = pygame.image.load('./sprites/Space.png')

pygame.init()
font = pygame.font.Font('./font.tff',96)
screen = pygame.display.set_mode(size)
decisions = dict({'left':0,'right':0})
planet = Planet ("./sprites/Planets/Planet.png", scale=scale, ypadding=0)
player = Sprite('./sprites/kangaroo128x128.png')

def main ():
    initialise()
    start_render()

def initialise():
    global player
    pass

def start_render ():
    global steps, planet, player, screen, font
    graph_color = (0,255,100)
    background_color=(16,0,16)
    clock = pygame.time.Clock()
    itr = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        clock.tick(24)

        where = 'left' if player.new_angle > player.angle else 'right'
        decisions[where] += 1
        text = font.render(f"moving {where}", True, graph_color)
        textRect = text.get_rect()
        textRect.center = (width//2,45)

        player.random_walk(steps)
        planet.origin(size)

        screen.fill(background_color)
        screen.blit(background,(0,0))
        planet.blit(screen)
        create_graph(screen,planet.rect,radius,steps)
        make_elementary_points(screen,planet.rect.center,10,0,steps,radius)
        screen.blit(text, textRect)
        player.animate_and_blit(screen)

        # Checking if The Sprite has gone back to the original position
        if planet.net_rotation in (0, 360) : 
            pass
        pygame.display.flip()
        itr += 1

def draw_edge (i,color,_from=910,_to=890):
    pygame.draw.line(screen,color,(i,_from),(i,_to))

def draw_plot (data):
    direction = list(data.keys())
    values = list(data.values())
    plt.bar(direction,values, color = "purple", width = 0.5)
    plt.show()

if __name__ == "__main__":
    main()
