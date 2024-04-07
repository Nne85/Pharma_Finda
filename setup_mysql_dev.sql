-- Prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS pharmacy_dev_db;
CREATE USER IF NOT EXISTS 'pharmacy_dev'@'localhost' IDENTIFIED BY 'pharmacy_dev_pwd';
GRANT ALL PRIVILEGES ON pharmacy_dev_db . * TO 'pharmacy_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'pharmacy_dev'@'localhost';
