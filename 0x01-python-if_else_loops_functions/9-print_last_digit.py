#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        return - (abs(number) % 10)
    elif number == 0:
        return '00'
    return number % 10
