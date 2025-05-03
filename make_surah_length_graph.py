import matplotlib.pyplot as plt
import mysql.connector

from arg_parser import\
	make_graph_parser
from db_reading import\
	get_surah_ids_chron_order,\
	get_surahs_period_length
from file_io import\
	load_json_file
from surah_graphs import\
	GRAPH_X_LIMIT,\
	make_axes_values


args = make_graph_parser().parse_args()
auth_path = args.auth_path.resolve()
chron_order = args.chron_order

authentication = load_json_file(auth_path)

db_conn = mysql.connector.connect(**authentication)
surah_per_len_data = get_surahs_period_length(db_conn, chron_order)
surah_numbers, surah_lengths, colors\
	= make_axes_values(surah_per_len_data)

graph_title = "Length of the Surahs"
if chron_order:
	graph_title += "\n(Chronological Order)"
	x_indices = *(n for n in range(1, GRAPH_X_LIMIT)),
	x_labels = get_surah_ids_chron_order(db_conn)
else:
	graph_title += "\n(Traditional Order)"
	x_indices = surah_numbers
	x_labels = surah_numbers

plt.bar(x_indices, surah_lengths, color=colors)
plt.title(graph_title)
plt.xlabel("Surah number")
plt.xlim(0, GRAPH_X_LIMIT)
plt.xticks(x_indices, labels=x_labels, rotation=90, fontsize=9)
plt.ylabel("Length (verses)")
plt.tight_layout()
plt.show()
