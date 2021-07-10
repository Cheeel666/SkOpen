from database.client import DBconnection
from database.models.models import *
from database.exceptions import *


class DbInteraction:
    def __init__(self, host, port, user, db_name, password, rebuild_db=False):
        self.postgres_connection = DBconnection(host, port, user, db_name, password, rebuild_db)

        if rebuild_db:
            pass

    def connect(self):
        self.postgres_connection.get_connection()

    def disconnect(self):
        self.postgres_connection.close_connection()

    def add_user_info(self, username, email, password, role):
        query = Users.insert(name=username, password=password, email=email, id_role=role)
        return self.postgres_connection.execute_query(query)

    def get_user_info(self, username):
        query = Users.select().where(Users.name==username)
        user = self.postgres_connection.execute_query(query).fetchone()
        if user:
            return {'username':user[1], 'password':user[2], 'email':user[3]}
        else:
            raise UserNotFoundException('UserNotFound')

    def add_country(self, country):
        query = Country.insert(name_country=country)
        return self.postgres_connection.execute_query(query)

    def add_city(self, city, id_country):
        query = City.insert(name_city=city, id_country=id_country)
        return self.postgres_connection.execute_query(query)



if __name__ == "__main__":
    db = DbInteraction('localhost', '5432', 'postgres', 'agregator', '', 0)
    db.connect()
    print(db.get_user_info('semenchel'))
    db.disconnect()
