import matplotlib.pyplot as plt

with open("random_gridlength.txt") as file:
    data = [float(num) for num in file.read().splitlines()]
    plt.plot(data,"r")
    plt.xlabel("gridlength")
    plt.ylabel("number of moves")
    plt.show()
