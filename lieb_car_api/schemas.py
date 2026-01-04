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


# schema de envio de dados optcionais para alterar apenas 1 valor (@router.patch)
class CarPartialUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    color: Optional[str] = None
    factory_year: Optional[int] = None
    model_year: Optional[int] = None
    description: Optional[str] = None


# schema que lista uma lista de dados
class CarList(BaseModel):
    cars: list[CarPublic]
