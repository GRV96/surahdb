"""
This script calculates the cumulative sum of the surahs' length and writes it
in a CSV file.
"""

import mysql.connector

from src import QuranPeriod
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

db_config = load_json_file(db_config_path)
validate_db_config(db_config)
db_conn = mysql.connector.connect(**db_config)

surah_data = get_surah_data(db_conn, chron_order, QuranPeriod.UNDEF)
surah_data_size = len(surah_data)

cumul_length_sum = 0
for i in range(surah_data_size):
	data_line = surah_data[i]
	cumul_length_sum += data_line[-1]
	data_line = list(data_line)
	data_line.append(cumul_length_sum)
	surah_data[i] = data_line

for data_line in surah_data:
	data_line.append(data_line[-1]/cumul_length_sum)

col_names = list(COLUMN_NAMES)
col_names.extend(["cumulnbverses", "proportion"])
print(col_names)

write_csv(surah_file, col_names, surah_data)
