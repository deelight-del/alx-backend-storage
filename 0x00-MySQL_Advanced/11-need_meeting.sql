-- Task 11, no need for tables.
-- Change Delimiters.
DELIMITER $$;

-- CREATE VIEW
CREATE VIEW need_meeting (name)
AS SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL)$$

-- Reset Delimiter
DELIMITER ;
