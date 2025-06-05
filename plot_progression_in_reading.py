"""
This script produces a graph showing the progression in the Quran's reading
based on the last surah entirely read.
"""


import matplotlib.pyplot as plt
import mysql.connector

from src.arg_parser import\
	make_parser_plots
from src.database.db_config_validation import\
	validate_db_config
from src.database.db_reading import\
	COLUMN_ID,\
	COLUMN_PERIOD,\
	COLUMN_NB_VERSES,\
	get_surah_data
from src.file_io import\
	load_json_file
from src.quran_periods import\
	PERIOD_UNDEF
from src.surah_graphs import\
	GraphText
from src.surah_graphs.graph_creation import\
	COLOR_MECCAN,\
	COLOR_MEDINAN,\
	X_LIMIT,\
	X_TICKS,\
	apply_order,\
	make_axes_values


args = make_parser_plots(__doc__).parse_args()
db_config_path = args.db_config.resolve()
chron_order = args.chron_order
graph_lang = args.language

db_config = load_json_file(db_config_path)
validate_db_config(db_config)
db_conn = mysql.connector.connect(**db_config)

surah_per_len_data = get_surah_data(db_conn, chron_order, PERIOD_UNDEF,
	COLUMN_ID, COLUMN_PERIOD, COLUMN_NB_VERSES)
surah_nums_mec, surah_nums_med, surah_lengths_mec, surah_lengths_med\
	= make_axes_values(surah_per_len_data, True)

x_indices_mec, x_indices_med\
	= apply_order(chron_order, surah_nums_mec, surah_nums_med)

if chron_order:
	x_labels = get_surah_data(db_conn, True, PERIOD_UNDEF, COLUMN_ID)
else:
	x_labels = X_TICKS

graph_text = GraphText()

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
ax.scatter(x_indices_mec, surah_lengths_mec,
	color=COLOR_MECCAN, label=graph_text.get_legend_meccan(graph_lang))
ax.scatter(x_indices_med, surah_lengths_med,
	color=COLOR_MEDINAN, label=graph_text.get_legend_medinan(graph_lang))
ax.set_title(graph_text.get_title_reading_progression(chron_order, graph_lang))
ax.set_xlabel(graph_text.get_label_last_surah_read(graph_lang))
ax.set_xlim(0, X_LIMIT)
ax.set_xticks(X_TICKS, labels=x_labels, rotation=90, fontsize=9)
ax.set_ylabel(graph_text.get_label_verses_read(graph_lang))
ax.set_yticks(range(0, 6001, 500), minor=True)
ax.grid(True, which="both")
figure.tight_layout()
plt.legend()
plt.show()
