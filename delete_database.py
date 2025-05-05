import mysql.connector

from src.arg_parser import\
	make_auth_parser
from src.file_io import\
	load_json_file


args = make_auth_parser().parse_args()
auth_path = args.auth_path.resolve()

authentication = load_json_file(auth_path)
db_conn = mysql.connector.connect(**authentication)

with db_conn.cursor() as cursor:
	cursor.execute("DROP DATABASE IF EXISTS surahdb;")
