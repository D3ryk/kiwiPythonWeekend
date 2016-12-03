from ticket_searcher import TicketSearcher
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--from", type=str, help="source station of searched connection")
parser.add_argument("--to", type=str, help="destination station of searched connection")
parser.add_argument("--when", type=str, help="date of searched connection")
args = vars(parser.parse_args())

ts = TicketSearcher()

connections = ts.get_connections(ts.get_city_id(args['from']), ts.get_city_id(args['to']), datetime.strptime(args['when'], '%Y-%m-%d'))
best_connection = ts.get_best_connection(connections)
print(best_connection)
