import mysql.connector

from src.arg_parser import\
	make_parser_dumping
from src.db_reading import\
	COLUMN_NAMES,\
	get_surah_data
from src.file_io import\
	load_json_file,\
	write_csv
from src.quran_periods import\
	PERIOD_UNDEF


args = make_parser_dumping().parse_args()
db_config_path = args.db_config.resolve()
surah_file = args.surah_file.resolve()
chron_order = args.chron_order

db_config = load_json_file(db_config_path)
db_conn = mysql.connector.connect(**db_config)

surah_data = get_surah_data(db_conn, chron_order, PERIOD_UNDEF)
write_csv(surah_file, COLUMN_NAMES, surah_data)
