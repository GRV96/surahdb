# __all__ declared at the module's end

from argparse import ArgumentParser
from pathlib import Path


def _add_arg_auth_path(parser):
	parser.add_argument("-a", "--auth-path", type=Path, default=None,
		help="JSON file containing database authentication data.")


def _add_arg_chron_order(parser):
	parser.add_argument("-c", "--chron-order", action="store_true",
		help="Sort the surahs in chronological order.")


def _add_arg_data_path(parser):
	parser.add_argument("-d", "--data-path", type=Path, default=None,
		help="Path to the surahs' data.")


def make_parser_auth():
	parser = ArgumentParser()
	_add_arg_auth_path(parser)
	return parser


def make_parser_dumping():
	parser = ArgumentParser()
	_add_arg_auth_path(parser)
	_add_arg_data_path(parser)
	_add_arg_chron_order(parser)
	return parser


def make_parser_plots():
	parser = ArgumentParser()
	_add_arg_auth_path(parser)
	_add_arg_chron_order(parser)
	return parser


def make_parser_loading():
	parser = ArgumentParser()
	_add_arg_auth_path(parser)
	_add_arg_data_path(parser)
	return parser


__all__ = [
	make_parser_auth.__name__,
	make_parser_dumping.__name__,
	make_parser_loading.__name__,
	make_parser_plots.__name__
]
