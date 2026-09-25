from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase    

DATABASE_URL = "postgresql+psycopg://azure@localhost/congregation_reporting"
engine=create_engine(DATABASE_URL)
sessionLocal=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)
class Base(DeclarativeBase):
    pass

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()