-- File to create inde on part of name of column
-- Change Delimiter
DELIMITER $$

-- CREATE INDEX
CREATE INDEX idx_name_first ON names (name(1))$$

-- Reset Delimiter
DELIMITER ;
