import json
from pathlib import Path
from sys import argv

import mysql.connector


BACKSLASH = "\\"
SLASH = "/"


auth_path = Path(argv[1]).resolve()
data_path = Path(argv[2]).resolve()

with auth_path.open("r", encoding="utf-8") as auth_file:
	authentication = json.load(auth_file)

db_conn = mysql.connector.connect(**authentication)

init_db_path = Path("init_db.sql").resolve()
with db_conn.cursor() as cursor:
	with init_db_path.open("r", encoding="utf-8") as init_db_file:
		cursor.execute(init_db_file.read())

db_conn = mysql.connector.connect(**authentication)
with db_conn.cursor() as cursor:
	cursor.execute("USE surahdb;")
	cursor.execute(
		f"LOAD DATA LOCAL INFILE \'{str(data_path).replace(BACKSLASH, SLASH)}\'\n"
		"INTO TABLE surahs\n"
		"FIELDS TERMINATED BY ';'\n"
		"IGNORE 1 LINES\n"
		"(id, chronology, titlefr, period, nbverses);")
	db_conn.commit()
