from pathlib import Path

from src.file_io import load_json_file
from .language import Language


_KEY_TITLE_SURAH_LENGTH = "title_surah_length"
_KEY_TITLE_READING_PROGRESSION = "title_reading_progression"
_KEY_SUFFIX_CHRON = "suffix_chron"
_KEY_SUFFIX_TRAD = "suffix_trad"
_KEY_LEGEND_MECCAN = "legend_meccan"
_KEY_LEGEND_MEDINAN = "legend_medinan"
_KEY_SURAH_NUMBER = "label_surah_number"
_KEY_LAST_SURAH_READ = "label_last_surah_read"
_KEY_LABEL_SURAH_LENGTH = "label_surah_length"
_KEY_LABEL_VERSES_READ = "label_verses_read"


def _get_title_suffix_key(chron_order: bool):
	if chron_order:
		suffix_key = _KEY_SUFFIX_CHRON
	else:
		suffix_key = _KEY_SUFFIX_TRAD

	return suffix_key


class GraphText:
	"""
	This singleton provides all the inscriptions that can appear on the graphs
	produced by this repository. All texts are available in French and English.
	"""

	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance._load_content()

		return cls._instance

	def _load_content(self) -> None:
		content_path\
			= Path(__file__).resolve().parent/"graph_inscriptions.json"

		self._content = load_json_file(content_path)

	def get_title_surah_length(self, chron_order: bool, language: Language) -> str:
		title = self._content[_KEY_TITLE_SURAH_LENGTH][language.value]

		suffix_key = _get_title_suffix_key(chron_order)
		suffix = self._content[suffix_key][language.value]

		return title + suffix

	def get_title_reading_progression(
			self, chron_order: bool, language: Language) -> str:
		title = self._content[_KEY_TITLE_READING_PROGRESSION][language.value]

		suffix_key = _get_title_suffix_key(chron_order)
		suffix = self._content[suffix_key][language.value]

		return title + suffix

	def get_label_surah_number(self, language: Language) -> str:
		return self._content[_KEY_SURAH_NUMBER][language.value]

	def get_label_last_surah_read(self, language: Language) -> str:
		return self._content[_KEY_LAST_SURAH_READ][language.value]

	def get_label_surah_length(self, language: Language) -> str:
		return self._content[_KEY_LABEL_SURAH_LENGTH][language.value]

	def get_label_verses_read(self, language: Language) -> str:
		return self._content[_KEY_LABEL_VERSES_READ][language.value]

	def get_legend_meccan(self, language: Language) -> str:
		return self._content[_KEY_LEGEND_MECCAN][language.value]

	def get_legend_medinan(self, language: Language) -> str:
		return self._content[_KEY_LEGEND_MEDINAN][language.value]


__all__ = [GraphText.__name__]
