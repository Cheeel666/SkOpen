from database.client import DBconnection
from database.models.models import *
from database.exceptions import *
from parser.parser import *
from api.utils import parse_roads
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
        rosa_lifts, rosa_trails = parse_roads(data, 0)
        # print("OK: ", len(data) == len(rosa_lifts) + len(rosa_trails))

        fields = (Roads.type_road, Roads.name_road, Roads.lenght, Roads.width, Roads.worktime, Roads.work_status, Roads.id_courort)
        query_lifts = Roads.insert_many(rosa_lifts, fields=fields)
        query_lifts.execute()

        fields = (Roads.type_road, Roads.name_road, Roads.complexity, Roads.lenght, Roads.width, Roads.work_status, Roads.id_courort)
        query_trails = Roads.insert_many(rosa_trails, fields=fields)
        query_trails.execute()

    def update_laura(self, data):
        laura_lifts, laura_trails = parse_roads(data, 1)
        fields = (Roads.type_road, Roads.name_road, Roads.worktime, Roads.work_status,
                  Roads.id_courort)
        query_lifts = Roads.insert_many(laura_lifts, fields=fields)
        query_lifts.execute()

        # fields = (Roads.type_road, Roads.name_road, Roads.complexity, Roads.lenght, Roads.width, Roads.work_status,
        #           Roads.id_courort)
        # query_trails = Roads.insert_many(laura_trails, fields=fields)
        # query_trails.execute()

    def update_polyana(self, data):
        polyana_lifts, polyana_trails = parse_roads(data, 2)

        fields = (Roads.type_road, Roads.name_road, Roads.work_status,
                  Roads.id_courort)
        query_lifts = Roads.insert_many(polyana_lifts, fields=fields)
        query_lifts.execute()

        fields = (Roads.type_road, Roads.name_road, Roads.work_status,
                  Roads.id_courort)
        query_trails = Roads.insert_many(polyana_trails, fields=fields)
        query_trails.execute()

    def update_roads(self):
        Roads._schema.truncate_table(restart_identity=True)

        manager = ServiceFactory()
        self.update_rosa(manager.getRosa())
        self.update_polyana(manager.getPolyana())
        self.update_laura(manager.getLaura())

if __name__ == "__main__":
    db = DbInteraction('127.0.0.1', '5555', 'ilchel', 'agregator', 'password', 0)
    db.connect()
    manager = ServiceFactory()
    # ALTER SEQUENCE roads_id_road_seq restart with 1;
    print(db.update_roads())
    # print(manager.getLaura())
    db.disconnect()
