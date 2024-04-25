-- Module to create trigger when an insert happens.
-- Change DELIMTER
DELIMITER $$

-- Write Trigger
CREATE TRIGGER reduce_items
BEFORE INSERT ON items
FOR EACH ROW
BEGIN
SET NEW.quantity = NEW.quantity - 1;
END$$

-- reset delimeter
DELIMITER ;
