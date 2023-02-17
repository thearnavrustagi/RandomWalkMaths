import matplotlib.pyplot as plt
import numpy as np

def steps(m,n): return [i*(j-i) for i,j in zip(m,n)]

with open("random_gridlength.txt") as file:
    y2 = steps(np.linspace(1,50,100),np.linspace(1,100,100))
    data = [float(num) for num in file.read().splitlines()]
    plt.plot(data,"r")
    plt.plot(y2,"c")
    plt.xlabel("gridlength")
    plt.ylabel("number of moves")
    plt.show()
