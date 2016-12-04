from ticket_searcher import TicketSearcher
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()

required = parser.add_argument_group('required arguments')
required.add_argument("-f", "--from", type=str, help="source station of searched connection", required=True)
required.add_argument("-t", "--to", type=str, help="destination station of searched connection", required=True)

parser.add_argument("--when", type=str, help="date of searched connection")
args = vars(parser.parse_args())

if not args['when']:
    args['when'] = datetime.today().strftime('%Y-%m-%d')

ts = TicketSearcher()

connections = ts.get_connections(ts.get_city_id(args['from']), ts.get_city_id(args['to']), datetime.strptime(args['when'], '%Y-%m-%d'))
best_connection = ts.get_best_connection(connections)
print(best_connection)
