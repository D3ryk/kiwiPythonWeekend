from ticket_searcher import TicketSearcher


ts = TicketSearcher()
connections = ts.get_connections()
print(connections[0])
#ts.show_last_response_in_browser()