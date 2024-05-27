from datetime import datetime

from db_alvo.models import Signal, Data
from db_alvo.connector import async_session

from sqlalchemy import delete


class SignalService:
    async def create_signal(name: str):
        async with async_session() as session:
            session.add(Signal(name=name))
            await session.commit()

    async def delete_signal(signal_id: int):
        async with async_session() as session:
            await session.execute(delete(Signal).where(Signal.id==signal_id))
            await session.commit()


class SignalDataService:
    async def add_data(timestamp: datetime, value: float, signal_id: int):
        async with async_session() as session:
            await session.add(Data(timestamp=timestamp, value=value, signal_id=signal_id))
            await session.commit()
