import matplotlib.pyplot as plt
import mysql.connector

from src.arg_parser import\
	make_parser_plots
from src.db_reading import\
	COLUMN_ID,\
	COLUMN_PERIOD,\
	COLUMN_NB_VERSES,\
	PERIOD_UNDEF,\
	get_surah_data
from src.file_io import\
	load_json_file
from src.surah_graphs import\
	COLOR_MECCAN,\
	COLOR_MEDINAN,\
	LABEL_MECCAN,\
	LABEL_MEDINAN,\
	X_LIMIT,\
	X_TICKS,\
	apply_order,\
	make_axes_values


args = make_parser_plots().parse_args()
auth_path = args.auth_path.resolve()
chron_order = args.chron_order

authentication = load_json_file(auth_path)
db_conn = mysql.connector.connect(**authentication)

surah_per_len_data = get_surah_data(db_conn, chron_order, PERIOD_UNDEF,
	COLUMN_ID, COLUMN_PERIOD, COLUMN_NB_VERSES)
surah_nums_mec, surah_nums_med, surah_lengths_mec, surah_lengths_med\
	= make_axes_values(surah_per_len_data, False)

graph_title_suffix, x_indices_mec, x_indices_med\
	= apply_order(chron_order, surah_nums_mec, surah_nums_med)

if chron_order:
	x_labels = get_surah_data(db_conn, True, PERIOD_UNDEF, COLUMN_ID)
else:
	x_labels = X_TICKS

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
ax.bar(x_indices_mec, surah_lengths_mec,
	color=COLOR_MECCAN, label=LABEL_MECCAN)
ax.bar(x_indices_med, surah_lengths_med,
	color=COLOR_MEDINAN, label=LABEL_MEDINAN)
ax.set_title("Length of the Surahs" + graph_title_suffix)
ax.set_xlabel("Surah number")
ax.set_xlim(0, X_LIMIT)
ax.set_xticks(X_TICKS, labels=x_labels, rotation=90, fontsize=9)
ax.set_ylabel("Length (verses)")
ax.grid(True, axis="y")
figure.tight_layout()
plt.legend()
plt.show()
