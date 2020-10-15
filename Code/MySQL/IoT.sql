--  _____                _        ____________ 
-- /  __ \              | |       |  _  \ ___ \
-- | /  \/_ __ ___  __ _| |_ ___  | | | | |_/ /
-- | |   | '__/ _ \/ _` | __/ _ \ | | | | ___ \
-- | \__/\ | |  __/ (_| | ||  __/ | |/ /| |_/ /
--  \____/_|  \___|\__,_|\__\___| |___/ \____/ 


CREATE DATABASE IoT

USE IoT

CREATE TABLE rooms (
    id_room int primary key,
    name varchar(15),
    size enum ("Chico, mediano, Grande")
);

CREATE TABLE users (
    id_person int primary key,
    name varchar(15),
    birth date
);

CREATE TABLE passcodes(
    id_passcode int primary key,
    code varchar(15),
    expiration_date date
);

CREATE TABLE locks(
    id_lock int primary key,
    battery_level int  CHECK (battery_level > 0 AND battery_level <100),
    status enum("Open", "Closed")
);

CREATE TABLE thermostats(
    id_thermostat int primary key,
    int temperature,
    status enum("Working", "Sleep", "Error"),
    battery_level int  CHECK (battery_level > 0 AND battery_level <100)
);

CREATE TABLE cameras(
    id_camera int primary key,
    status enum("Movement", "Static"),
    battery_level int CHECK (battery_level > 0 AND battery_level <100)
);

CREATE TABLE lights(
    id_light int primary key,
    status enum("On", "Off"),
    intensity int CHECK (battery_level > 0 AND battery_level <255)
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
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),
    id_light int,
    FOREIGN KEY (id_light) REFERENCES light(id_light),
    UNIQUE (id_light)
);

CREATE TABLE temperature_control(
    time_sec TIMESTAMP,
    id_room int,
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),
    id_thermostat int,
    FOREIGN KEY (id_thermostat) REFERENCES thermostat(id_thermostat),
    UNIQUE (id_thermostat)
);

CREATE TABLE security_control(
    time_sec TIMESTAMP,
    id_room int, 
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),
    id_camera int,
    FOREIGN KEY (id_camara) REFERENCES cameras(id_camera),
);

CREATE TABLE alert(
    time_sec TIMESTAMP,
    status enum("Resolved", "Unresolved"),
    messagess varchar(200),
    origin varchar(100),
    id_room int,
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),
);
-- NO NECESARIA
CREATE TABLE access_control(
    entry_time TIMESTAMP,
    
    id_room int,
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),

    id_person int,
    FOREIGN KEY (id_person) REFERENCES users(id_person),
    
);

CREATE TABLE allowed_persons(
    id_room int,
    FOREIGN KEY (id_room) REFERENCES rooms(id_room),

    id_person int,
    FOREIGN KEY (id_person) REFERENCES users(id_person),

    id_passcode int,
    FOREIGN KEY (id_passcode) REFERENCES passcodes(id_passcode),
    
    id_lock int,
    FOREIGN KEY (id_lock) REFERENCES locks(id_lock),
    UNIQUE (id_lock),
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

SHOW INDEX this_table_column;
SHOW CREATE TABLE table_name;

--  _   _       _                 
-- | | | |     | |                
-- | | | | __ _| |_   _  ___  ___ 
-- | | | |/ _` | | | | |/ _ \/ __|
-- \ \_/ / (_| | | |_| |  __/\__ \
--  \___/ \__,_|_|\__,_|\___||___/

INSERT INTO users (id_person, name, birth) values (1, "Jorge", "2001-04-06");

INSERT INTO users (id_person, name, birth) values (2, "Josué", "2001-05-09");

INSERT INTO users (id_person, name, birth) values (3, "Luis", "2001-02-21");
