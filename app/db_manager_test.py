
import unittest
from db_manager import DBManager

class TestDBManager(unittest.TestCase):
    def setUp(self):
        self.conn = DBManager(password_file='/run/secrets/db-password')

    def tearDown(self):
        self.conn.connection.close()

    def test_query_ohlc(self):
        rec = self.conn.query_ohlc()
        self.assertIsNotNone(rec)
        self.assertIsInstance(rec, dict)
        self.assertIn('UNIX', rec)
        self.assertIn('SYMBOL', rec)
        self.assertIn('OPEN', rec)
        self.assertIn('HIGH', rec)
        self.assertIn('LOW', rec)
        self.assertIn('CLOSE', rec)

if __name__ == '__main__':
    unittest.main()
