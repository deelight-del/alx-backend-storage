-- In this module, we create a stored procedure
-- That computes and stores average score of a user.
-- Change Delimiter
DELIMITER $$

-- CREATE PROCEDURE
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	-- Declare variable to store value
	DECLARE avg_score FLOAT;
	DECLARE new_user_id INT;

	SET new_user_id = user_id;

	-- Select the average from the corrections tabel into declared value
	SELECT AVG(score) INTO avg_score FROM corrections
	WHERE user_id = new_user_id
	GROUP BY user_id;

	-- Update the avergage score into the users table
	UPDATE users SET average_score = avg_score
	WHERE id = user_id;
END$$

-- Reset DELIMITER
DELIMITER ;
