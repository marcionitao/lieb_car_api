from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from lieb_car_api.database import get_session
from lieb_car_api.models import Car
from lieb_car_api.schemas import CarPublic, CarSchema

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post(
    '/', response_model=CarPublic, status_code=status.HTTP_201_CREATED
)
# abrir o banco de dados, abrir uma conexão com db, salvar o registo na DB e fechar a conexão
def create_car(
    car: CarSchema,
    session: Session = Depends(get_session),  # noqa: B008
):
    car = Car(
        **car.model_dump()
    )  # Converte o objeto Pydantic (CarSchema) em um objeto SQLAlchemy (Car)
    session.add(car)  # adiciona os dados
    session.commit()  # salva os dados
    session.refresh(car)  # atualiza os dados
    return car
