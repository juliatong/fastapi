from fastapi import FastAPI, Request, UploadFile, File
import pymysql.cursors
from utils import record_to_dict, process_csv_file, load_csv, page_result
from connect import SessionLocal
import uvicorn
from models import Record
import json
from create_tables import create_table
import logging



# Enable logging for SQL statements
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     create_table()

@app.get("/")
def hello_world():
    return {"message": "OK"}


# @app.post("/data")
# async def upload_csv(file: UploadFile = File(...)):
#     contents = await file.read()
#     data_to_insert=await process_csv_file(contents)
def upload_csv():
    data_to_insert=load_csv()
    # Starting from here, to perform any additional processing on the CSV data
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
def get_all_records(page_num: int = 1, page_size: int = 10):
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
def get_symbol_path_variable_records(symbol: str):   
    db = SessionLocal()
    try:
        # Fetch all data from the database using the query method of the session
        print("path variable++",symbol)
        data_symbol = db.query(Record).filter_by(SYMBOL=symbol)
        # for data with symbol:
        # for data in data_symbol:
        #     print(data.UNIX , data.SYMBOL)

        records_dicts = [record_to_dict(record) for record in data_symbol]
        # Return the list of dictionaries as the response
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






# upload_csv()






