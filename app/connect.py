from sqlalchemy import create_engine,URL,text, orm 
from sqlalchemy.exc import OperationalError



# DATABASE_URL ="mysql+pymysql://root:db-57xsl@db/example"
# engine = create_engine(DATABASE_URL, echo=True)

url_object = URL.create(
    "mysql+pymysql",
    username="root",
    password="db-57xsl",  # plain (unescaped) text
    host="db",
    database="example",
)
engine = create_engine(url_object)


# with engine.connect() as connection:
#     result = connection.execute(text('select "Hello"'))
#     print(result.all())

try:
    with engine.connect() as connection:
        result = connection.execute(text('select "Hello"'))
        print(result.all())
        print("MySQL connection successful!")

except OperationalError as e:
    print("Error connecting to MySQL:", e)


SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
    

    