# __all__ declared at the module's end

from argparse import ArgumentParser
from pathlib import Path


def _add_arg_chron_order(parser):
	parser.add_argument("-c", "--chron-order", action="store_true",
		help="Sort the surahs in chronological order.")


def _add_arg_db_config(parser):
	parser.add_argument("--db-config", type=Path, default=None,
		help="A JSON file containing database configuration.")


def _add_arg_data_path(parser):
	parser.add_argument("-d", "--data-path", type=Path, default=None,
		help="A CSV file containing the surahs' data.")


def make_parser_db_config():
	parser = ArgumentParser()
	_add_arg_db_config(parser)
	return parser


def make_parser_dumping():
	parser = ArgumentParser()
	_add_arg_db_config(parser)
	_add_arg_data_path(parser)
	_add_arg_chron_order(parser)
	return parser


def make_parser_loading():
	parser = ArgumentParser()
	_add_arg_db_config(parser)
	_add_arg_data_path(parser)
	return parser


def make_parser_plots():
	parser = ArgumentParser()
	_add_arg_db_config(parser)
	_add_arg_chron_order(parser)
	return parser


__all__ = [
	make_parser_db_config.__name__,
	make_parser_dumping.__name__,
	make_parser_loading.__name__,
	make_parser_plots.__name__
]
