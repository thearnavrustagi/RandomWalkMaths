import sys, pygame
from pygame.locals import *
from sprite import Sprite
from numpy import random
import matplotlib.pyplot as plt

size = width, height = 1500, 960

pygame.init()
font = pygame.font.Font('./font.tff',96)
screen = pygame.display.set_mode(size)
monkey = Sprite("sprites/sprite2-128x128.png",size)
memory = dict({'left':0,'right':0})

def main ():
    initialise()
    try:
        start_render()
    except KeyboardInterrupt:
        draw_plot(memory)

def initialise():
    monkey.origin()
    planet_sprites = []

    # for i in range(1,7):
    #     planet_sprites.append(pygame.image.load(f"sprites/Frames/Pixel Earth{i}.png"))

    return planet_sprites

def start_render ():
    global memory
    graph_color = (0,255,100)
    background_color=(16,0,16)
    clock = pygame.time.Clock()
    itr = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        clock.tick(60)

        monkey.random_walk()

        where = 'left' if monkey.old_position > monkey.position else 'right'
        memory[where] += 1

        text = font.render(f"moving {where}", True, graph_color)
        textRect = text.get_rect()
        textRect.center = (width//2,96)

        screen.fill(background_color)
        draw_graph(screen, graph_color)
        monkey.blit(screen)
        screen.blit(text, textRect)

        # screen.blit(planet_sprites[itr%6],(128,128))
        
        draw_edge(monkey.target[0],(255,50,50),940,860)
        # draw_nescafe(screen,monkey.target[0],820)

        pygame.display.flip()
        itr += 1

def draw_graph(screen,color):
    pygame.draw.line(screen, color,(0,900),(1500,900))
    for i in range(0,1500,15):
        draw_edge(i,color)

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
