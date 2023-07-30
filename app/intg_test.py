import os
from fastapi.testclient import TestClient
import unittest
from utils import process_csv_file
from models import Record
from connect import SessionLocal
from main import app
import asyncio

import requests

from main import app

client = TestClient(app)


def test_post_data():
    url = 'http://localhost:8000/data'
    token = 'julia'  # Replace with your actual access token

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',  # Set the appropriate content type if needed
    }
    files = [('files', open('ohlc.csv', 'rb'))]
    resp = requests.post(url=url, files=files, headers=headers)
    print(resp.status_code) 
    print(resp.text)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

# can add more GET tests here as an alernative to GET on postman