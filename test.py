import psycopg2
from psycopg2 import OperationalError
from peewee import *

from playhouse.postgres_ext import PostgresqlExtDatabase
db = PostgresqlDatabase("agregator")

class DbModel(Model):
    class Meta:
        database = db

class Citytest(DbModel):
    id_city = AutoField(column_name="id_city")
    name_city = TextField(column_name="name_city")
    id_country = IntegerField(column_name="id_country")

db_name = 'postgres'
user = 'postgres'
password = 'password'
host = 'localhost'
port = '5555'
pg_conn = PostgresqlDatabase(
            database=db_name,
            user=user,
            password=password,
            host=host,
            port=port,
        )

conn = psycopg2.connect("dbname=agregator user=ilchel password=password")
cur = conn.cursor()
query = "drop table test    ;"
cur.execute(query)
conn.commit()
cur.close()
conn.close()
print(query)