CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(255) NOT NULL,
    latitude DECIMAL(10,8) NOT NULL,
    longitude DECIMAL(11,8) NOT NULL,
    current_stop_sequence INT NOT NULL,
    direction_id INT NOT NULL,
    speed DECIMAL(5,2) DEFAULT NULL,  -- can be null
    revenue VARCHAR(20),              -- stores "REVENUE" or "NON_REVENUE"
    current_status VARCHAR(255),
    updated_at DATETIME               -- stores ISO-8601 datetime
);

