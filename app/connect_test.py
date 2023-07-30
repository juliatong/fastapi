import unittest
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from connect import engine

class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.engine = engine
        
    def test_database_connection(self):
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text('select "Hello"'))
                rows = result.all()
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][0], "Hello")
                print("MySQL connection successful!")
        except OperationalError as e:
            self.fail(f"Error connecting to MySQL: {e}")

if __name__ == '__main__':
    unittest.main()
