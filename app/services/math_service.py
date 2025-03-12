from typing import List

class MathService:
    @staticmethod
    def sum_numbers(numbers: List[float]) -> float:
        return sum(numbers)

    @staticmethod
    def calculate_average(numbers: List[float]) -> float:
        return sum(numbers) / len(numbers) if numbers else 0
