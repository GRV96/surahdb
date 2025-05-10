# __all__ declared at the module's end

from .quran_periods import\
	PERIOD_MECCAN,\
	PERIOD_MEDINAN


COLOR_MECCAN = "#008000"
COLOR_MEDINAN = "#e60000"

LABEL_MECCAN = "Meccan surahs"
LABEL_MEDINAN = "Medinan surahs"

X_LIMIT = 115
X_TICKS = *(n for n in range(1, X_LIMIT)),


def apply_order(chron_order, surah_nums_mec, surah_nums_med):
	if chron_order:
		graph_title_suffix = "\n(Chronological Order)"
		bound_mec_surahs = len(surah_nums_mec) + 1
		x_indices_mec = *(n for n in range(1, bound_mec_surahs)),
		x_indices_med = *(n for n in range(bound_mec_surahs, X_LIMIT)),
	else:
		graph_title_suffix = "\n(Traditional Order)"
		x_indices_mec = surah_nums_mec
		x_indices_med = surah_nums_med

	return graph_title_suffix, x_indices_mec, x_indices_med


def color_for_period(period):
	color = None

	if period == PERIOD_MECCAN:
		color = COLOR_MECCAN
	elif period == PERIOD_MEDINAN:
		color = COLOR_MEDINAN

	return color


def make_axes_values(surah_per_len_data, cumulength):
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

		if period == PERIOD_MECCAN:
			if cumulength:
				length_sum += surah_length
				surah_length = length_sum

			surah_numbers_mec.append(surah_number)
			surah_lengths_mec.append(surah_length)

		elif period == PERIOD_MEDINAN:
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
	"LABEL_MECCAN",
	"LABEL_MEDINAN",
	"X_LIMIT",
	"X_TICKS",
	apply_order.__name__,
	color_for_period.__name__,
	make_axes_values.__name__
]
