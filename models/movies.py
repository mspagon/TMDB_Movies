from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Movies(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)

# test