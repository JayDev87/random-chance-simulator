# Chance Sim by JayDev
# Thanks for checking it out!
from random import seed
from random import random
from random import randint
import time
main = True
s = 1
winx = 0
print("Random Chance Simulator V2 by JayDev")
while main:
    r1 = input("Randint1:")
    r2 = input("Randint2:")
    x = input("Amount of simulations:")
    print("Note: Showing numbers will greatly slow down sim speed but shows more data.")
    setting = input("Show numbers?(y/n):")
    start = time.strftime('%d/%m/%Y %H:%M:%S')
    r1 = int(r1)
    r2 = int(r2)
    x = int(x)
    for _ in range(x):
        seed(s)
        value = randint(r1, r2)
        if setting == "y":
            print(value)
        s += 1
        if value == 1:
            winx += 1
            print('A number matched to 1. Current matches:', winx)
    print('With a', r1, "in", r2, "chance, there was", winx, "matches after", x, "simulations.")
    print("Start time:", start)
    print("End time:", time.strftime('%d/%m/%Y %H:%M:%S'))
    winx = 0
