#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if last_digit > 5:
    print("Last digit of {} and is greater than 5".format(last_digit))
elif last_digit == 0 :
    print("Last digit of {} and is 0".format(last_digit))
elif last_digit < 6 & last_digit > 0:
    print("Last digit of {} and is less than 6 and not 0".format(last_digit))
