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

-- Reset Delimter
DELIMITER ;

