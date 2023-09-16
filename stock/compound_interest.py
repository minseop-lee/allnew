from pydantic import BaseModel

class FutureValueInput(BaseModel):
    principal: float
    interest_rate: float
    years: int

# 복리 계산 함수
def calculate_future_value(principal: float, interest_rate: float, years: int) -> float:
    future_value = principal * (1 + interest_rate) ** years
    return future_value