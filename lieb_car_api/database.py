from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///cars.db'

engine = create_engine(DATABASE_URL)

# cria uma sessäo na DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# função do SQLAlchemy que cria uma classe base especial.
Base = declarative_base()
# cria a sessäo e usa
def get_session():
  session = SessionLocal() 
  try:
    yield session
  finally:
    session.close()