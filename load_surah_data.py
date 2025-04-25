from pathlib import Path
from sys import argv

import mysql.connector

from file_io import\
	load_json_file,\
	read_whole_file


BACKSLASH = "\\"
SLASH = "/"


auth_path = Path(argv[1]).resolve()
data_path = Path(argv[2]).resolve()

authentication = load_json_file(auth_path)

db_conn = mysql.connector.connect(**authentication)

with db_conn.cursor() as cursor:
	script_content = read_whole_file(Path("init_db.sql").resolve())
	cursor.execute(script_content)

db_conn = mysql.connector.connect(**authentication)
data_path = str(data_path).replace(BACKSLASH, SLASH)
with db_conn.cursor() as cursor:
	cursor.execute("USE surahdb;")
	cursor.execute(
		f"LOAD DATA LOCAL INFILE \'{data_path}\'\n"
		"INTO TABLE surahs\n"
		"FIELDS TERMINATED BY ';'\n"
		"IGNORE 1 LINES\n"
		"(id, chronology, titlefr, period, nbverses);")
	db_conn.commit()
