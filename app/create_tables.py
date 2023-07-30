from models import Base, Record
from datetime import datetime
from connect import engine
from db_manager import DBManager
from connect import SessionLocal

def create_table():
    return Base.metadata.create_all(bind=engine)

    
def populate_table():
    record1= Record(UNIX=datetime(2022, 2, 16, 0, 21, 40), SYMBOL='XRPEUR', OPEN=42123.290000000, CLOSE= 42146.060000000, HIGH= 42148.320000000, LOW= 42120.820000000)
    record2=Record(UNIX=datetime(2023, 2, 15, 18, 26, 0), SYMBOL='ADAEUR', OPEN=42123.290000000, CLOSE= 42146.060000000, HIGH= 42148.320000000, LOW= 42120.820000000)

    db = SessionLocal()
    db.add_all([record1, record2])
    db.commit()
    db.close()

create_table()
populate_table()