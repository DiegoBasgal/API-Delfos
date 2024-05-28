from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException
from services import SignalService, SignalDataService
from schemas import SignalCreateInput, SignalDataInput, ReturnMessage, ErrorMessage, SignalListOutput


signal_router = APIRouter(prefix='/signal')
assets_router = APIRouter(prefix='/assets')

# SIGNAL
@signal_router.post('/create', response_model=ReturnMessage, responses={400: {'model': ErrorMessage}})
async def create_signal(signal_input: SignalCreateInput):
    try:
        await SignalService.create_signal(name=signal_input.name)
        return ReturnMessage(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@signal_router.delete('/delete/{signal_id}', response_model=ReturnMessage, responses={400: {'model': ErrorMessage}})
async def delete_signal(signal_id: int):
    try:
        await SignalService.delete_signal(signal_id)
        return ReturnMessage(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


# DATA
@signal_router.post('/data/add', response_model=ReturnMessage, responses={400: {'model': ErrorMessage}})
async def create_signal_data(signal_data_input: SignalDataInput):
    try:
        await SignalDataService.add_data(timestamp=signal_data_input.timestamp, value=signal_data_input.value, signal_id=signal_data_input.signal_id)
        return ReturnMessage(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@signal_router.delete('/data/remove/{signal_id}', response_model=ReturnMessage, responses={400: {'model': ErrorMessage}})
async def remove_signal_data(signal_id: int, value: float):
    try:
        await SignalDataService.remove_data(signal_id=signal_id, value=value)
        return ReturnMessage(message='OK')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@signal_router.get('/list', response_model=List[SignalListOutput], responses={400: {'model': ErrorMessage}})
async def signal_list():
    try:
        return await SignalService.list_signal()
    except Exception as error:
        raise HTTPException(400, detail=str(error))