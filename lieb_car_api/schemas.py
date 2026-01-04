from typing import Optional

from pydantic import BaseModel


# schema de envio de dados sem ID - request
class CarSchema(BaseModel):
    brand: str
    model: str
    color: Optional[str] = None
    factory_year: Optional[int] = None
    model_year: Optional[int] = None
    description: Optional[str] = None


# schema de resposta de dados com ID - response
class CarPublic(CarSchema):
    id: int
    brand: str
    model: str
    color: Optional[str] = None
    factory_year: Optional[int] = None
    model_year: Optional[int] = None
    description: Optional[str] = None


# achma que lista os dados
class CarList(BaseModel):
    cars: list[CarPublic]
