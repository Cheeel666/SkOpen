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

    def add_user_info(self, username, email, password, role=1):
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

    def delete_user_by_email(self, email):
        query = Users.delete().where(Users.email==email)
        query.execute()

    def add_comment(self, email, text, id_courort):
        cur = self.postgres_connection.get_connection().cursor()

        query = "select id_user from users where email = '" + str(email) + "';"
        # print(query)
        cur.execute(query)
        id_user = cur.fetchone()[0]
        self.postgres_connection.close_connection()
        cur = self.postgres_connection.get_connection().cursor()
        query = "insert into comment (id_user, id_courort, content, likes, visability) values (" + str(id_user)+\
                ", " + str(id_courort) + ", '" + str(text) + "',0,0)"
        # print(query)
        cur.execute(query)
        self.postgres_connection.pg_conn.commit()
        self.postgres_connection.close_connection()

    def update_laura(self, data):
        laura_lifts, laura_trails = parse_roads(data, 1)
        fields = (Roads.type_road, Roads.name_road, Roads.worktime, Roads.work_status,
                  Roads.id_courort)
        query_lifts = Roads.insert_many(laura_lifts, fields=fields)
        query_lifts.execute()

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
        manager = ServiceFactory()
        rosa_data = manager.getRosa()
        laura_data = manager.getLaura()
        polyana_data = manager.getPolyana()

        Roads._schema.truncate_table(restart_identity=True)

        self.update_rosa(rosa_data)
        self.update_laura(laura_data)
        self.update_polyana(polyana_data)

    def get_all_users(self):
        query = """
        select array_to_json(array_agg(lap))
        from (select t1.name, t1.email, t2.title AS "role" 
        from users t1 join roles t2 on t1.id_role = t2.id_role) lap;
        """
        cur = self.postgres_connection.get_connection().cursor()
        cur.execute(query)
        res = cur.fetchall()
        self.postgres_connection.close_connection()
        return res

    def get_user(self, mail, password):
        query = "select name, id_user, email, password, id_role from users where email = '" + str(mail) + "' and password = '" + str(password)+"'limit 1;"
        cur = self.postgres_connection.get_connection().cursor()
        cur.execute(query)
        res = cur.fetchone()
        self.postgres_connection.close_connection()
        return res

    def check_user(self, mail):
        query = "select email from users where email = '" + str(mail) + "' limit 1;"
        cur = self.postgres_connection.get_connection().cursor()
        cur.execute(query)
        res = cur.fetchone()
        self.postgres_connection.close_connection()
        return res

    def get_courorts(self):
        query = """
        select array_to_json(array_agg(lap))
        from (select name_courort, city from courorts) lap;
        """
        cur = self.postgres_connection.get_connection().cursor()
        cur.execute(query)
        res = cur.fetchone()
        self.postgres_connection.close_connection()
        return res

    def get_rosa(self):
        query = """
        select array_to_json(array_agg(lap))
        from (select type_road, name_road, work_status from roads where id_courort = 0) lap;
        """
        cur = self.postgres_connection.get_connection().cursor()
        cur.execute(query)
        res = cur.fetchone()
        self.postgres_connection.close_connection()
        return res

    def get_gorod(self):
        query = """
                select array_to_json(array_agg(lap))
                from (select type_road, name_road, work_status from roads where id_courort = 2) lap;
                """
        cur = self.postgres_connection.get_connection().cursor()
        cur.execute(query)
        res = cur.fetchone()
        self.postgres_connection.close_connection()
        return res

    def get_laura(self):
        query = """
                select array_to_json(array_agg(lap))
                from (select type_road, name_road, work_status from roads where id_courort = 1) lap;
                """
        cur = self.postgres_connection.get_connection().cursor()
        cur.execute(query)
        res = cur.fetchone()
        self.postgres_connection.close_connection()
        return res


if __name__ == "__main__":
    db = DbInteraction('127.0.0.1', '5555', 'ilchel', 'agregator', 'password', 0)
    db.connect()
    manager = ServiceFactory()

    print(db.update_roads())

    db.disconnect()
