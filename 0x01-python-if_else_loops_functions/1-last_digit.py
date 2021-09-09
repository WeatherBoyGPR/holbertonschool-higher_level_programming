#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is ".format(number), end='')
if (number) < 0:
    numberend = -(-number % 10)
else:
    numberend = number % 10
if (numberend) > 5:
    print("{} and is greater than 5".format(numberend))
elif (number % 10) == 0:
    print("{} and is 0".format(numberend))
else:
    print("{} and is less than 6 and not 0".format(numberend))
