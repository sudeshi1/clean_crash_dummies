DROP TABLE IF EXISTS accidents;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS vehicle;

---------------------
---------------------
CREATE TABLE accidents (

    state VARCHAR NOT NULL, 
    case_number INTEGER NOT NULL,
    persons INTEGER NOT NULL,
    county VARCHAR NOT NULL ,
    city  VARCHAR NOT NULL, 
    month VARCHAR NOT NULL,
    day VARCHAR NOT NULL, 
    route VARCHAR NOT NULL, 
    rural_urban VARCHAR NOT NULL,
    lat FLOAT NOT NULL,
    lon FLOAT NOT NULL,
    first_harm VARCHAR NOT NULL,
    man_collision VARCHAR NOT NULL, 
    light_condit VARCHAR NOT NULL, 
    weather VARCHAR NOT NULL
    ); 


---------------------
---------------------

CREATE TABLE people (
    case_number INTEGER NOT NULL,
    vehicle_manufacturer VARCHAR NOT NULL,
    vehicle_model VARCHAR NOT NULL,
    age INTEGER NOT NULL,
    sex VARCHAR NOT NULL,
    doa_status VARCHAR NOT NULL,
    passenger_type VARCHAR NOT NULL,
    age_label VARCHAR NOT NULL
);


---------------------
---------------------
CREATE TABLE vehicle (
    case_number INTEGER NOT NULL,
    vehicle_num INTEGER NOT NULL,
    vehicle_body_type VARCHAR NOT NULL,
    speed_exceed VARCHAR NOT NULL,
    traff_violation VARCHAR NOT NULL,
    pedestrian VARCHAR NOT NULL,
    hit_run VARCHAR NOT NULL,
    PRIMARY KEY (case_number, vehicle_num)

);
