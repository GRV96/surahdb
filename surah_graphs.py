GRAPH_X_LIMIT = 115

COLOR_MECCAN = "#008000"
COLOR_MEDINIAN = "#e60000"


def color_for_period(period):
	color = None

	if period == 0:
		color = COLOR_MECCAN
	elif period == 1:
		color = COLOR_MEDINIAN

	return color
