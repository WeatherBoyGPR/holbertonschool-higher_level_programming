#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is ".format(number), end='')
if (number % 10) > 0:
    number = -number
if (number % 10) > 5:
    print("{} and is greater than five".format(number % 10))
elif (number % 10) == 0:
    print("{} and is zero".format(number % 10))
else:
    print("{} and is less than 6 and not 0".format(number % 10))
