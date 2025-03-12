# from pydantic import BaseModel, Field, ConfigDict
# from typing import List

# class MathRequest(BaseModel):
#     numbers: List[float] = Field(..., description="List of numbers to be processed")

#     model_config = ConfigDict(json_schema_extra={
#         "example": {
#             "numbers": [1.2, 3.4, 5.6]
#         }
#     })

# from pydantic import BaseModel, Field, field_validator
# from typing import List

# class MathRequest(BaseModel):
#     numbers: List[float] = Field(..., description="Lista de números a serem processados")

#     @field_validator("numbers")
#     @classmethod
#     def validate_numbers(cls, v):
#         if not v:
#             raise ValueError("A lista de números não pode estar vazia")
#         if any(not isinstance(n, (int, float)) for n in v):
#             raise ValueError("Todos os valores devem ser números (int ou float)")
#         return v

#     class Config:
#         json_schema_extra = {
#             "example": {"numbers": [1.2, 3.4, 5.6]}
#         }


from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import List

class MathRequest(BaseModel):
    numbers: List[float] = Field(..., description="Lista de números a serem processados")

    @field_validator("numbers")
    @classmethod
    def validate_numbers(cls, v):
        if not v:
            raise ValueError("A lista de números não pode estar vazia")
        if any(not isinstance(n, (int, float)) for n in v):
            raise ValueError("Todos os valores devem ser números (int ou float)")
        return v

    model_config = ConfigDict(
        json_schema_extra={"example": {"numbers": [1.2, 3.4, 5.6]}}
    )