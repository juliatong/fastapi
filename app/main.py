from fastapi import FastAPI
import pymysql.cursors

app = FastAPI()

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

    def query_titles(self):
        with self.cursor as cursor:
            # Read a single record
            sql = "SELECT * FROM ohlc_price"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)

conn = None

@app.get("/")
def hello_world():
    return {"message": "OK"}


@app.get("/test")
def test_connection():
    # return {"message": "OOOOO"}
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    rec = conn.query_titles()

    response = ''
    for c in rec:
        response = response  + '<div>   Hello  ' + c + '</div>'
    return response 