from datetime import datetime
from pydantic import BaseModel


class SignalCreateInput(BaseModel):
    name: str

class SignalDataInput(BaseModel):
    timestamp: datetime
    signal_id: int
    value: float


class ReturnMessage(BaseModel):
    message: str

class ErrorMessage(ReturnMessage):
    detail: str