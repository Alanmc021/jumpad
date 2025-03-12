# from fastapi import APIRouter
# from app.models.numbers import Numbers
# from app.controllers.math_controller import handle_sum, handle_average

# router = APIRouter()

# @router.post("/sum")
# def sum_values(numbers: Numbers):
#     return handle_sum(numbers)

# @router.post("/average")
# def average_values(numbers: Numbers):
#     return handle_average(numbers)


from fastapi import APIRouter
from app.models.numbers import MathRequest

router = APIRouter()

@router.post("/sum")
def sum_numbers(request: MathRequest):
    return {"result": sum(request.numbers)}

@router.post("/average")
def average_numbers(request: MathRequest):
    return {"result": sum(request.numbers) / len(request.numbers) if request.numbers else 0}
