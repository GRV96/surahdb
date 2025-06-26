"""
This script writes the surahs' data in a CSV file.
"""


import mysql.connector

from src.arg_parser import\
	make_parser_dumping
from src.database.db_config_validation import\
	validate_db_config
from src.database.db_reading import\
	COLUMN_NAMES,\
	get_surah_data
from src.file_io import\
	load_json_file,\
	write_csv


args = make_parser_dumping(__doc__).parse_args()
db_config_path = args.db_config.resolve()
surah_file = args.surah_file.resolve()
chron_order = args.chron_order
quran_period = args.period

db_config = load_json_file(db_config_path)
validate_db_config(db_config)

with mysql.connector.connect(**db_config) as db_conn:
	surah_data = get_surah_data(db_conn,
		chron_order=chron_order, period=quran_period)
	write_csv(surah_file, COLUMN_NAMES, surah_data)
