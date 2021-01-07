# Chance Sim by JayDev
# Thanks for checking it out!
from random import seed
from random import random
from random import randint
main = True
s = 1
winx = 0
print("Random Chance Simulator V1 by JayDev")
while main:
    r1 = input("Randint1:")
    r2 = input("Randint2:")
    x = input("Amount of simulations:")
    print("Note: Showing numbers will greatly slow down sim speed but shows more data.")
    setting = input("Show numbers?(y/n):")
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
            print('You won!')
            winx += 1
    print('With a', r1, "in", r2, "chance, you won", winx, "times after", x, "simulations.")
    winx = 0
