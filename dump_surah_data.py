from pathlib import Path
from sys import argv

import mysql.connector

from file_io import\
	load_json_file,\
	write_csv


auth_path = Path(argv[1]).resolve()
data_path = Path(argv[2]).resolve()

authentication = load_json_file(auth_path)

db_conn = mysql.connector.connect(**authentication)
with db_conn.cursor() as cursor:
	cursor.execute("USE surahdb;")
	cursor.execute("SELECT * FROM v_chron_order;")
	surah_data = cursor.fetchall()

	column_titles = ("id", "chronology", "titlefr", "period", "nbverses")
	write_csv(data_path, column_titles, surah_data)
