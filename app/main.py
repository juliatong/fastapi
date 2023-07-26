from fastapi import FastAPI
import csv
import pymysql.cursors
# from models import Record
# from connect import SessionLocal
import uvicorn


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OKabc"}


# @app.post("/data")
# async def load_csv(request: Request):
#     with open('names.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         data_to_insert = []
#         for row in reader:
#             print(row['UNIX'], row['SYMBOL'])
#             data_to_insert.append(Record(UNIX=row['UNIX'],SYMBOL=row["SYMBOL"] ))

#     db = SessionLocal
#     try:
#         db.add_all(data_to_insert)
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         raise e
#     finally:
#         db.close()

#     return {"message": "CSV data uploaded and inserted into the database."}





