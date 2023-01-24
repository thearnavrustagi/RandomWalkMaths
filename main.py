import sys, pygame
from pygame.locals import *
from planet import Planet
from numpy import random
import matplotlib.pyplot as plt

size = width, height = 1500, 960

pygame.init()
font = pygame.font.Font('./font.tff',96)
screen = pygame.display.set_mode(size)
steps = dict({'left':0,'right':0})
planet = Planet ("./sprites/Planets/Planet.png")

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
        
        clock.tick(6)

        planet.random_walk()
        where = 'left' if planet.direction > 0 else 'right'

        text = font.render(f"moving {where}", True, graph_color)
        textRect = text.get_rect()
        textRect.center = (width//2,96)

        screen.fill(background_color)
        planet.blit(screen)
        screen.blit(text, textRect)

        pygame.display.flip()
        itr += 1

def draw_edge (i,color,_from=910,_to=890):
    pygame.draw.line(screen,color,(i,_from),(i,_to))

# def draw_nescafe (screen, x,y):
#     nescafe = pygame.image.load("./sprites/nescafe.png")
#     nescafe_rect = nescafe.get_rect()
#     nescafe_rect.centerx = x
#     nescafe_rect.centery = y

#     screen.blit(nescafe, nescafe_rect)

def draw_plot (data):
    direction = list(data.keys())
    values = list(data.values())
    plt.bar(direction,values, color = "purple", width = 0.5)
    plt.show()

if __name__ == "__main__":
    main()
