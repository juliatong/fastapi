import pymysql.cursors

class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = pymysql.connect(
            user=user, 
            password="db-57xsl",
            host=host, # name of the mysql service as set in the docker compose file
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        pf.close()
        self.cursor = self.connection.cursor()

    def query_ohlc(self):
        with self.cursor as cursor:
            # Read a single record
            sql = "SELECT * FROM ohlc_price"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)


conn = None

def test_connection():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    rec = conn.query_ohlc()


test_connection()    