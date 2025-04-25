import csv
import json
from pathlib import Path
from sys import argv

import mysql.connector


auth_path = Path(argv[1]).resolve()
data_path = Path(argv[2]).resolve()

with auth_path.open("r", encoding="utf-8") as auth_file:
	authentication = json.load(auth_file)

db_conn = mysql.connector.connect(**authentication)
with db_conn.cursor() as cursor:
	cursor.execute("USE surahdb;")
	cursor.execute("SELECT * FROM v_chron_order;")
	surah_data = cursor.fetchall()

	with data_path.open("w", encoding="utf-8", newline="") as data_file:
		writer = csv.writer(data_file, delimiter=";")
		writer.writerow(("id", "chronology", "titlefr", "period", "nbverses"))

		for sd in surah_data:
			writer.writerow(sd)
