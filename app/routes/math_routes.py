from fastapi import APIRouter
from app.models.numbers import MathRequest

router = APIRouter()

@router.post("/sum")
def sum_numbers(request: MathRequest):
    return {"result": sum(request.numbers)}

@router.post("/average")
def average_numbers(request: MathRequest):
    return {"result": sum(request.numbers) / len(request.numbers) if request.numbers else 0}
