from app.services.math_service import sum_numbers, calculate_average
from app.models.numbers import Numbers

def handle_sum(numbers: Numbers):
    result = sum_numbers(numbers.values)
    return {"operation": "sum", "result": result}

def handle_average(numbers: Numbers):
    result = calculate_average(numbers.values)
    return {"operation": "average", "result": result}
