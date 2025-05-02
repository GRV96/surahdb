import matplotlib.pyplot as plt
import mysql.connector

from arg_parser import\
	make_graph_parser
from db_reading import\
	get_surahs_length
from file_io import\
	load_json_file


args = make_graph_parser().parse_args()
auth_path = args.auth_path.resolve()
chron_order = args.chron_order

authentication = load_json_file(auth_path)

db_conn = mysql.connector.connect(**authentication)
surah_length_data = get_surahs_length(db_conn, chron_order)

surah_ids = list()
surah_lengths = list()
for sl in surah_length_data:
	surah_ids.append(sl[0])
	surah_lengths.append(sl[1])

plt.bar(surah_ids, surah_lengths)

plt.title("Length of the Surahs")
plt.xlabel("Surah number")
plt.xlim(0, 114)
plt.ylabel("Number of verses")
plt.tight_layout()
plt.show()
