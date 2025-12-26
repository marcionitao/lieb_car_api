from fastapi import FastAPI

from lieb_car_api.routers import router as cars_router

app = FastAPI(
  title='Lieb Car API',
  description='A modern API using FastAPI',
  version='0.1.0'
)
# usando a rota  
app.include_router(cars_router)

@app.get('/')
def read_root():
  return {'status': 'ok', 'message': 'Hello World'}