from ticket_searcher import TicketSearcher


ts = TicketSearcher()

connections = ts.get_connections(ts.get_city_id('Praha'), ts.get_city_id('Brno'), '2016-12-20')
print(connections)
#ts.show_last_response_in_browser()
