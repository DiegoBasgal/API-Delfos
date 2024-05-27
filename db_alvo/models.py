from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey


Base = declarative_base()

class Signal(Base):
    __tablename__ = 'signal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    datas = relationship('Data', backref='signal')

class Data(Base):
    __tablename__ = 'data'
    timestamp = Column(DateTime, primary_key=True)
    value = Column(DECIMAL)
    signal_id = Column(Integer, ForeignKey('signal.id'))