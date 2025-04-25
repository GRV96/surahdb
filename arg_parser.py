from argparse import ArgumentParser
from pathlib import Path


def _make_basic_parser():
	parser = ArgumentParser()

	parser.add_argument("-a", "--auth-path", type=Path, default=None,
		help="Path to the authentication file.")

	parser.add_argument("-d", "--data-path", type=Path, default=None,
		help="Path to the surahs' data.")

	return parser


def make_dumping_parser():
	parser = _make_basic_parser()
	parser.add_argument("-c", "--chron-order", action="store_true",
		help="Write the surahs' data in chronological order.")

	return parser


def make_loading_parser():
	parser = _make_basic_parser()
	return parser
