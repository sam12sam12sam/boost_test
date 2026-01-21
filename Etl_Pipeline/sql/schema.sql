
DROP SCHEMA IF EXISTS boost_test;
CREATE SCHEMA boost_test;
use boost_test;
-- RAW CSV TABLE
DROP TABLE IF EXISTS raw_test;
CREATE TABLE raw_test (
    id VARCHAR(20),
    name VARCHAR(255),
    address TEXT,
    color VARCHAR(50),
    created_at VARCHAR(100),
    last_login VARCHAR(50),
    is_claimed VARCHAR(20),
    paid_amount VARCHAR(50)
);

-- RAW JSON TABLE
DROP TABLE IF EXISTS raw_users;
CREATE TABLE raw_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    raw_payload JSON NOT NULL,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CLEAN CSV TABLE
DROP TABLE IF EXISTS test;
CREATE TABLE test (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    color VARCHAR(50),
    created_at TIMESTAMP NULL,
    last_login TIMESTAMP NULL,
    is_claimed BOOLEAN,
    paid_amount NUMERIC(12,2)
);

-- CLEAN USERS
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id CHAR(36) PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255),
    dob VARCHAR(255),
    address TEXT,
    created_at VARCHAR(255),
    updated_at VARCHAR(255)
);

-- TELEPHONE NUMBERS
DROP TABLE IF EXISTS telephone_numbers;
CREATE TABLE telephone_numbers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id CHAR(36),
    phone VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- JOBS HISTORY
DROP TABLE IF EXISTS jobs_history;
CREATE TABLE jobs_history (
    job_id CHAR(36) PRIMARY KEY,
    user_id CHAR(36),
    occupation VARCHAR(255),
    is_fulltime BOOLEAN,
    start VARCHAR(255),
    end VARCHAR(255),
    logged_at VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);



CREATE USER 'boost_user'@'%' IDENTIFIED BY 'boost_password';
GRANT ALL PRIVILEGES ON boost_test.* TO 'boost_user'@'%';
FLUSH PRIVILEGES;

SELECT user, host FROM mysql.user;
