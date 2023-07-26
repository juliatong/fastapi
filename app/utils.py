import csv
from models import Record
from datetime import datetime

def load_csv():
    with open('ohlc.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_to_insert = []
        for row in reader:
            print(row['UNIX'], row['SYMBOL'], row['OPEN'], row['HIGH'], row['LOW'], row['CLOSE'])
            datetime_value = convert_unix_timestamp_milliseconds(row['UNIX'])
            data_to_insert.append(Record(UNIX=datetime_value,SYMBOL=row["SYMBOL"], OPEN=row['OPEN'], CLOSE=row['CLOSE'],HIGH=row['HIGH'],LOW=row['LOW']))

    return data_to_insert


def convert_unix_timestamp_milliseconds(timestamp_ms):
    timestamp_seconds = int(timestamp_ms) / 1000
    datetime_value = datetime.fromtimestamp(timestamp_seconds)

    return datetime_value

load_csv()