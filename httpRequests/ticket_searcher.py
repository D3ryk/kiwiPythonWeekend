from grab import Grab


class TicketSearcher:
    def __init__(self):
        self.g = Grab()
        self.g.go('https://www.studentagency.cz/data/wc/ybus-form/destinations-cs.json')
        self.all_rides = self.g.response.json

    def show_last_response_in_browser(self):
        self.g.response.browse()

    def get_connections(self):
        self.g.go('https://jizdenky.regiojet.cz')
        self.g.go('https://jizdenky.regiojet.cz/Booking/from/10202002/to/10202003/tarif/REGULAR/departure/20161203/retdep/20161203/return/false')
        self.g.go('https://jizdenky.regiojet.cz/Booking/from/10202002/to/10202003/tarif/REGULAR/departure/20161203/retdep/20161203/return/false?1-1.IBehaviorListener.0-mainPanel-routesPanel&_=1480766048364')

        connections = []
        for elem in self.g.doc.select('//div[contains(@class, "routeSummary")]'):
            departure = elem.select('//div[contains(@class, "col_depart")]')
            arival = elem.select('//div[contains(@class, "col_arival")]')
            change = elem.select('//div[contains(@class, "col_change")]')
            space = elem.select('//div[contains(@class, "col_space")]')
            price = elem.select('//div[contains(@class, "col_price")]')
            price = price.text().split()

            connections.append({
                'departure': departure.text(),
                'arrival': arival.text(),
                'transfer': change.text(),
                'free_spaces': space.text(),
                'price': price[0],
                'currency': price[1]
            })

        return connections
