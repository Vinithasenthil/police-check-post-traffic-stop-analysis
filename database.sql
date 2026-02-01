CREATE DATABASE securecheck_db;
SHOW DATABASES;
USE securecheck_db;
CREATE TABLE traffic_stops (
    stop_id INT AUTO_INCREMENT PRIMARY KEY,
    stop_date VARCHAR(20),
    stop_time VARCHAR(20),
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
SHOW tables;
DESCRIBE traffic_stops;
SELECT COUNT(*) FROM traffic_stops;
SELECT * FROM traffic_stops LIMIT 5;







