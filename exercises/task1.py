from typing import *


def is_the_same(input_list: List[any]) -> bool:
    is_same = True
    for x in range(len(input_list)):
        if input_list[x] != input_list[0]:
            is_same = False

    return is_same


assert is_the_same([1, 1, 1]) == True
assert is_the_same([1, 2, 1]) == False
assert is_the_same([True]) == True
assert is_the_same(['blue', 'blue']) == True
assert is_the_same([2, 'red']) == False
print("Success")
