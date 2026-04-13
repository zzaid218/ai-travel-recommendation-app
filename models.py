from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import declarative_base
from db import engine

Base = declarative_base()

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)
    description = Column(String)
    category = Column(String)
    embedding = Column(LargeBinary)

Base.metadata.create_all(engine)