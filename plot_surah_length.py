import matplotlib.pyplot as plt
import mysql.connector

from src.arg_parser import\
	make_graph_parser
from src.db_reading import\
	get_surahs_period_length
from src.file_io import\
	load_json_file
from src.surah_graphs import\
	GRAPH_X_LIMIT,\
	apply_order,\
	make_axes_values


args = make_graph_parser().parse_args()
auth_path = args.auth_path.resolve()
chron_order = args.chron_order

authentication = load_json_file(auth_path)
db_conn = mysql.connector.connect(**authentication)

surah_per_len_data = get_surahs_period_length(db_conn, chron_order)
surah_numbers, surah_lengths, colors\
	= make_axes_values(surah_per_len_data)

graph_title_suffix, x_indices = apply_order(chron_order, surah_numbers)

plt.bar(x_indices, surah_lengths, color=colors)
plt.title("Length of the Surahs" + graph_title_suffix)
plt.xlabel("Surah number")
plt.xlim(0, GRAPH_X_LIMIT)
plt.xticks(x_indices, labels=surah_numbers, rotation=90, fontsize=9)
plt.ylabel("Length (verses)")
plt.grid(True, axis="y")
plt.tight_layout()
plt.show()
