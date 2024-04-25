-- FILE TO CREATE STORED PROCEDURES FOR WEIGHTED AVERAGE
-- change delimeter
DELIMITER $$

-- CREATE PROCEDURE FOR CALCULATING WEIGHTED AVERAGE
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	-- DECLARE VARIABLES
	DECLARE num FLOAT;
	DECLARE deno FLOAT;

	-- CREATE JOIN AND INSERT VALUES INTO NUMERATOR
	-- AND DENOMINATOR
	SELECT SUM(projects.weight * corrections.score),
	SUM(projects.weight) INTO num, deno
	FROM corrections INNER JOIN projects
	ON corrections.project_id = projects.id
	WHERE corrections.user_id = user_id;

	-- INSERT RESULT OF NUM / DENO INTO REQUIRED POSITON
	UPDATE users SET average_score = num / deno WHERE id = user_id;
END$$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
	-- Declare integers for holding cursor and markingcontinue handler
	DECLARE a,b INT;

	-- Declare Cursor from select statement
	DECLARE cur_1 CURSOR FOR
	SELECT id FROM users;

	-- Declare Continue handler when cursor reaches end.
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET b = 1;

	--Open Cursor
	OPEN cur_1;

	-- Start looping through cursor
	REPEAT
	FETCH cur_1 INTO a;   /* Fetch each loop id into a */
	CALL ComputeAverageWeightedScoreForUser(a); /* Call Procedure above for each id.*/
	UNTIL b = 1
	END REPEAT;
	CLOSE cur_1;
END$$

-- Reset Delimter
DELIMITER ;

