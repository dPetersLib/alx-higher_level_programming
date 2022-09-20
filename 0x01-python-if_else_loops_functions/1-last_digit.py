#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = int(str(number)[-1])
if ld > 5:
    p = 'greater than 5'
elif ld < 6 and ld != 0:
    p = 'less than 6 and not 0'
else:
    p = 'zero'
print(f"Last digit of {number} is {ld} and is {p}")
