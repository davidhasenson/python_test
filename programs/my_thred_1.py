from threading import Thread
import time


def my_func(name):
    time.sleep(5)
    print(name)


x = Thread(target=my_func, args=("your_name",), daemon=True)

x.start()
x.join()
