create table families(
	id INTEGER primary key autoincrement,
	name TEXT,
  rank INTEGER,
	house TEXT
);

create table members(
	id INTEGER primary key autoincrement,
	name TEXT,
  gender TEXT,
	families_id, INTEGER,
	FOREIGN KEY(families_id) REFERENCES families(id)
);
