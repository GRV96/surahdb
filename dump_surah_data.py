import mysql.connector

from src.arg_parser import\
	make_dumping_parser
from src.db_reading import\
	COLUMN_TITLES,\
	get_surah_data
from src.file_io import\
	load_json_file,\
	write_csv


args = make_dumping_parser().parse_args()
auth_path = args.auth_path.resolve()
data_path = args.data_path.resolve()
chron_order = args.chron_order

authentication = load_json_file(auth_path)

db_conn = mysql.connector.connect(**authentication)
surah_data = get_surah_data(db_conn, chron_order)
write_csv(data_path, COLUMN_TITLES, surah_data)
