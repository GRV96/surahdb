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

for sl in surah_length_data[:6]:
	print(f"{sl[0]}: {sl[1]}")
