from datetime import datetime
from pydantic import BaseModel
from typing import List


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


class Data(BaseModel):
    id: int
    timestamp: datetime
    value: float
    signal_id: int

    class Config:
        from_attributes = True


class SignalListOutput(BaseModel):
    id: int
    name: str
    data: List[Data]

    class Config:
        from_attributes = True