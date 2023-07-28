from fastapi import Depends, FastAPI, Request, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from typing import List
import pymysql.cursors  
from utils import record_to_dict, process_csv_file, load_csv, page_result
from connect import SessionLocal
import uvicorn
from models import Record
import json
# from create_tables import create_table
import subprocess
import logging



# Enable logging for SQL statements
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def generate_token(form_data:  OAuth2PasswordRequestForm = Depends()):
     return {"access_token": form_data.username, "token_type": "bearer"}

@app.get("/")
def hello_world():
    return {"message": "OK"}


@app.post("/data")
async def upload_csv(files: List[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        data_to_insert=await process_csv_file(contents)
        db = SessionLocal()
        try:
            db.add_all(data_to_insert)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    return {"message": "CSV data uploaded and inserted into the database."}


# pagination with default value
@app.get("/data")
def get_all_records(token: str = Depends(oauth2_scheme), page_num: int = 1, page_size: int = 10):
    db = SessionLocal()
    try:
        # Fetch all data from the database using the query method of the session
        all_data = db.query(Record).all()
        records_dicts = [record_to_dict(record) for record in all_data]
        # Return the list of dictionaries as the response
        paged_response=page_result(records_dicts, page_num, page_size)
        return paged_response
    finally:
        db.close()



# path variable query
@app.get("/data/{symbol}")
def get_symbol_path_variable_records(symbol: str, token: str = Depends(oauth2_scheme)):   
    db = SessionLocal()
    try:
        data_symbol = db.query(Record).filter_by(SYMBOL=symbol)
        # for data with symbol:
        # for data in data_symbol:
        #     print(data.UNIX , data.SYMBOL)

        records_dicts = [record_to_dict(record) for record in data_symbol]
        return records_dicts
    finally:
        db.close()

# TODO: offset/cursor based pagination

# TODO: query parameter query
# @app.get("/data")
# def get_symbol_query_parameter_records(symbol: str):
#     db = SessionLocal()
#     try:
#         # Fetch all data from the database using the query method of the session
#         if symbol:
#             print("query parameter--")
#             tmp={ "symbol": symbol}
#             print(tmp)
#         data_symbol = db.query(Record).filter_by(SYMBOL=symbol)
#         records_dicts = [record_to_dict(record) for record in data_symbol]
#         # Return the list of dictionaries as the response
#         return records_dicts
#     finally:
#         db.close()

# 






