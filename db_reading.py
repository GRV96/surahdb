COLUMN_TITLES = ("id", "chronology", "titlefr", "period", "nbverses")


def get_surah_data(db_conn, chron_order):
	with db_conn.cursor() as cursor:
		view = "v_chron_order" if chron_order else "v_trad_order"
		cursor.execute("USE surahdb;")
		cursor.execute(f"SELECT * FROM {view};")
		surah_data = cursor.fetchall()

	return surah_data
