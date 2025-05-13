import mysql.connector

from src.arg_parser import\
	make_parser_db_config
from src.database.db_config_validation import\
	validate_db_config
from src.database.db_reading import\
	DB_NAME_SURAHDB,\
	db_exists
from src.file_io import\
	load_json_file


args = make_parser_db_config().parse_args()
db_config_path = args.db_config.resolve()

db_config = load_json_file(db_config_path)
validate_db_config(db_config)
db_conn = mysql.connector.connect(**db_config)

with db_conn.cursor() as cursor:
	if db_exists(cursor, DB_NAME_SURAHDB):
		cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME_SURAHDB};")
	else:
		print(f"Database {DB_NAME_SURAHDB} does not exist.")
