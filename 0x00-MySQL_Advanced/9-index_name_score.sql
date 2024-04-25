-- File to create index based on first name and score.
-- Ensure Delimiter is ;
DELIMITER ;

-- CREATE INDEX
CREATE INDEX idx_name_first_score ON names (name(1), score);
