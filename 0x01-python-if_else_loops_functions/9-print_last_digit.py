#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ld = 0 - (abs(number) % 10)
    else:
        ld = number % 10
    return ld
