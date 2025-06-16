# __all__ declared at the module's end

from argparse import\
	ArgumentParser,\
	RawDescriptionHelpFormatter
from pathlib import Path

from .quran_period import QuranPeriod
from .surah_graphs import Language


def _add_arg_chron_order(parser: ArgumentParser) -> None:
	parser.add_argument("-c", "--chron-order", action="store_true",
		help="Sort the surahs in chronological order.")


def _add_arg_db_config(parser: ArgumentParser) -> None:
	parser.add_argument("-d", "--db-config", type=Path, required=True,
		help="A JSON file containing database connection configuration.")


def _add_arg_language(parser: ArgumentParser) -> None:
	parser.add_argument("-l", "--language", type=Language,
		default=Language.FRENCH,
		help=f"Possible values: {', '.join(l.value for l in Language)}.")


def _add_arg_quran_period(parser: ArgumentParser) -> None:
	value_mec = QuranPeriod.MECCAN
	value_med = QuranPeriod.MEDINAN

	parser.add_argument("-p", "--period", type=QuranPeriod,
		default=QuranPeriod.UNDEF,
		help=f"The Meccan ({value_mec}) or Medinan ({value_med}) period.")


def _add_arg_surah_file(parser: ArgumentParser) -> None:
	parser.add_argument("-s", "--surah-file", type=Path, required=True,
		help="A CSV file containing the surahs' data.")


def make_parser_db_config(description: str) -> ArgumentParser:
	"""
	This function creates an argument parser that requires the path to a JSON
	file that configures the connection to a MySQL server.

	Args:
		description: the description of the script that will use this parser.

	Returns:
		ArgumentParser: an argument parser.
	"""
	parser = ArgumentParser(
		description=description, formatter_class=RawDescriptionHelpFormatter)
	_add_arg_db_config(parser)
	return parser


def make_parser_dumping(description: str) -> ArgumentParser:
	"""
	This function creates an argument parser for the scripts that dump database
	content in a CSV file.

	Args:
		description: the description of the script that will use this parser.

	Returns:
		ArgumentParser: an argument parser.
	"""
	parser = ArgumentParser(
		description=description, formatter_class=RawDescriptionHelpFormatter)
	_add_arg_db_config(parser)
	_add_arg_surah_file(parser)
	_add_arg_chron_order(parser)
	_add_arg_quran_period(parser)
	return parser


def make_parser_loading(description: str) -> ArgumentParser:
	"""
	This function creates an argument parser for the script that creates the
	database and loads data into it.

	Args:
		description: the description of the script that will use this parser.

	Returns:
		ArgumentParser: an argument parser.
	"""
	parser = ArgumentParser(
		description=description, formatter_class=RawDescriptionHelpFormatter)
	_add_arg_db_config(parser)
	_add_arg_surah_file(parser)
	return parser


def make_parser_plots(description: str) -> ArgumentParser:
	"""
	This function creates an argument parser for the scripts that plot data.

	Args:
		description: the description of the script that will use this parser.

	Returns:
		ArgumentParser: an argument parser.
	"""
	parser = ArgumentParser(
		description=description, formatter_class=RawDescriptionHelpFormatter)
	_add_arg_db_config(parser)
	_add_arg_chron_order(parser)
	_add_arg_language(parser)
	return parser


__all__ = [
	make_parser_db_config.__name__,
	make_parser_dumping.__name__,
	make_parser_loading.__name__,
	make_parser_plots.__name__
]
