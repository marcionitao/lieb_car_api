import uuid
from sqlalchemy import Column, Integer, String, Text
from lieb_car_api.database import Base

class Car(Base):
  __tablename__ = 'cars'
  
  id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
  brand = Column(String, nullable=False)
  model = Column(String, nullable=False)
  color = Column(String, nullable=True)
  factory_year = Column(Integer, nullable=True)
  model_year = Column(Integer, nullable=True)
  description = Column(Text, nullable=True)