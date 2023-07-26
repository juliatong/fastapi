from models import Base, Record
from connect import engine


def _add_tables():
    return Base.metadata.create_all(bind=engine)

_add_tables()