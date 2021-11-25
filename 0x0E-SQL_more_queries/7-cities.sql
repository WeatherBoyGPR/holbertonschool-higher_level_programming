-- will create database hbtn_0d_usa and table cities
-- cities
-- id INT UNIQUE, AUTO, NOT NULL, PRIMARY KEY
-- state_id INT, NOT NULL, FOREIGN KEY(id in states table)
-- name VARCHAR(256), NOT NULL
CREATE DATABASE
	IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE
	IF NOT EXISTS `hbtn_0d_usa`.`cities`(
		id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
		state_id INT NOT NULL,
		name VARCHAR(256) NOT NULL,
	FOREIGN KEY(`state_id`) REFERENCES `hbtn_0d_usa`.`states`(id));
