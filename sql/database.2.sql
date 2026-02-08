CREATE DATABASE securecheck_v2;
USE securecheck_v2;
drop table traffic_stops;
CREATE TABLE traffic_stops (
    stop_id INT AUTO_INCREMENT PRIMARY KEY,
    stop_date DATE,
    stop_time TIME,
    country_name VARCHAR(100),
    driver_gender VARCHAR(10),
    driver_age_raw INT,
    driver_age INT,
    driver_race VARCHAR(50),
    violation_raw VARCHAR(100),
    violation VARCHAR(100),
    search_conducted BOOLEAN,
    search_type VARCHAR(100),
    stop_outcome VARCHAR(50),
    is_arrested BOOLEAN,
    stop_duration VARCHAR(20),
    drugs_related_stop BOOLEAN,
    vehicle_number VARCHAR(50)
);
SELECT COUNT(*) FROM traffic_stops;
SELECT COUNT(*) FROM traffic_stops WHERE search_conducted = 1;
CREATE INDEX idx_vehicle_number ON traffic_stops(vehicle_number);
CREATE INDEX idx_driver_gender ON traffic_stops(driver_gender);
CREATE INDEX idx_violation ON traffic_stops(violation);
CREATE INDEX idx_country_name ON traffic_stops(country_name);
CREATE INDEX idx_stop_date ON traffic_stops(stop_date);
CREATE INDEX idx_is_arrested ON traffic_stops(is_arrested);
CREATE INDEX idx_search_conducted ON traffic_stops(search_conducted)







