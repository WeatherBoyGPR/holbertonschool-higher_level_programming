-- creates database `hbtn_0d_usa` and table `states`
-- `states`
-- id INT UNIQUE AUTO PRIMARY KEY, name VARCHAR(256) NOT NULL
CREATE DATABASE
	IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE
	IF NOT EXISTS `hbtn_0d_usa`.`states`(
	PRIMARY KEY(`id`),
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
