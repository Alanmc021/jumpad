# from pydantic import BaseModel
# from typing import List

# class Numbers(BaseModel):
#     values: List[int]



from pydantic import BaseModel
from typing import List

class MathRequest(BaseModel):
    numbers: List[int]
