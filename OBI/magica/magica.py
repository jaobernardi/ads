from re import T
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
    dimension = get_input(int)     # N
    line_1 = get_input(int, ' ')   # X1
    line_2 = get_input(int, ' ')   # X2
    line_3 = get_input(int, ' ')   # X2
    matrix = [line_1, line_2, line_3]
    sums = [sum(line_1), sum(line_2), sum(line_3)]
    missing_line_sum = min(sums)
    if dimension < 3 or dimension > 10:
        return
    
    for line, sum_value in enumerate(sums):
        if sum_value == missing_line_sum:
            for col, value in enumerate(matrix[line]):
                if value == 0:
                    yield max(sums)-min(sums)
                    yield line+1
                    yield col+1


if __name__ == "__main__":
    for i in main():
        print(i)