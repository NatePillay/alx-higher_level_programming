-- create BD and Table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id)
	)
