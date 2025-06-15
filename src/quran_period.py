from enum import Enum


class QuranPeriod(Enum):
	UNDEF: int = -1
	MECCAN: int = 0
	MEDINAN: int = 1

	@staticmethod
	def from_value(val):
		try:
			if isinstance(val, str):
				val = int(val)

			quran_period = QuranPeriod(val)

		except ValueError:
			quran_period = QuranPeriod.UNDEF
			
		return quran_period


__all__ = [QuranPeriod.__name__]
