-- Prepares a MySQL Test server for the project.
CREATE DATABASE IF NOT EXISTS pharmacy_test_db;
CREATE USER IF NOT EXISTS 'pharmacy_test'@'localhost' IDENTIFIED BY 'pharmacy_test_pwd';
GRANT ALL PRIVILEGES ON pharmacy_test_db . * TO 'pharmacy_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'pharmacy_test'@'localhost';