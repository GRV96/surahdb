from enum import StrEnum


class Language(StrEnum):
	ENGLISH = "en"
	FRENCH = "fr"

	@classmethod
	def _missing_(cls, value):
		if not isinstance(value, str):
			raise TypeError(f"{cls.__name__} values are strings.")

		value_lower = value.lower()

		for language in cls:
			if language == value_lower:
				return language

		raise ValueError(f"{value} is not a {cls.__name__} value.")


__all__ = [Language.__name__]
