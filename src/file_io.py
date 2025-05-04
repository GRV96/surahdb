# __all__ declared at the module's end

import csv
import json


_COLON = ";"
_EMPTY_STR = ""
_MODE_R = "r"
_MODE_W = "w"
_UTF8  = "utf-8"


def load_json_file(json_path):
	with json_path.open(_MODE_R, encoding=_UTF8) as json_file:
		return json.load(json_file)


def read_whole_file(file_path):
	with file_path.open(_MODE_R, encoding=_UTF8) as file:
		return file.read()


def write_csv(csv_path, column_titles, data_by_line):
	with csv_path.open(_MODE_W, encoding=_UTF8, newline=_EMPTY_STR) as file:
		writer = csv.writer(file, delimiter=_COLON)
		writer.writerow(column_titles)

		for d in data_by_line:
			writer.writerow(d)


__all__ = [
	load_json_file.__name__,
	read_whole_file.__name__,
	write_csv.__name__
]
