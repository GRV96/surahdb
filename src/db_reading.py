# __all__ declared at the module's end

COLUMN_ID = "id"
COLUMN_CHRON = "chronology"
COLUMN_TITLE_FR = "titlefr"
COLUMN_PERIOD = "period"
COLUMN_NB_VERSES = "nbverses"

COLUMN_NAMES = (
	COLUMN_ID,
	COLUMN_CHRON,
	COLUMN_TITLE_FR,
	COLUMN_PERIOD, 
	COLUMN_NB_VERSES
)

DB_NAME_SURAHDB = "surahdb"
USE_SURAHDB = f"USE {DB_NAME_SURAHDB};"

PERIOD_MECCAN = 0
PERIOD_MEDINAN = 1
PERIOD_UNDEF = -1

COMMA_SPACE = ", "

_ASTERISK = "*"
_SEMICOLON = ";"

_TABLE_NAME_SURAHS = "surahs"
_WHERE_PERIOD_MECCAN = f"\nWHERE {COLUMN_PERIOD}={PERIOD_MECCAN}"
_WHERE_PERIOD_MEDINAN = f"\nWHERE {COLUMN_PERIOD}={PERIOD_MEDINAN}"
_ORDER_BY_CHRON = f"\nORDER BY {COLUMN_CHRON}"
_ORDER_BY_ID = f"\nORDER BY {COLUMN_ID}"


def db_exists(cursor, db_name):
	cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
	db_matches = cursor.fetchall()
	return len(db_matches) == 1


def get_surah_data(db_conn, chron_order, period, *column_names):
	nb_columns = len(column_names)
	if nb_columns > 0:
		col_names = COMMA_SPACE.join(column_names)
	else:
		col_names = _ASTERISK

	query = f"SELECT {col_names}\nFROM {_TABLE_NAME_SURAHS}"

	if period == PERIOD_MECCAN:
		query += _WHERE_PERIOD_MECCAN
	elif period == PERIOD_MEDINAN:
		query += _WHERE_PERIOD_MEDINAN

	if chron_order:
		query += _ORDER_BY_CHRON
	else:
		query += _ORDER_BY_ID

	query += _SEMICOLON

	surah_data = None
	with db_conn.cursor() as cursor:
		cursor.execute(USE_SURAHDB)
		cursor.execute(query)
		surah_data = cursor.fetchall()

	if nb_columns == 1:
		surah_data = [item[0] for item in surah_data]

	return surah_data


__all__ = [
	"COLUMN_ID",
	"COLUMN_CHRON",
	"COLUMN_TITLE_FR",
	"COLUMN_PERIOD",
	"COLUMN_NB_VERSES",
	"COLUMN_NAMES",
	"DB_NAME_SURAHDB",
	"USE_SURAHDB",
	"PERIOD_MECCAN",
	"PERIOD_MEDINAN",
	"PERIOD_UNDEF",
	"COMMA_SPACE",
	get_surah_data.__name__
]
