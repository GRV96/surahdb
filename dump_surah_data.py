import mysql.connector

from arg_parser import\
	make_dumping_parser
from file_io import\
	load_json_file,\
	write_csv


args = make_dumping_parser().parse_args()
auth_path = args.auth_path.resolve()
data_path = args.data_path.resolve()
chron_order = args.chron_order

authentication = load_json_file(auth_path)

db_conn = mysql.connector.connect(**authentication)
with db_conn.cursor() as cursor:
	view = "v_chron_order" if chron_order else "v_trad_order"
	cursor.execute("USE surahdb;")
	cursor.execute(f"SELECT * FROM {view};")
	surah_data = cursor.fetchall()

	column_titles = ("id", "chronology", "titlefr", "period", "nbverses")
	write_csv(data_path, column_titles, surah_data)
