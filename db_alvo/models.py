from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey


Base = declarative_base()

class Signal(Base):
    __tablename__ = 'signal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    datas = relationship('Data', backref='signal', lazy='subquery')

class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime)
    value = Column(DECIMAL)
    signal_id = Column(Integer, ForeignKey('signal.id'))