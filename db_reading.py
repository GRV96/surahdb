COLUMN_TITLES = ("id", "chronology", "titlefr", "period", "nbverses")

_USE_SURAH_DB = "USE surahdb;"


def get_surah_data(db_conn, chron_order):
	view_name = "v_chron_order" if chron_order else "v_trad_order"
	surah_data = _get_view_data(db_conn, view_name)
	return surah_data


def get_surahs_length(db_conn, chron_order):
	view_name = "v_surah_length_chron_order" if chron_order\
		else "v_surah_length_trad_order"
	surah_length_data = _get_view_data(db_conn, view_name)
	return surah_length_data


def _get_view_data(db_conn, view_name):
	surah_data = None

	with db_conn.cursor() as cursor:
		cursor.execute(_USE_SURAH_DB)
		cursor.execute(f"SELECT * FROM {view_name};")
		surah_data = cursor.fetchall()

	return surah_data
