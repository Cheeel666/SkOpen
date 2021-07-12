from database.client import DBconnection
from database.models.models import *
from database.exceptions import *


class DbInteraction:
    def __init__(self, host, port, user, db_name, password, rebuild_db=False):
        self.postgres_connection = DBconnection(host, port, user, db_name, password, rebuild_db)

        if rebuild_db:
            self.rebuild()

    def rebuild(self):
        MODELS = (Roads)
        #self.postgres_connection.get_connection().drop_tables(MODELS)
        self.postgres_connection.get_connection().create_tables(MODELS)
        # curs = self.postgres_connection.get_connection().cursor()
        # curs.execute(str(query))
        # user = curs.fetchone()
        # curs.close()
        return

    def connect(self):
        self.postgres_connection.get_connection()

    def disconnect(self):
        self.postgres_connection.close_connection()

    def add_user_info(self, username, email, password, role):
        query = Users.insert(name=username, password=password, email=email, id_role=role)
        return query.execute()

    def get_user_info(self, username):
        query = Users.select().where(Users.name==username)
        curs = self.postgres_connection.get_connection().cursor()
        curs.execute(str(query))
        user = curs.fetchone()
        curs.close()

        if user:
            return {'username':user[1], 'password':user[2], 'email':user[3]}
        else:
            raise UserNotFoundException('UserNotFound')

    def add_country(self, country):
        query = Country.insert(name_country=country)
        return query.execute()

    def add_city(self, city, id_country):
        query = City.insert(name_city=city, id_country=id_country)
        return query.execute()



if __name__ == "__main__":
    db = DbInteraction('127.0.0.1', '5432', 'postgres', 'agregator', '', 0)
    db.connect()
    print(db.rebuild())
    db.disconnect()
