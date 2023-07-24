from fastapi import FastAPI
import csv
import pymysql.cursors


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}


# @app.post("/data")
# def load_csv(request: Request):
#     with open('names.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             print(row['first_name'], row['last_name'])





