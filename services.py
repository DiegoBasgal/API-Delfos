from httpx import Client
from datetime import datetime
from sqlalchemy import delete
from sqlalchemy.future import select

from db_alvo.models import Signal, Data
from db_alvo.connector import async_session


class SignalService:
    async def create_signal(name: str):
        async with async_session() as session:
            print(name)
            session.add(Signal(name=name))
            await session.commit()

    async def delete_signal(signal_id: int):
        async with async_session() as session:
            await session.execute(delete(Signal).where(Signal.id==signal_id))
            await session.commit()

    async def list_signal():
        async with async_session() as session:
            result = await session.execute(select(Signal))
            signal = result.scalars().all()
            for sig in signal:
                result = await session.execute(select(Data).where(Data.signal_id==sig.id))
                sig.data = result.scalars().all()
            return signal


class SignalDataService:
    async def add_data(timestamp: datetime, value: float, signal_id: int):
        async with async_session() as session:
            print(timestamp, value, signal_id)
            session.add(Data(timestamp=datetime.now(), value=value, signal_id=signal_id))
            await session.commit()

    async def remove_data(signal_id: int, value: float):
        async with async_session() as session:
            await session.execute(delete(Data).where(Data.signal_id==signal_id, Data.value==value))
            await session.commit()