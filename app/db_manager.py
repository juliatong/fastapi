# db_manager.py
import pymysql.cursors

class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = pymysql.connect(
            user=user, 
            password="db-57xsl",
            host=host, # name of the MySQL service as set in the docker compose file
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        pf.close()
        self.cursor = self.connection.cursor()

    def query_ohlc(self):
        with self.cursor as cursor:
            # Read a single record
            sql = "SELECT * FROM ohlc_history"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
