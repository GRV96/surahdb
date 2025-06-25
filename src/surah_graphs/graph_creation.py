# __all__ declared at the module's end

from src.quran_period import QuranPeriod


COLOR_MECCAN: str = "#008000"
COLOR_MEDINAN: str = "#e60000"

X_LIMIT: int = 115
X_TICKS: tuple[int, ...] = *(n for n in range(1, X_LIMIT)),


def apply_order(
		chron_order: bool,
		surah_nums_mec: list[int],
		surah_nums_med: list[int])\
		-> tuple[list[int], list[int]]:
	"""
	Given the Meccan and Medinan surahs' numbers, this function creates
	abscissas for the graphs by applying the chronological or traditional
	order.

	Args:
		chron_order: If True, the chronological order is applied. If False, the
			traditional order is applied.
		surah_nums_mec: the Meccan surahs' numbers. Their order must match
			argument chron_order.
		surah_nums_med: the Medinan surahs' numbers. Their order must match
			argument chron_order.

	Returns:
		tuple:
			* The abscissas for the Meccan surahs
			* The abscissas for the Medinan surahs
	"""
	if chron_order:
		bound_mec_surahs = len(surah_nums_mec) + 1
		x_indices_mec = [n for n in range(1, bound_mec_surahs)]
		x_indices_med = [n for n in range(bound_mec_surahs, X_LIMIT)]
	else:
		x_indices_mec = surah_nums_mec
		x_indices_med = surah_nums_med

	return x_indices_mec, x_indices_med


def make_axes_values(
		surah_per_len_data: list[tuple], cumulength: bool)\
		-> tuple[list, list, list, list]:
	"""
	This function takes surah data and makes four lists that will serve to
	constitute the graphs' axes.

	* The Meccan surahs' numbers
	* The Medinan surahs' numbers
	* The Meccan surahs' lengths
	* The Medinan surahs' lengths

	Args:
		surah_per_len_data: the surahs' ID, period and length.
		cumulength: If True, the two latter lists contain the lengths'
			cumulative sums. If False, those lists contain the surahs' length.

	Returns:
		tuple: four lists containing the surahs' numbers and lengths.
	"""
	surah_numbers_mec = list()
	surah_numbers_med = list()
	surah_lengths_mec = list()
	surah_lengths_med = list()

	if cumulength:
		length_sum = 0

	for spl in surah_per_len_data:
		surah_number = spl[0]
		period = spl[1]
		surah_length = spl[2]

		if period == QuranPeriod.MECCAN:
			if cumulength:
				length_sum += surah_length
				surah_length = length_sum

			surah_numbers_mec.append(surah_number)
			surah_lengths_mec.append(surah_length)

		elif period == QuranPeriod.MEDINAN:
			if cumulength:
				length_sum += surah_length
				surah_length = length_sum

			surah_numbers_med.append(surah_number)
			surah_lengths_med.append(surah_length)

	return surah_numbers_mec, surah_numbers_med,\
		surah_lengths_mec, surah_lengths_med


__all__ = [
	"COLOR_MECCAN",
	"COLOR_MEDINAN",
	"X_LIMIT",
	"X_TICKS",
	apply_order.__name__,
	make_axes_values.__name__
]
