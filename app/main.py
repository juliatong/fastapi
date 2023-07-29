from fastapi import Depends, FastAPI, Request, UploadFile, File
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import text
from sqlalchemy.sql import func
from fastapi_pagination import Page, add_pagination, paginate, LimitOffsetPage
# from schema import RecordOutput
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


@app.get("/data")
def get_records(symbol: str = None,  page_num: int = 1, page_size: int = 10, sort_column: str = None, token: str = Depends(oauth2_scheme)):   
    db = SessionLocal()
    try:
        query = db.query(Record)
        # filter
        if symbol:
            query=query.filter_by(SYMBOL=symbol)
        # sort
        if sort_column:
            query=query.order_by(text(sort_column))    
        # pagination    
        skip=(page_num-1) * limit
        limit=page_size
        query=query.offset(skip).limit(limit)

        # response in json
        all_data = query.all()
        records_dicts = [record_to_dict(record) for record in all_data]
        return records_dicts
    finally:
        db.close()


# aggregation
# @app.get("/data/aggregate")
# def get_all_records_limit(token: str = Depends(oauth2_scheme), group_by_column: str = None):
#     db = SessionLocal()
#     try:
#         query = db.query(Record, func.sum(Record.OPEN))

#         if group_by_column:
#             query = query.group_by(text(group_by_column))

#         all_data = query.all()
#         records_dicts = [record_to_dict(record) for record in all_data]
#         return records_dicts
#     finally:
#         db.close()










