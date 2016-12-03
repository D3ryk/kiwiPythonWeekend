from ticket_searcher import TicketSearcher
from datetime import datetime

ts = TicketSearcher()

connections = ts.get_connections(ts.get_city_id('Praha'), ts.get_city_id('Brno'), datetime.strptime('2016-12-25', '%Y-%m-%d'))
best_connection = ts.get_best_connection(connections)
print(best_connection)
