from ticket_searcher import TicketSearcher
from datetime import datetime, date
import argparse

# script argument setup
parser = argparse.ArgumentParser()

required = parser.add_argument_group('required arguments')
required.add_argument("-f", "--from", type=str, help="source station of searched connection", required=True)
required.add_argument("-t", "--to", type=str, help="destination station of searched connection", required=True)

parser.add_argument("-w", "--when", type=str, help="date of searched connection")
args = vars(parser.parse_args())

# --when/-w parameter sanitation
if args['when']:
    try:
        args['when'] = datetime.strptime(args['when'], '%Y-%m-%d')
    except ValueError:
        exit('Bad date format for parameter --when/-w should be in %Y-%m-%d')

    if datetime.date(args['when']) < date.today():
        exit('Provided date is from past')
else:
    args['when'] = datetime.today()

# main logic
# cmd script don't respect any config search restrictions
ts = TicketSearcher({})

connections = ts.get_connections(
    ts.get_city_id(args['from']),
    ts.get_city_id(args['to']),
    args['when']
)

best_connection = ts.get_best_connection(connections)
print(best_connection)
