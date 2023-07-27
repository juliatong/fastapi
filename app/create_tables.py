from models import Base, Record
from connect import engine


def create_table():
    return Base.metadata.create_all(bind=engine)


create_table()