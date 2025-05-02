from argparse import ArgumentParser
from pathlib import Path


def _add_arg_auth_path(parser):
	parser.add_argument("-a", "--auth-path", type=Path, default=None,
		help="Path to the authentication file.")


def _add_arg_chron_order(parser):
	parser.add_argument("-c", "--chron-order", action="store_true",
		help="Write the surahs' data in chronological order.")


def _add_arg_data_path(parser):
	parser.add_argument("-d", "--data-path", type=Path, default=None,
		help="Path to the surahs' data.")


def make_dumping_parser():
	parser = ArgumentParser()
	_add_arg_auth_path(parser)
	_add_arg_data_path(parser)
	_add_arg_chron_order(parser)
	return parser


def make_graph_parser():
	parser = ArgumentParser()
	_add_arg_auth_path(parser)
	_add_arg_chron_order(parser)
	return parser


def make_loading_parser():
	parser = ArgumentParser()
	_add_arg_auth_path(parser)
	_add_arg_data_path(parser)
	return parser
