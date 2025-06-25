# __all__ declared at the module's end

from typing import Any

from src.quran_period import QuranPeriod


COLUMN_ID: str = "id"
COLUMN_CHRON: str = "chronology"
COLUMN_TITLE_FR: str = "titlefr"
COLUMN_TITLE_EN: str = "titleen"
COLUMN_PERIOD: str = "period"
COLUMN_NB_VERSES: str = "nbverses"

COLUMN_NAMES: tuple[str, ...] = (
	COLUMN_ID,
	COLUMN_CHRON,
	COLUMN_TITLE_FR,
	COLUMN_TITLE_EN,
	COLUMN_PERIOD, 
	COLUMN_NB_VERSES
)

DB_NAME_SURAHDB: str = "surahdb"
USE_SURAHDB: str = f"USE {DB_NAME_SURAHDB};"

COMMA_SPACE: str = ", "

_ASTERISK: str = "*"
_SEMICOLON: str = ";"

_TABLE_NAME_SURAHS: str = "surahs"
_WHERE_PERIOD_MECCAN: str\
	= f"\nWHERE {COLUMN_PERIOD}={QuranPeriod.MECCAN}"
_WHERE_PERIOD_MEDINAN: str =\
	f"\nWHERE {COLUMN_PERIOD}={QuranPeriod.MEDINAN}"
_ORDER_BY_CHRON: str = f"\nORDER BY {COLUMN_CHRON}"
_ORDER_BY_ID: str = f"\nORDER BY {COLUMN_ID}"


def db_exists(cursor, db_name: str) -> bool:
	"""
	This function uses a MySQL cursor to determine whether the specified
	database exists.

	Args:
		cursor: a MySQL cursor.
		db_name: the name of the database whose existence is verified.

	Returns:
		bool: True if the database exists, False otherwise.
	"""
	cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
	db_matches = cursor.fetchall()
	return len(db_matches) == 1


def get_surah_data(
		db_conn, chron_order: bool,
		period: QuranPeriod | int,
		*column_names: str)\
		-> list[tuple | Any]:
	"""
	This function extracts data about the surahs from the database.

	It is possible to include only surahs from the Meccan (number 0) or Medinan
	(number 1) period. If any other value is passed, all surahs will be
	included.

	The variable length argument allows to specify which columns to select. If
	no columns are specified, all columns will be selected.

	The returned value is a list of tuples representing database rows. However,
	if only one column is selected, the list's items will be this column's
	values instead.

	Args:
		db_conn: the connection to a database.
		chron_order: If True, the surahs will be sorted in chronological order.
			If False, the surhas will be sorted in traditional order.
		period: the Meccan or Medinan period or no period.
		column_names: the columns to select.

	Returns:
		list: the rows extracted from the database.
	"""
	nb_columns = len(column_names)
	if nb_columns > 0:
		col_names = COMMA_SPACE.join(column_names)
	else:
		col_names = _ASTERISK

	query = f"SELECT {col_names}\nFROM {_TABLE_NAME_SURAHS}"

	if period == QuranPeriod.MECCAN:
		query += _WHERE_PERIOD_MECCAN
	elif period == QuranPeriod.MEDINAN:
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
	"COLUMN_TITLE_EN",
	"COLUMN_PERIOD",
	"COLUMN_NB_VERSES",
	"COLUMN_NAMES",
	"DB_NAME_SURAHDB",
	"USE_SURAHDB",
	"COMMA_SPACE",
	db_exists.__name__,
	get_surah_data.__name__
]
