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


def main() -> GeneratorType:
    interval_amount: int = get_input(int)
    total_sum: int = get_input(int)
    intervals: list[int] = get_input(int, ' ')

    # checking stuff
    if (0 > interval_amount or interval_amount > 100000) \
        or (0 > total_sum or total_sum > 1000000) :
        
        return
    
    [0, 2, 1, 0, 1]
    pointer = 1

    # Process data 
    valid_intervals: int = 0
    current_interval: list[int] = []
    enumerated_list: dict = {k:v for k, v in enumerate(intervals)}

    current_pointer = 0
    done = False
    solutions = []
    while not done:
        current_interval = []
        for loop_index in range(interval_amount):
            if loop_index+current_pointer not in enumerated_list:
                done = True
                break
            
            if loop_index == 0 and current_pointer > 0:
                current_interval.append(enumerated_list[loop_index+current_pointer-1])
            
            current_interval.append(enumerated_list[loop_index+current_pointer])
            
            if sum(current_interval) > total_sum:
                current_pointer += 1
                break
            
            if sum(current_interval) == total_sum and current_interval not in solutions:
                valid_intervals += 1                
                if len(current_interval) == interval_amount:
                    done = True
                    break
                solutions.append(current_interval)
                if loop_index != interval_amount-1:
                    if loop_index+current_pointer+1 in enumerated_list:
                        if sum(current_interval) + enumerated_list[loop_index+current_pointer+1] == total_sum:
                            sol = [*current_interval, enumerated_list[loop_index+current_pointer+1]]
                            if sol not in solutions:
                                valid_intervals += 1
                current_pointer += 1
                break
          
    yield solutions
    yield valid_intervals

if __name__ == '__main__':
    for i in main():
        print(i)