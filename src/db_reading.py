# __all__ declared at the module's end

COLUMN_TITLES = ("id", "chronology", "titlefr", "period", "nbverses")

DB_NAME_SURAHDB = "surahdb"
USE_SURAHDB = f"USE {DB_NAME_SURAHDB};"


def db_exists(cursor, db_name):
	cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
	db_matches = cursor.fetchall()
	return len(db_matches) == 1


def get_surah_chronology_trad_order(db_conn):
	chron_data = _get_view_data(db_conn, "v_surah_chronology_trad_order")
	return *(item[0] for item in chron_data),


def get_surah_data(db_conn, chron_order):
	view_name = "v_chron_order" if chron_order else "v_trad_order"
	surah_data = _get_view_data(db_conn, view_name)
	return surah_data


def get_surah_ids_chron_order(db_conn):
	id_data = _get_view_data(db_conn, "v_surah_ids_chron_order")
	return *(item[0] for item in id_data),


def get_surahs_length(db_conn, chron_order):
	view_name = "v_surah_length_chron_order" if chron_order\
		else "v_surah_length_trad_order"
	surah_length_data = _get_view_data(db_conn, view_name)
	return surah_length_data


def get_surahs_period_length(db_conn, chron_order):
	view_name = "v_surah_period_length_chron_order" if chron_order\
		else "v_surah_period_length_trad_order"
	surah_length_data = _get_view_data(db_conn, view_name)
	return surah_length_data


def _get_view_data(db_conn, view_name):
	surah_data = None

	with db_conn.cursor() as cursor:
		cursor.execute(USE_SURAHDB)
		cursor.execute(f"SELECT * FROM {view_name};")
		surah_data = cursor.fetchall()

	return surah_data


__all__ = [
	"COLUMN_TITLES",
	"DB_NAME_SURAHDB",
	"USE_SURAHDB",
	get_surah_chronology_trad_order.__name__,
	get_surah_data.__name__,
	get_surah_ids_chron_order.__name__,
	get_surahs_length.__name__,
	get_surahs_period_length.__name__
]
