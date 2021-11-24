-- Will create table unique_id
-- id INT = 1 UNIQUE, VARCHAR(256)
CREATE TABLE
	IF NOT EXISTS `unique_id`(
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256));
