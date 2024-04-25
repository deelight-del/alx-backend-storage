-- Module to create trigger when an insert happens.
-- Change DELIMTER
DELIMITER $$

-- Write Trigger
CREATE TRIGGER reduce_items
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
END$$

-- reset delimeter
DELIMITER ;
