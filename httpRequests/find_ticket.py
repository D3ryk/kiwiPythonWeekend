from ticket_searcher import TicketSearcher


ts = TicketSearcher()
connections = ts.get_connections()
print(connections)