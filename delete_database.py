import mysql.connector

from src.arg_parser import\
	make_parser_auth
from src.db_reading import\
	DB_NAME_SURAHDB,\
	db_exists
from src.file_io import\
	load_json_file


args = make_parser_auth().parse_args()
auth_path = args.auth_path.resolve()

authentication = load_json_file(auth_path)
db_conn = mysql.connector.connect(**authentication)

with db_conn.cursor() as cursor:
	if db_exists(cursor, DB_NAME_SURAHDB):
		cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME_SURAHDB};")
	else:
		print("Database surahdb does not exist.")
