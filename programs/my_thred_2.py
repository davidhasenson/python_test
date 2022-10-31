from threading import Thread
from random import randint


def random_add(name, goal):
    result = 0
    while result < goal:
        i = randint(1, 10)
        result += i
    print(f" Thread: {name} sum: {result}")


x = Thread(target=random_add, args=("x", 10000), daemon=True)
y = Thread(target=random_add, args=("y", 10000), daemon=True)

x.start()
y.start()
x.join()
y.join()
