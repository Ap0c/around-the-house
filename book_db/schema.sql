CREATE VIRTUAL TABLE IF NOT EXISTS books USING fts4 (title, author, location);
