from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, DECIMAL

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    timestamp = Column(DateTime, primary_key=True)
    wind_speed = Column(DECIMAL)
    power = Column(DECIMAL)
    ambient_temperature = Column(DECIMAL)