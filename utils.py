from math import sin,cos, pi, atan
import pygame 

START = 10
END = 0
STEPS = 60
SCALE = 7
RADIUS = 51*SCALE
SIZE = (1900, 1000)
CENTER = tuple(map( lambda x,y:y*x,SIZE, (0.5,0.5)))
print(CENTER)

def create_graph (screen,rect, radius, steps):
    for i in range(steps):
        x,y = get_point_on_earth(rect.center, i, steps, radius)
        draw_dot(screen,(x,y))

def draw_dot(screen, loc ,color="#f6cd26", dot_radius : int = 4):
    pygame.draw.circle(screen, color, loc , dot_radius)

def get_point_on_earth(center,i,steps,radius):
        theta = i*(2*pi/steps)
        y = radius * sin(theta) + center[1]
        x = radius * cos(theta) + center[0]

        return x,y

def make_elementary_points(screen,center,start,end,steps,radius,start_color=(0,255,128),end_color=(255,0,0)):
    draw_dot(screen, get_point_on_earth(center,start,steps,radius),start_color, dot_radius=8)
    draw_dot(screen, get_point_on_earth(center,end,steps,radius),end_color, dot_radius=8)

def get_angle (p1):
    if not p1[0]: p1 = (0.000001,p1[1])
    return atan (p1[1]/p1[0])

