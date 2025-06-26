"""
This script calculates the cumulative sum of the surahs' length and writes it
in a CSV file.
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
	surah_data_size = len(surah_data)

cumul_length_sum = 0
for i in range(surah_data_size):
	data_line = surah_data[i]
	cumul_length_sum += data_line[-1]
	data_line = list(data_line)
	data_line.append(cumul_length_sum)
	surah_data[i] = data_line

for data_line in surah_data:
	cumulproportion = data_line[-1]/cumul_length_sum

	# The rounded proportion is stored as a string.
	data_line.append(f"{(cumulproportion*100):.4g}%")

col_names = list(COLUMN_NAMES)
col_names.extend(["cumulnbverses", "cumulproportion"])

write_csv(surah_file, col_names, surah_data)
