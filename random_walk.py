from random import randint
from sys import argv

og_posn = 10
steps = 100
tot = 0
runs = 100

if argv[1] == "steps": 
    steps = int(argv[2])
    og_posn = steps//2
elif argv[1] == "posn":
    og_posn = int(argv[2])


if __name__ == "__main__":
    for _ in range(runs):
        posn = og_posn
        while True:
            if not posn: break
            move = 1 if randint(0,1) else -1
            posn = (posn + move)%steps
            tot += 1
    print(tot/runs)
