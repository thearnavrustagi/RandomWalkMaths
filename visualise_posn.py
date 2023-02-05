import matplotlib.pyplot as plt

with open("random_posn.txt") as file:
    data = [float(num) for num in file.read().splitlines()]
    plt.plot(data,"r")
    plt.xlabel("starting steps")
    plt.ylabel("number of moves")
    plt.show()
