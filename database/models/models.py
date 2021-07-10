# Models package describes all of the tables in database and its relations
import psycopg2
from psycopg2 import OperationalError
from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase
from datetime import datetime

ext_db = PostgresqlExtDatabase("agregator")
db = PostgresqlDatabase("agregator")


class ExtDbModel(Model):
    class Meta:
        database = ext_db


class DbModel(Model):
    class Meta:
        database = db



class Country(DbModel):
    id_country = AutoField(column_name="id_country")
    name_country = TextField(column_name="name_country")

    class Meta:
        table_name = "country"


class City(DbModel):
    id_city = AutoField(column_name="id_city")
    name_city = TextField(column_name="name_city")
    id_country = IntegerField(column_name="id_country")

    class Meta:
        table_name = "city"


class Courorts(DbModel):
    id_courort = AutoField(column_name="id_courort")
    name_courort = TextField(column_name="name_courort")
    city = TextField(column_name="city")
    visability = IntegerField(column_name="visability")
    class Meta:
        table_name = "courorts"


class Roads(DbModel):
    id_road = AutoField(column_name="id_road")
    id_courort = IntegerField(column_name="id_courort")
    type_road = TextField(column_name="type_road")
    name_road = TextField(column_name="name_road")
    work_status = IntegerField(column_name="work_status")
    complexity = TextField(column_name="complexity")
    lenght = IntegerField(column_name="lenght")
    width = IntegerField(column_name="width")
    worktime = TextField(column_name="worktime")

    class Meta:
        table_name = "roads"


class Roles(DbModel):
    id_role = AutoField(column_name="id_role")
    title = TextField(column_name="title")
    permission_vis = IntegerField(column_name="permission_vis")
    permission_change = IntegerField(column_name="permission_change")
    permission_mod = IntegerField(column_name="permission_mod")
    permission_comment = IntegerField(column_name="permission_comment")

    class Meta:
        table_name = "roles"


class Users(DbModel):
    id_user = AutoField(column_name="id_user")
    name = TextField(unique=True)
    password = TextField(column_name="password")
    email=TextField(column_name="email")
    id_role = IntegerField(column_name="id_role")
    dt_registration = DateField(column_name="dt_registration", default=datetime.now())

    class Meta:
        table_name = "users"


class Comment(DbModel):
    id_comment = AutoField(column_name="id_comment")
    id_user = IntegerField(column_name="id_user")
    id_courort = IntegerField(column_name="id_courort")
    content = TextField(column_name="content")
    likes = IntegerField(column_name="likes")
    visability = IntegerField(column_name="visability")
    datetime = DateTimeField(column_name="datetime", default=datetime.now())

    class Meta:
        table_name = "comment"


class Action(DbModel):
    id_action = AutoField(column_name="id_action")
    description = TextField(column_name="description")

    class Meta:
        table_name = "action"


class Log(DbModel):
    id_interaction = AutoField(column_name="id_interaction")
    id_user = IntegerField(column_name="id_user")
    id_action = IntegerField(column_name="id_action")
    datetime = DateTimeField(column_name="datetime", default=datetime.now())