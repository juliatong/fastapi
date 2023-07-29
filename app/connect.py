from sqlalchemy import create_engine,URL,text, orm 
from sqlalchemy.exc import OperationalError


url_object = URL.create(
    "mysql+pymysql",
    username="root",
    password="db-57xsl",  # plain (unescaped) text
    host="db",
    database="example",
)
engine = create_engine(url_object)

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
    

    