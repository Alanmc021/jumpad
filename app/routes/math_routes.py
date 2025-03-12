from fastapi import APIRouter
from app.controllers.math_controller import MathController
from app.models.numbers import MathRequest

router = APIRouter()

@router.post(
    "/sum",
    summary="Sum numbers",
    description="Receives a list of numbers and returns their sum.",
    response_model=dict,
    responses={
        200: {"description": "Successful Response", "content": {"application/json": {"example": {"operation": "sum", "result": 10}}}},
        400: {"description": "Bad Request - Invalid input", "content": {"application/json": {"example": {"detail": "List of numbers cannot be empty"}}}},
    }
) 
def sum_numbers(request: MathRequest):
    """Calculate the sum of a list of numbers."""
    return MathController.handle_sum(request)

@router.post(
    "/average",
    summary="Calculate average",
    description="Receives a list of numbers and returns their average.",
    response_model=dict,
    responses={
        200: {"description": "Successful Response", "content": {"application/json": {"example": {"operation": "average", "result": 5.5}}}},
        400: {"description": "Bad Request - Invalid input", "content": {"application/json": {"example": {"detail": "List of numbers cannot be empty"}}}},
    }
)
def average_numbers(request: MathRequest):
    """Calculate the average of a list of numbers."""
    return MathController.handle_average(request)
