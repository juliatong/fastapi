import unittest
from utils import process_csv_file, record_to_dict
import asyncio
from datetime import datetime
from decimal import Decimal
from models import Record

class TestProcessCSVFile(unittest.TestCase):
    def test_process_csv_file(self):
        # Create a mock file with some CSV data
        mock_file = b"UNIX,SYMBOL,OPEN,HIGH,LOW,CLOSE\n1644719640,BTCUSDT,42113,42126,42113,42123\n1644719700,BTCUSDT,42123,42148,42121,42146\n"

        # Call the function with the mock file using asyncio.run
        data_to_insert = asyncio.run(process_csv_file(mock_file))

        records_dicts = [record_to_dict(record) for record in data_to_insert]
        # Assert that the data_to_insert list contains the correct records
        expected_data = [
            {"UNIX": '1970-01-20 00:51:59', "SYMBOL": "BTCUSDT", "OPEN": "42113", "HIGH": "42126", "LOW": "42113", "CLOSE": "42123"},
            {"UNIX": '1970-01-20 00:51:59', "SYMBOL": "BTCUSDT", "OPEN": "42123", "HIGH": "42148", "LOW": "42121", "CLOSE": "42146"},
        ]
        self.assertEqual(records_dicts, expected_data)

if __name__ == "__main__":
    unittest.main()
