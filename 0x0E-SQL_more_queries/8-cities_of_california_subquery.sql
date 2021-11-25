-- Will list all cities of california in database hbtn_0d_usa
SELECT id, name
	FROM `hbtn_0d_usa`.`cities`
	WHERE state_id IN
		(SELECT id
		FROM `hbtn_0d_usa`.`states`
		WHERE name = 'California')
	ORDER BY `id`;
