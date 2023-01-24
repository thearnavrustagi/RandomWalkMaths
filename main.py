import sys, pygame
from pygame.locals import *
from planet import Planet
from animal import Animal
from numpy import random
import matplotlib.pyplot as plt

size = width, height = 1900,1000

pygame.init()
font = pygame.font.Font('./font.tff',96)
screen = pygame.display.set_mode(size)
steps = dict({'left':0,'right':0})
planet = Planet ("./sprites/Planets/Planet.png", scale=7, ypadding=40)

def main ():
    initialise()
    start_render()

def initialise():
    pass

def start_render ():
    global steps
    graph_color = (0,255,100)
    background_color=(16,0,16)
    clock = pygame.time.Clock()
    itr = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        

        clock.tick(60)

        planet.random_walk(12 , size)

        where = 'left' if planet.direction > 0 else 'right'

        text = font.render(f"moving {where}", True, graph_color)
        textRect = text.get_rect()
        textRect.center = (width//2,45)

        screen.fill(background_color)
        planet.blit(screen)
        screen.blit(text, textRect)
        

        # Checking if The Sprite has gone back to the original position
        if planet.net_rotation in (0, 360) : 
            print("Back to Origin!")
            break
        print(planet.net_rotation)

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
