import unittest
from utils import process_csv_file, record_to_dict
import asyncio
import json
from datetime import datetime
from decimal import Decimal
from models import Record

class TestProcessCSVFile(unittest.TestCase):
    def test_process_csv_file(self):
        # Create a mock file with some CSV data
        mock_file = b"UNIX,SYMBOL,OPEN,HIGH,LOW,CLOSE\n1644719640,XRPUSDT,42113,42126,42113,42123\n1644719700,ADAETH,42123,42148,42121,42146\n"

        # Call the function with the mock file using asyncio.run
        data_to_insert = asyncio.run(process_csv_file(mock_file))

        records_dicts = [record_to_dict(record) for record in data_to_insert]
        # Assert that the data_to_insert list contains the correct records
        expected_data = [
            {"UNIX": '1970-01-20 00:51:59', "SYMBOL": "XRPUSDT", "OPEN": "42113", "HIGH": "42126", "LOW": "42113", "CLOSE": "42123"},
            {"UNIX": '1970-01-20 00:51:59', "SYMBOL": "ADAETH", "OPEN": "42123", "HIGH": "42148", "LOW": "42121", "CLOSE": "42146"}
        ]
        print("===record_dicst",records_dicts)
        print("===expected_data",expected_data)
        self.assertEqual(records_dicts, expected_data)



    # def test_pagination_json(self):
    #     with open('result_data.json') as f:
    #         data = json.load(f)

    #     paged_response=page_result(data, 1, 1)
        
    #     json_response = json.dumps(paged_response, indent=2)

    #     # Print the JSON-like formatted string
    #     print("======Print the JSON-like formatted string")
    #     print(json_response)
    #     # self.assertEqual(records_dicts, expected_data)


if __name__ == "__main__":
    unittest.main()
