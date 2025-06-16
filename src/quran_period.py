from enum import IntEnum


class QuranPeriod(IntEnum):
	UNDEF: int = -1
	MECCAN: int = 0
	MEDINAN: int = 1

	@classmethod
	def _missing_(cls, value):
		try:
			value = int(value)

			if value in cls:
				quran_period = cls(value)
			else:
				quran_period = cls.UNDEF

		except (TypeError, ValueError):
			quran_period = cls.UNDEF
			
		return quran_period


__all__ = [QuranPeriod.__name__]
