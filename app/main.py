from fastapi import FastAPI, Request, UploadFile, File
import pymysql.cursors
from utils import record_to_dict, process_csv_file
from connect import SessionLocal
import uvicorn
from models import Record
import json


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OKabc"}


@app.post("/data")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    data_to_insert=await process_csv_file(contents)

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


@app.get("/data")
def get_all_records():
    db = SessionLocal()
    try:
        # Fetch all data from the database using the query method of the session
        all_data = db.query(Record).all()
        for data in all_data:
            print(data.UNIX , data.SYMBOL)

        records_dicts = [record_to_dict(record) for record in all_data]
        # Return the list of dictionaries as the response
        return records_dicts
    finally:
        # Close the session to release resources
        db.close()


# load_csv()




