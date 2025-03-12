from typing import List

def sum_numbers(values: List[int]) -> int:
    return sum(values)

def calculate_average(values: List[int]) -> float:
    if len(values) == 0:
        return 0
    return sum(values) / len(values)
