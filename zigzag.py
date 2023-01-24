import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def main ():
    x,y = show_sprite()
    plot(x,y)

def show_sprite():
    img = mpimg.imread('sprite64x64.png')
    imgplot = plt.imshow(img)
    return [],[]
def zigzag(f1=lambda x: 2*x, f2=lambda x:20-2*x):
    x = []
    y = []
    for i in range(20):
        x.append(i*5)
        if i%2: y.append(10)
        else:   y.append(0)

    return x,y

def plot (x,y):
    plt.gca().set_aspect('equal')
    plt.plot(x,y)
    anotate_plot(x,y)
    plt.show()

def anotate_plot(x,y):
    for xy in zip(x,y):
        plt.annotate('(%d, %d)'%xy,xy=xy)

if __name__ == "__main__":
    main()
