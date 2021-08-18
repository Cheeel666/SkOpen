-- ok
drop table if exists city;
drop table if exists country;
create table country (
	id_country SERIAL PRIMARY KEY,
	name_country varchar NOT NULL
);
--ok
drop table if exists city;
create table city (
	id_city SERIAL PRIMARY KEY,
	name_city varchar NOT NULL,
	id_country integer NOT NULL,
	FOREIGN KEY (id_country) REFERENCES country(id_country)
);

drop table if exists roads;
drop table if exists courorts;
create table courorts(
	id_courort SERIAL PRIMARY KEY,
	name_courort varchar NOT NULL,
	city varchar NOT NULL,
	visability integer
);

insert into courorts values(0, 'Rosa', 'Sochi', 1), (1, 'Laura', 'Sochi', 1), (2, 'Polyana', 'Sochi', 1);

create table roads(
	id_road serial PRIMARY KEY,
	id_courort integer NOT NULL,
	type_road varchar NOT NULL,
	name_road varchar NOT NULL,
	work_status integer NOT NULL,
	complexity varchar,
	lenght integer,
	width integer,
	worktime varchar,
	FOREIGN KEY (id_courort) REFERENCES courorts(id_courort)
);

--role model


--1 admin 1 1 1 1
--2 mod 0 0 1 1
--3 user 0 0 0 1

drop table if exists comment;
drop table if exists users;
create table users (
	id_user serial PRIMARY KEY,
	name varchar not null,
    email varchar not null,
	password varchar not null,
	user_role varchar not null,
	dt_registration date,
	FOREIGN KEY (id_role) REFERENCES roles(id_role)
);

create table comment (
	id_comment serial PRIMARY KEY,
	id_user integer not null,
	id_courort integer not null,
	content varchar not null,
	likes integer not null,
	visability integer not null,
	datetime timestamp,
	FOREIGN KEY (id_user) REFERENCES users(id_user)
);

drop table if exists audit;
create table audit (
	id_interaction SERIAL PRIMARY KEY,
	id_user integer NOT NULL,
	action varchar not null,
	dt_interaction timestamp
);


insert into users values (0, 'ilya', 'il_chel@mail.ru', '12345', 'admin');


--triggers

CREATE OR REPLACE FUNCTION users_insert_trigger_fnc()
  RETURNS trigger AS
$$
BEGIN
	INSERT INTO "audit" ("id_user", "action", "dt_interaction")
	VALUES(NEW."id_user",'user registred' ,current_date);
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER user_insert_trigger
  AFTER INSERT
  ON "users"
  FOR EACH ROW
  EXECUTE PROCEDURE users_insert_trigger_fnc();

CREATE OR REPLACE FUNCTION comments_insert_trigger_fnc()
  RETURNS trigger AS
$$
BEGIN
	INSERT INTO "audit" ("id_user", "action", "dt_interaction")
	VALUES(NEW."id_user",'new comment' ,current_date);
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER comment_insert_trigger
  AFTER INSERT
  ON "comment"
  FOR EACH ROW
  EXECUTE PROCEDURE comments_insert_trigger_fnc();

CREATE OR REPLACE FUNCTION users_delete_trigger_fnc()
  RETURNS trigger AS
$$
BEGIN
	INSERT INTO "audit" ("id_user", "action", "dt_interaction")
	VALUES(NEW."id_user",'user deleted' ,current_date);
RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER user_delete_trigger
  AFTER delete
  ON "users"
  FOR EACH ROW
  EXECUTE PROCEDURE users_delete_trigger_fnc();