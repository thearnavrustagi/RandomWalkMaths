import matplotlib.pyplot as plt
import numpy as np

def steps (m,n): return [i*(n-i) for i in m]

with open("random_posn.txt") as file:
    y2= steps(np.linspace(1,99,100),100)
    data = [float(num) for num in file.read().splitlines()]
    plt.plot(data,"r")
    plt.plot(y2,"c")
    plt.xlabel("starting position")
    plt.ylabel("number of moves")
    plt.show()
