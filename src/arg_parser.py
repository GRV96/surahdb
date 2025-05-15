# __all__ declared at the module's end

from argparse import\
	ArgumentParser,\
	RawDescriptionHelpFormatter
from pathlib import Path


def _add_arg_chron_order(parser):
	parser.add_argument("-c", "--chron-order", action="store_true",
		help="Sort the surahs in chronological order.")


def _add_arg_db_config(parser):
	parser.add_argument("-d", "--db-config", type=Path, required=True,
		help="A JSON file containing database configuration.")


def _add_arg_surah_file(parser):
	parser.add_argument("-s", "--surah-file", type=Path, required=True,
		help="A CSV file containing the surahs' data.")


def make_parser_db_config(description):
	parser = ArgumentParser(
		description=description, formatter_class=RawDescriptionHelpFormatter)
	_add_arg_db_config(parser)
	return parser


def make_parser_dumping(description):
	parser = ArgumentParser(
		description=description, formatter_class=RawDescriptionHelpFormatter)
	_add_arg_db_config(parser)
	_add_arg_surah_file(parser)
	_add_arg_chron_order(parser)
	return parser


def make_parser_loading(description):
	parser = ArgumentParser(
		description=description, formatter_class=RawDescriptionHelpFormatter)
	_add_arg_db_config(parser)
	_add_arg_surah_file(parser)
	return parser


def make_parser_plots(description):
	parser = ArgumentParser(
		description=description, formatter_class=RawDescriptionHelpFormatter)
	_add_arg_db_config(parser)
	_add_arg_chron_order(parser)
	return parser


__all__ = [
	make_parser_db_config.__name__,
	make_parser_dumping.__name__,
	make_parser_loading.__name__,
	make_parser_plots.__name__
]
