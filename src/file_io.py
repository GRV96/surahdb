# __all__ declared at the module's end

import csv
import json

from pathlib import Path


_COLON: str = ";"
_EMPTY_STR: str = ""
_MODE_R: str = "r"
_MODE_W: str = "w"
_UTF8: str  = "utf-8"


def load_json_file(json_path: Path) -> dict | list:
	"""
	This function reads a JSON file and loads its content.

	Args:
		json_path: the path to a JSON file.

	Returns:
		the JSON file's loaded content.
	"""
	with json_path.open(_MODE_R, encoding=_UTF8) as json_file:
		return json.load(json_file)


def read_whole_file(file_path: Path) -> str:
	"""
	This function reads a text file and provides all its content as one string.

	Args:
		file_path: the path to the file to read.

	Returns:
		str: the file's whole content.
	"""
	with file_path.open(_MODE_R, encoding=_UTF8) as file:
		return file.read()


def write_csv(
		csv_path: Path,
		column_titles: list[str] | tuple[str, ...],
		data_by_lines) -> None:
	"""
	This function writes data in a CSV file whose path is given.

	The data must consist of a list or tuple whose items are lists or tuples
	representing a line of data in the CSV fiile.

	Args:
		csv_path: the path to the CSV file.
		column_titles: the titles of the CSV file's columns.
		data_by_lines: the data to write in the CSV file.
	"""
	with csv_path.open(_MODE_W, encoding=_UTF8, newline=_EMPTY_STR) as file:
		writer = csv.writer(file, delimiter=_COLON)
		writer.writerow(column_titles)

		for d in data_by_lines:
			writer.writerow(d)


__all__ = [
	load_json_file.__name__,
	read_whole_file.__name__,
	write_csv.__name__
]
