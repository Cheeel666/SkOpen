from database.models.models import *
import psycopg2

class DBconnection:
    def __init__(self, host, port, user, db_name, password, rebuild_db=False):
        self.host = host
        self.port = port
        self.user = user
        self.db_name = db_name
        self.password = password
        self.rebuild_db = rebuild_db
        self.pg_conn = 0

    def get_connection(self):
        self.pg_conn = PostgresqlDatabase(
            database=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        return self.pg_conn

    def close_connection(self):
        self.pg_conn.close()


if __name__ == "__main__":
    dbcon = DBconnection(
        host="127.0.0.1", port=5432, user="postgres", db_name="agregator", password=""
    )
    print(dbcon.get_connection())
    dbcon.close_connection()

