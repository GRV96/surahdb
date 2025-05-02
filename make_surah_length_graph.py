import matplotlib.pyplot as plt
import mysql.connector

from arg_parser import\
	make_graph_parser
from db_reading import\
	get_surah_ids_chron_order,\
	get_surahs_length
from file_io import\
	load_json_file


_NB_SURAHS = 114


args = make_graph_parser().parse_args()
auth_path = args.auth_path.resolve()
chron_order = args.chron_order

authentication = load_json_file(auth_path)

db_conn = mysql.connector.connect(**authentication)
surah_length_data = get_surahs_length(db_conn, chron_order)

surah_numbers = list()
surah_lengths = list()
for sl in surah_length_data:
	surah_numbers.append(sl[0])
	surah_lengths.append(sl[1])

graph_title = "Length of the Surahs"
if chron_order:
	graph_title += "\n(Chronological Order)"
	x_indices = *(n for n in range(1, _NB_SURAHS+1)),
	x_labels = get_surah_ids_chron_order(db_conn)
else:
	graph_title += "\n(Traditional Order)"
	x_indices = surah_numbers
	x_labels = surah_numbers

plt.bar(x_indices, surah_lengths)
plt.title(graph_title)
plt.xlabel("Surah number")
plt.xlim(0, _NB_SURAHS)
plt.xticks(x_indices, labels=x_labels)
plt.ylabel("Length (verses)")
plt.tight_layout()
plt.show()
