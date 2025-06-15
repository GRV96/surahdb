from enum import Enum


class QuranPeriod(Enum):
	UNDEF: int = -1
	MECCAN: int = 0
	MEDINAN: int = 1

	@staticmethod
	def from_int(number):
		try:
			quran_period = QuranPeriod(number)
		except ValueError:
			quran_period = QuranPeriod.UNDEF
			
		return quran_period
