from fastapi import HTTPException
from app.services.math_service import MathService
from app.models.numbers import MathRequest

class MathController:
    @staticmethod
    def handle_sum(request: MathRequest):
        if not request.numbers:
            raise HTTPException(status_code=400, detail="List of numbers cannot be empty")
        if any(not isinstance(num, (int, float)) for num in request.numbers):
            raise HTTPException(status_code=400, detail="All values must be numbers")

        return {"operation": "sum", "result": MathService.sum_numbers(request.numbers)}

    @staticmethod
    def handle_average(request: MathRequest):
        if not request.numbers:
            raise HTTPException(status_code=400, detail="List of numbers cannot be empty")
        if any(not isinstance(num, (int, float)) for num in request.numbers):
            raise HTTPException(status_code=400, detail="All values must be numbers")

        return {"operation": "average", "result": MathService.calculate_average(request.numbers)}
