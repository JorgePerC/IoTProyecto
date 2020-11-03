--  _____                _        ____________ 
-- /  __ \              | |       |  _  \ ___ \
-- | /  \/_ __ ___  __ _| |_ ___  | | | | |_/ /
-- | |   | '__/ _ \/ _` | __/ _ \ | | | | ___ \
-- | \__/\ | |  __/ (_| | ||  __/ | |/ /| |_/ /
--  \____/_|  \___|\__,_|\__\___| |___/ \____/ 

-- Para que no nos pida borrarla al correr si ya existe
DROP DATABASE IF EXISTS ExampleDB;
CREATE DATABASE ExampleDB;

USE ExampleDB;

-- Ahora todas las bases básicas tienen autoincrement
-- Esto puede causar cosas raras si estás en modo save = False
-- Así que, ten cuidado, xd

CREATE TABLE rooms (
    id_room int primary key NOT NULL AUTO_INCREMENT,
    name varchar(15),
    size enum ("Chico, mediano, Grande")
);

CREATE TABLE users (
    id_person int primary key NOT NULL AUTO_INCREMENT,
    name varchar(15),
    birth date
);

CREATE TABLE passcodes(
    id_passcode int primary key NOT NULL AUTO_INCREMENT,
    code varchar(15),
    expiration_date date
);

CREATE TABLE locks(
    id_lock int primary key NOT NULL AUTO_INCREMENT,
    status enum("Open", "Closed"),
    battery_level int,
    CHECK (battery_level > 0 AND battery_level <100)
);

CREATE TABLE thermostats(
    id_thermostat int primary key NOT NULL AUTO_INCREMENT,
    temperature int,
    status enum("Working", "Sleep", "Error"),
    battery_level int,
    CHECK (battery_level > 0 AND battery_level < 100)
);   

CREATE TABLE cameras(
    id_camera int primary key NOT NULL AUTO_INCREMENT,
    status enum("Movement", "Static"),
    battery_level int,
    CHECK (battery_level > 0 AND battery_level <100)
);

CREATE TABLE lights(
    id_light int primary key NOT NULL AUTO_INCREMENT,
    status enum("On", "Off"),
    intensity int,
    CHECK (intensity > 0 AND intensity <= 255)
);

-- ______     _       _   _                 
-- | ___ \   | |     | | (_)                
-- | |_/ /___| | __ _| |_ _  ___  _ __  ___ 
-- |    // _ \ |/ _` | __| |/ _ \| '_ \/ __|
-- | |\ \  __/ | (_| | |_| | (_) | | | \__ \
-- \_| \_\___|_|\__,_|\__|_|\___/|_| |_|___/

-- Crear una entidad:
CREATE TABLE light_control(
    time_sec int,
    id_room int,
    id_light int,
    UNIQUE (id_light),
    FOREIGN KEY (id_light) REFERENCES lights(id_light),
    FOREIGN KEY (id_room) REFERENCES rooms(id_room)
);

CREATE TABLE temperature_control(
    time_sec TIMESTAMP,
    id_room int,
    id_thermostat int,
    UNIQUE (id_thermostat),
    FOREIGN KEY (id_thermostat) REFERENCES thermostats(id_thermostat),
    FOREIGN KEY (id_room) REFERENCES rooms(id_room)
);

CREATE TABLE security_control(
    time_sec TIMESTAMP,
    id_room int, 
    id_camera int,
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),
    FOREIGN KEY (id_camera) REFERENCES cameras(id_camera)
);

CREATE TABLE alert(
    time_sec TIMESTAMP,
    messagess varchar(200),
    origin varchar(100),
    id_room int,
    status enum("Resolved", "Unresolved"),
    FOREIGN KEY (id_room) REFERENCES rooms(id_room)
);
-- NO NECESARIA
CREATE TABLE access_control(
    entry_time TIMESTAMP,
    id_room int,
    id_person int,
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),
    FOREIGN KEY (id_person) REFERENCES users(id_person)  
);

CREATE TABLE allowed_persons(
    id_room int,
    id_person int,
    id_passcode int,
    id_lock int,
    UNIQUE (id_lock),
    FOREIGN KEY (id_passcode) REFERENCES passcodes(id_passcode),
    FOREIGN KEY (id_person) REFERENCES users(id_person),
    FOREIGN KEY (id_lock) REFERENCES locks(id_lock),
    FOREIGN KEY (id_room) REFERENCES rooms(id_room)
);


-- Relacionar: Constrains
/*
Un constrain es un condición que se está revisando constantemente 
para los datos de la base de datos

CHECK
Can be used with alter, or created from begigging
FOREING KEY (this_table_column) REFERENCES table(column)

El describe no dice si una relación es foránea
ALTER TABLE light_control MODIFY id_light int unique;
*/

-- SHOW INDEX this_table_column;
-- SHOW CREATE TABLE table_name;

--  _   _       _                 
-- | | | |     | |                
-- | | | | __ _| |_   _  ___  ___ 
-- | | | |/ _` | | | | |/ _ \/ __|
-- \ \_/ / (_| | | |_| |  __/\__ \
--  \___/ \__,_|_|\__,_|\___||___/

INSERT INTO users (id_person, name, birth) values (1, "Jorge", "2001-04-06");

INSERT INTO users (id_person, name, birth) values (2, "Josué", "2001-05-09");

INSERT INTO users (id_person, name, birth) values (3, "Luis", "2001-02-21");
