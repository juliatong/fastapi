from fastapi import Depends, FastAPI, Request, UploadFile, File, HTTPException
import mimetypes
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import text
from datetime import datetime
from typing import Annotated
from typing import List
import pymysql.cursors  
from utils import record_to_dict, process_csv_file
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
async def upload_csv(files: List[UploadFile] = File(...), token: str = Depends(oauth2_scheme)):
    for file in files:
        # Check if the file is a CSV file based on its content type
        content_type, _ = mimetypes.guess_type(file.filename) 
        if content_type != 'text/csv':
            raise HTTPException(status_code=415, detail="Unsupported Media Type. Only CSV files are allowed.")

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
def get_records(symbol: str = None, from_date: int=None, to_date: int=None, page_num: int = 1, page_size: int = 10, sort_column: str = None, token: str = Depends(oauth2_scheme)):   
    db = SessionLocal()
    try:
        query = db.query(Record)
        # filter
        if symbol:
            query=query.filter_by(SYMBOL=symbol)
        # filter by date range
        if from_date is not None or to_date is not None:
            from_date = to_date if from_date is None else from_date
            to_date = from_date+1000 if to_date is None else to_date
            start_date=datetime.fromtimestamp(from_date/1000)
            end_date=datetime.fromtimestamp(to_date/1000)
            query=query.filter(Record.UNIX.between(start_date, end_date))     
        # sort
        if sort_column:
            query=query.order_by(text(sort_column))    
        # pagination    
        limit = page_size
        skip = (page_num - 1) * limit
        query = query.offset(skip).limit(limit)


        # response in json
        all_data = query.all()
        records_dicts = [record_to_dict(record) for record in all_data]
        return records_dicts
    finally:
        db.close()


# aggregation











