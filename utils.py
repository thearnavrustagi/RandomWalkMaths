from math import sin,cos, pi, atan, log
import pygame 

START = 10
END = 0
STEPS = 60
SCALE = 7
RADIUS = 51*SCALE
SIZE = HEIGHT, WIDTH = (1900, 1000)
CENTER = tuple(map( lambda x,y:y*x,SIZE, (0.5,0.5)))
BAR_HEIGHT = SIZE[1]//5
start_color="#92F7A6"
end_color="#F30C2C"
color="#FFD372"
print(CENTER)

def create_graph (screen,rect, radius, steps):
    for i in range(steps):
        x,y = get_point_on_earth(rect.center, i, steps, radius)
        draw_dot(screen,(x,y))

def draw_dot(screen, loc ,color="#FFD372", dot_radius : int = 4):
    pygame.draw.circle(screen, color, loc , dot_radius)

def get_point_on_earth(center,i,steps,radius):
        theta = i*(2*pi/steps)
        y = radius * sin(theta) + center[1]
        x = radius * cos(theta) + center[0]

        return x,y

def make_elementary_points(screen,center,start,end,steps,radius,start_color="#92F7A6",end_color="#F30C2C"):
    draw_dot(screen, get_point_on_earth(center,start,steps,radius),start_color, dot_radius=8)
    draw_dot(screen, get_point_on_earth(center,end,steps,radius),end_color, dot_radius=8)

def get_angle (p1):
    if not p1[0]: p1 = (0.000001,p1[1])
    return atan (p1[1]/p1[0])

def log_15 (x : int) -> int:
    if x <= 0 : return 0
    return int(log(x)/log(1.01))

def calc_bar_height(decisions : dict, side : str) -> int :
    if decisions[side] <= BAR_HEIGHT : 
        return ( decisions[side] * 100 ) // BAR_HEIGHT
    else :
        return log_15(( decisions[side] * 100 ) // BAR_HEIGHT) - 1.8*BAR_HEIGHT

def __add(a,b):
    return tuple(map(lambda x,y:x+y,a,b))

def render_probability_distribution (screen,posn, probability_distribution,scale=2):
    global color, start_color, end_color
    x = 64
    increment = 7
    points = []
    for i,y in enumerate(probability_distribution):
        point = __add(posn,(x,-y*scale))
        points.append(point)
        x+=increment
        mycolor = color
        if i == START: mycolor = start_color
        if i == END: mycolor = end_color
        draw_dot(screen,point,dot_radius=2,color=mycolor)

    for p1,p2 in zip(points[:-1],points[1:]):
        pygame.draw.line(screen,color,p1,p2)
