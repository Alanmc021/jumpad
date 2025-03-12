import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app.models.numbers import MathRequest

def test_math_request_valid():
    """Testa se a classe MathRequest aceita uma lista válida de números."""
    data = MathRequest(numbers=[1, 2, 3, 4])
    assert data.numbers == [1, 2, 3, 4]

def test_math_request_empty():
    """Testa se a classe MathRequest rejeita uma lista vazia."""
    with pytest.raises(ValueError, match="A lista de números não pode estar vazia"):
        MathRequest(numbers=[])

def test_math_request_invalid():
    """Testa se a classe MathRequest lança erro ao receber valores inválidos."""
    with pytest.raises(ValueError):
        MathRequest(numbers=["a", "b", "c"])  # Deve falhar, pois não são números

def test_math_request_negative_numbers():
    """Testa se a classe MathRequest aceita números negativos."""
    data = MathRequest(numbers=[-5, -10, -15])
    assert data.numbers == [-5, -10, -15]
