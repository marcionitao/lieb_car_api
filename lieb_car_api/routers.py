from fastapi import APIRouter, status

from lieb_car_api.schemas import CarPublic, CarSchema

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post(
    '/', response_model=CarPublic, status_code=status.HTTP_201_CREATED
)
def create_car(car: CarSchema):
    return car
