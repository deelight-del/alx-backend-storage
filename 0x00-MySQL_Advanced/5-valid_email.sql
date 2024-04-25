-- Task 5, where to check if valid_email is changed
-- Change Delimeter
DELIMITER $$

-- create trigger.
CREATE TRIGGER valid_email_tr
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
 IF OLD.email <> NEW.email THEN
	SET NEW.valid_email = 0;
 END IF;
END$$

-- reset trigger
DELIMITER ;
