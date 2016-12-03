from ticket_searcher import TicketSearcher
from datetime import datetime

ts = TicketSearcher()

connections = ts.get_connections(ts.get_city_id('Praha'), ts.get_city_id('Brno'), datetime.strptime('2016-12-23', '%Y-%m-%d'))
print(connections)
