from pathlib import Path

import mysql.connector

from src.arg_parser import\
	make_parser_loading
from src.db_reading import\
	USE_SURAHDB
from src.file_io import\
	load_json_file,\
	read_whole_file


BACKSLASH = "\\"
SLASH = "/"


args = make_parser_loading().parse_args()
auth_path = args.auth_path.resolve()
data_path = args.data_path.resolve()

authentication = load_json_file(auth_path)
db_conn = mysql.connector.connect(**authentication)

with db_conn.cursor() as cursor:
	script_content = read_whole_file(Path("src/init_db.sql").resolve())
	cursor.execute(script_content)

db_conn = mysql.connector.connect(**authentication)
data_path = str(data_path).replace(BACKSLASH, SLASH)
with db_conn.cursor() as cursor:
	cursor.execute(USE_SURAHDB)
	cursor.execute("SET GLOBAL local_infile=1;")
	cursor.execute(
		f"LOAD DATA LOCAL INFILE \'{data_path}\'\n"
		"INTO TABLE surahs\n"
		"FIELDS TERMINATED BY ';'\n"
		"IGNORE 1 LINES\n"
		"(id, chronology, titlefr, period, nbverses);")
	db_conn.commit()
