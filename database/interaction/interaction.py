from database.client import DBconnection
from database.models.models import *
from database.exceptions import *
from parser.parser import *
import psycopg2


class DbInteraction:
    def __init__(self, host, port, user, db_name, password, rebuild_db=False):
        self.postgres_connection = DBconnection(host, port, user, db_name, password, rebuild_db)

        if rebuild_db:
            self.rebuild()

    def rebuild(self):

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

    def update_rosa(self, data):
        query = Roads.delete().\
            where(Roads.id_courort == Courorts.select(Courorts.id_courort).where(Courorts.name_courort == "Rosa"))
        print(query)
        data = data[10:12]
        fields = (Roads.type_road, Roads.name_road, Roads.lenght, Roads.width, Roads.worktime, Roads.work_status)
        query1 = Roads.insert_many(data, fields=fields)
        print(query1)
        return query1.execute()

    def update_laura(self, data):
        pass

    def update_polyana(self, data):
        pass

if __name__ == "__main__":
    db = DbInteraction('127.0.0.1', '5432', 'postgres', 'agregator', '', 0)
    db.connect()
    manager = ServiceFactory()
    print(db.update_rosa(manager.getRosa()))
    # print(manager.getRosa()[10])
    db.disconnect()
