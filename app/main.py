from fastapi import FastAPI
import mysql.connector

app = FastAPI()

class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read(),
            host=host, # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()

    def query_titles(self):
        self.cursor.execute('SELECT * FROM ohlc price')
        rec = []
        for c in self.cursor:
            print(c)
            rec.append(c[0])
        return rec



@app.get("/")
def hello_world():
    return {"message": "OK"}


@app.get("/test")
def test_connection():
    return {"message": "OOOOO"}
    # global conn
    # if not conn:
    #     conn = DBManager(password_file='/run/secrets/db-password')
    # rec = conn.query_titles()

    # response = ''
    # for c in rec:
    #     response = response  + '<div>   Hello  ' + c + '</div>'
    # return response