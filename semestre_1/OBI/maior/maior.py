import itertools
from re import T
from types import GeneratorType
from typing import Any


def get_input(cast: Any, split: str = None):
    while True:
        try:
            inp = input()
            output = [cast(i) for i in inp.split(split)] if split else cast(inp)
        except ValueError:
            continue
        else:
            return output


def main():
    min_value = get_input(int) # N
    max_value = get_input(int) # M
    value_sum = get_input(int) # S

    solutions: list[int] = [-1]
    if 0 > value_sum or value_sum > 36 or 0 > max_value or min_value > max_value or 0 > min_value:
        yield -1
        return
    
    for i in range(min_value, max_value):
        if sum([int(v) for v in str(i)]) == value_sum:
            solutions.append(i)
    yield max(solutions)


for i in main():
    print(i)