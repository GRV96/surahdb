"""
This script creates the database and loads the surahs' data from a CSV file.
The user must provide the path to this file as an argument.

MySQL connection argument allow_local_infile must be true for this script.
Otherwise, it will be unable to load data from a file and will raise an
exception.
"""


from pathlib import Path

import mysql.connector

from src.arg_parser import\
	make_parser_loading
from src.database.db_config_validation import\
	validate_db_config
from src.database.db_reading import\
	COLUMN_NAMES,\
	DB_NAME_SURAHDB,\
	USE_SURAHDB,\
	COMMA_SPACE,\
	db_exists
from src.file_io import\
	load_json_file,\
	read_whole_file


BACKSLASH = "\\"
SLASH = "/"


args = make_parser_loading(__doc__).parse_args()
db_config_path = args.db_config.resolve()
surah_file = args.surah_file.resolve()
surah_file = str(surah_file).replace(BACKSLASH, SLASH)

db_config = load_json_file(db_config_path)
validate_db_config(db_config)

db_conn = mysql.connector.connect(**db_config)
with db_conn.cursor() as cursor:
	surahdb_exists = db_exists(cursor, DB_NAME_SURAHDB)

	if surahdb_exists:
		print(f"Database {DB_NAME_SURAHDB} already exists.")
	else:
		script_content = read_whole_file(
			Path("src/database/init_db.sql").resolve())
		cursor.execute(script_content)

if not surahdb_exists:
	db_conn.reconnect()
	with db_conn.cursor() as cursor:
		cursor.execute(USE_SURAHDB)
		cursor.execute("SET GLOBAL local_infile=1;")
		cursor.execute(
			f"LOAD DATA LOCAL INFILE \'{surah_file}\'\n"
			"INTO TABLE surahs\n"
			"FIELDS TERMINATED BY ';'\n"
			"IGNORE 1 LINES\n"
			f"({COMMA_SPACE.join(COLUMN_NAMES)});")
		db_conn.commit()
