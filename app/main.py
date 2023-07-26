from fastapi import FastAPI, Request
import pymysql.cursors
import utils
from connect import SessionLocal
import uvicorn
from models import Record


app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OKabc"}


# @app.post("/data")
# async def load_csv(request: Request):
def load_csv():
    data_to_insert=utils.load_csv()
    for obj in data_to_insert:
        print("in the list: "+ obj.OPEN+ obj.CLOSE+","+obj.HIGH)

    db =  db = SessionLocal()
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

        record_string = json.dumps(records_list, default=utils.record_to_json, indent=4)
        return record_string
    finally:
        # Close the session to release resources
        db.close()





load_csv()
# get_all_records()




