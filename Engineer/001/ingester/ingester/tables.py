from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://user:password@db/parking", future=True)
session = Session(engine)
Base = declarative_base()


class Parking(Base):
    __tablename__ = "parkings"

    id = Column(Integer, primary_key=True)
    public_equipment_id = Column(Integer, nullable=False)
    parking_name = Column(String)
    parking_code = Column(String)
    hour = Column(DateTime)
    user_category = Column(String)
    occupancy = Column(Integer)
