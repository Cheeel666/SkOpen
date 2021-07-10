drop database agregator;
create database agregator;
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
drop table if exists roles;
create table roles (
	id_role integer PRIMARY KEY,
	title varchar not null,
	permission_vis integer not null,
	permission_change integer not null,
	permission_mod integer not null,
	permission_comment integer not null
);
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
	id_role integer not null,
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
drop table if exists action;
create table action (
	id_action SERIAL PRIMARY KEY,
	description varchar not null
);

drop table if exists log;
create table log (
	id_interaction SERIAL PRIMARY KEY,
	id_user integer NOT NULL,
	id_action integer NOT NULL,
	dt_interaction timestamp
);

