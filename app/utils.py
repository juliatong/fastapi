import csv
from models import Record
from datetime import datetime
import tempfile
import os


async def process_csv_file (file):
    # Create a temporary file to save the uploaded content
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    try: 
        with open(temp_file.name, "wb") as f:
            f.write(file)
        
        # Process the CSV file from the temporary location
        data_to_insert = []
        with open(temp_file.name, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                print("row inserted from utils.py", row['UNIX'], row['SYMBOL'], row['OPEN'], row['HIGH'], row['LOW'], row['CLOSE'])
                datetime_value = convert_unix_timestamp_milliseconds(row['UNIX'])
                data_to_insert.append(Record(UNIX=datetime_value,SYMBOL=row["SYMBOL"], OPEN=row['OPEN'], CLOSE=row['CLOSE'],HIGH=row['HIGH'],LOW=row['LOW']))
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        # Close and remove the temporary file
        temp_file.close()
        os.unlink(temp_file.name)
    return data_to_insert


# page result set with page num an dpage size
def page_result(data, page_num, page_size):
    data_length=len(data)
    start = (page_num - 1) * page_size
    end = start + page_size

    response = {
        "data": data[start:end],
        "total": data_length,
        "count": page_size,
        "pagination": {}
    }

    if end >= data_length:
        response["pagination"]["next"] = None

        if page_num > 1:
            response["pagination"]["previous"] = f"/data?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None
    else:
        if page_num > 1:
            response["pagination"]["previous"] = f"/data?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None

        response["pagination"]["next"] = f"/data?page_num={page_num+1}&page_size={page_size}"
    return response    



def load_csv():
    with open('ohlc.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_to_insert = []
        for row in reader:
            # print(row['UNIX'], row['SYMBOL'], row['OPEN'], row['HIGH'], row['LOW'], row['CLOSE'])
            datetime_value = convert_unix_timestamp_milliseconds(row['UNIX'])
            data_to_insert.append(Record(UNIX=datetime_value,SYMBOL=row["SYMBOL"], OPEN=row['OPEN'], CLOSE=row['CLOSE'],HIGH=row['HIGH'],LOW=row['LOW']))

    return data_to_insert


# ocnvert datetime
def convert_unix_timestamp_milliseconds(timestamp_ms):
    timestamp_seconds = int(timestamp_ms) / 1000
    datetime_value = datetime.fromtimestamp(timestamp_seconds)

    return datetime_value


# Custom JSON serialization method
def record_to_dict(record):
    return {
        "UNIX": record.UNIX.strftime("%Y-%m-%d %H:%M:%S"),
        "SYMBOL": record.SYMBOL,
        "OPEN": str(record.OPEN),
        "HIGH": str(record.HIGH),
        "LOW": str(record.LOW),
        "CLOSE": str(record.CLOSE)
    }


