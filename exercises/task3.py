from typing import *
import random

def compare_two_numbers(a: int, b: int):
    if a < b:
        odp = (f'{a} is smaller than {b}')
    elif a > b:
        odp = (f'{a} is greater than {b}')
    elif a == b:
        odp = (f'a is equal b: 0')
    return odp


assert compare_two_numbers(2, 6) == '2 is smaller than 6'
assert compare_two_numbers(4, -5) == '4 is greater than -5'
assert compare_two_numbers(100, 100) == 'a is equal b: 0'


