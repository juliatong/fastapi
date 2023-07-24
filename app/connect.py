from sqlalchemy import create_engine,URL,text

url_object = URL.create(
    "mysql+pymysql",
    username="root",
    password="db-57xsl",  # plain (unescaped) text
    host="db",
    database="example",
)
# engine = create_engine("mysql+pymysql://root:db-57xsl@db/example")

engine = create_engine(url_object)
with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))
    print(result.all())