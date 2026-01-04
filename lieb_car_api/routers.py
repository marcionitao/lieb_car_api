from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from lieb_car_api.database import get_session
from lieb_car_api.models import Car
from lieb_car_api.schemas import CarList, CarPublic, CarSchema

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post(
    '/', response_model=CarPublic, status_code=status.HTTP_201_CREATED
)
def create_car(
    car: CarSchema,
    session: Session = Depends(get_session),  # noqa: B008
):
    # Converte o objeto Pydantic(CarSchema) em um objeto SQLAlchemy(Car) que a DB entende
    car = Car(**car.model_dump())
    session.add(car)
    session.commit()
    session.refresh(car)
    return car


@router.get(path='/', response_model=CarList, status_code=status.HTTP_200_OK)
def list_cars(
    session: Session = Depends(get_session),  # noqa: B008
    offset: int = 0,  # a partir zero
    limit: int = 100,  # traga 100 resultados
):
    # session.scalars busca na Table Car usando paginação
    query = session.scalars(select(Car).offset(offset).limmit(limit))
    cars = query.all()  # busque todos os carros
    return {'cars': cars}


@router.get(
    path='/{car_id}', response_model=CarPublic, status_code=status.HTTP_200_OK
)
def get_car(car_id: int, session: Session = Depends(get_session)):  # noqa: B008
    car = session.get(Car, car_id)
    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Car not found'
        )
    return car
