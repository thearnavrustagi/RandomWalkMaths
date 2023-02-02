import sys, pygame
from pygame.locals import *
from planet import Planet
from sprite import Sprite
from arrow import Arrow
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
font = pygame.font.Font('./font.tff',24)
screen = pygame.display.set_mode(size)
decisions = dict({'left':0,'right':0})
planet = Planet ("./sprites/Planets/p2.png", scale=scale, ypadding=0)
player = Sprite('./sprites/kangaroo128x128.png', steps=START)

l_arrow = Arrow('./sprites/Arrows/l-0.png', alt_path = './sprites/Arrows/l-1.png', scale=80, rect=(width - 200, height - 100))
r_arrow = Arrow('./sprites/Arrows/r-0.png', alt_path = './sprites/Arrows/r-1.png', scale=80, rect=(width - 110, height - 100))


def main ():
    initialise()
    start_render()

def initialise():
    global background
    rect = background.get_rect()
    myscale = SIZE[0] / rect.height
    myscale = tuple(map(lambda x,y:x*y,(myscale,myscale),rect.size))
    background = pygame.transform.scale(background, myscale)
    pass

def start_render ():
    global steps, planet, player, screen, font, decisions
    graph_color = "#f792e3"
    background_color=(16,0,16)
    clock = pygame.time.Clock()
    itr = 0

    count = 4

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        clock.tick(60)

        where = 'left' if player.new_angle > player.angle else 'right'
        decisions[where] += 1

        if where == 'left' : 
            if count == 4 : l_arrow.press()
            if count == 1 : l_arrow.press()
        else : 
            if count == 4 : r_arrow.press()
            if count == 1 : r_arrow.press()

        l_text = font.render(f"LEFT", True, graph_color)
        l_textRect = l_text.get_rect()
        l_textRect.center = (width - 160, height - 125)
        r_text = font.render(f"RIGHT", True, graph_color)
        r_textRect = r_text.get_rect()
        r_textRect.center = (width - 70, height - 125)

        l_text_c = font.render(f"{decisions['left']//4}", True, graph_color)
        l_textRect_c = l_text_c.get_rect()
        l_textRect_c.center = (width - 160, height - 155)
        r_text_c = font.render(f"{decisions['right']//4}", True, graph_color)
        r_textRect_c = r_text_c.get_rect()
        r_textRect_c.center = (width - 70, height - 155)



        player.random_walk(steps)
        planet.origin(size)

        screen.blit(background,(0,0))
        planet.blit(screen)
        create_graph(screen,planet.rect,radius,steps)
        make_elementary_points(screen,planet.rect.center,10,0,steps,radius)
        screen.blit(l_text, l_textRect)
        screen.blit(r_text, r_textRect)
        screen.blit(l_text_c, l_textRect_c)
        screen.blit(r_text_c, r_textRect_c)
        l_arrow.animate_and_blit(screen)
        r_arrow.animate_and_blit(screen)
        player.animate_and_blit(screen)
        
        
        

        l_bar = calc_bar_height(decisions, 'left')
        r_bar = calc_bar_height(decisions, 'right')

        pygame.draw.rect(screen, graph_color, pygame.Rect(width - 190, height - 170 - l_bar, 60, l_bar))
        pygame.draw.rect(screen, graph_color, pygame.Rect(width - 100, height - 170 - r_bar, 60, r_bar))

        # Checking if The Sprite has gone back to the original position
        if player.steps % STEPS == 0 : 
            print("BACK to Origin It Seems! Strangeeee...")
            break
        pygame.display.flip()
        itr += 1
        count -= 1

        if count == 0 : count = 4 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

def draw_edge (i,color,_from=910,_to=890):
    pygame.draw.line(screen,color,(i,_from),(i,_to))

def draw_plot (data):
    direction = list(data.keys())
    values = list(data.values())
    plt.bar(direction,values, color = "purple", width = 0.5)
    plt.show()

if __name__ == "__main__":
    main()
