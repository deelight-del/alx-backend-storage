-- Moudle to create AddBonus Store Procedures.
-- Change Delimiter
DELIMITER $$

-- Define Stored Procedure
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	-- Check if the project_name is not in project table
	IF project_name NOT IN (`projects`.name) THEN
		INSERT INTO projects(name) VALUES (project_name);
	END IF;
	-- Insert into the corrections table respectively.
	INSERT INTO corrections
	VALUES(user_id, (SELECT id FROM projects WHERE name = project_name), score);
END$$
-- reset DELIMETER
DELIMITER ;
