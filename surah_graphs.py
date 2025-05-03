GRAPH_X_LIMIT = 115

COLOR_MECCAN = "#008000"
COLOR_MEDINIAN = "#e60000"


def apply_order(chron_order, surah_numbers, ids_chron_fnc):
	if chron_order:
		graph_title_suffix = "\n(Chronological Order)"
		x_indices = *(n for n in range(1, GRAPH_X_LIMIT)),
		x_labels = ids_chron_fnc()
	else:
		graph_title_suffix = "\n(Traditional Order)"
		x_indices = surah_numbers
		x_labels = surah_numbers

	return graph_title_suffix, x_indices, x_labels


def color_for_period(period):
	color = None

	if period == 0:
		color = COLOR_MECCAN
	elif period == 1:
		color = COLOR_MEDINIAN

	return color


def make_axes_values(surah_per_len_data):
	surah_numbers = list()
	surah_lengths = list()
	colors = list()

	for spl in surah_per_len_data:
		surah_numbers.append(spl[0])
		colors.append(color_for_period(spl[1]))
		surah_lengths.append(spl[2])

	return surah_numbers, surah_lengths, colors


def make_axes_values_cumulength(surah_per_len_data):
	surah_numbers = list()
	nb_verses_read = list()
	sum_verses_read = 0
	colors = list()

	for spl in surah_per_len_data:
		surah_numbers.append(spl[0])
		colors.append(color_for_period(spl[1]))
		sum_verses_read += spl[2]
		nb_verses_read.append(sum_verses_read)

	return surah_numbers, nb_verses_read, colors
