import matplotlib.pyplot as plt
import mysql.connector

from arg_parser import\
	make_graph_parser
from db_reading import\
	get_surah_ids_chron_order,\
	get_surahs_length
from file_io import\
	load_json_file


_X_LIMIT = 115


args = make_graph_parser().parse_args()
auth_path = args.auth_path.resolve()
chron_order = args.chron_order

authentication = load_json_file(auth_path)

db_conn = mysql.connector.connect(**authentication)
surah_length_data = get_surahs_length(db_conn, chron_order)

surah_numbers = list()
verses_read = list()
sum_verses_read = 0
for sl in surah_length_data:
	surah_numbers.append(sl[0])
	sum_verses_read += sl[1]
	verses_read.append(sum_verses_read)

graph_title = "Progression in the Quran's Reading"
if chron_order:
	graph_title += "\n(Chronological Order)"
	x_indices = *(n for n in range(1, _X_LIMIT)),
	x_labels = get_surah_ids_chron_order(db_conn)
else:
	graph_title += "\n(Traditional Order)"
	x_indices = surah_numbers
	x_labels = surah_numbers

plt.plot(x_indices, verses_read)
plt.title(graph_title)
plt.xlabel("Last surah read")
plt.xlim(0, _X_LIMIT)
plt.xticks(x_indices, labels=x_labels, rotation=90, fontsize=9)
plt.ylabel("Verses read")
plt.tight_layout()
plt.show()
