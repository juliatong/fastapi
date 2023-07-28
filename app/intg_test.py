import os
from fastapi.testclient import TestClient
import unittest
from utils import process_csv_file
from models import Record
from connect import SessionLocal
from main import app
import asyncio

import requests

url = 'http://localhost:8000/data'
# files = [('files', open('ohlc.csv', 'rb')), ('files', open('images/2.png', 'rb'))]
files = {'file': open('ohlc.csv', 'rb')}
resp = requests.post(url=url, files=files)
print(resp)
print(resp.text)
print(resp.json())

# class TestProcessCSVFileClient(unittest.TestCase):
#     async def test_upload_csv(self):
#         # Initialize the test client
#         client = TestClient(app)

#         # Prepare a CSV file content as bytes (replace this with your CSV content)
#         csv_content = b"UNIX,SYMBOL,OPEN,HIGH,LOW,CLOSE\n1644719460001,MSFT,42113,42126,42113,42123\n1644719700,LTCBTC,42123,42148,42121,42146"

#         # Send a request to the endpoint with the CSV file as form data
#         response = client.post("/data", files={"file": ("data.csv", csv_content)})

#         # Check if the response status code is 200 (OK)
#         assert response.status_code == 200

#         # Check if the message in the response is correct
#         assert response.json() == {"message": "CSV data uploaded and inserted into the database."}

#         # Verify that the data is correctly inserted into the database
#         db = SessionLocal()
#         try:
#             # Query all data from the database and check if it matches the original data
#             all_data = db.query(Record).all()
#             assert len(all_data) == 2  # Assuming there are two records in the CSV file

#             # Perform any additional checks on the data as needed
#             # For example, you can check if the data matches the expected values

#         finally:
#             # Close the session and remove the test database after the test
#             db.close()

# if __name__ == "__main__":
#     asyncio.run(TestProcessCSVFileClient().test_upload_csv())