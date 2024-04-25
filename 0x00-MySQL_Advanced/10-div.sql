-- File to create function that does safe division.
-- Change Delimiter
DELIMITER $$

-- DEFINE FUNCITON
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS float
BEGIN
	IF b = 0 THEN RETURN 0;
	END IF;
	RETURN a / b;
END$$

-- reset delimiter
DELIMITER ;
