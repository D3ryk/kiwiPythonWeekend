from grab import Grab
from weblib.error import DataNotFound


class DataParser:
    def __init__(self):
        self.g = Grab()

    def get_all_destination(self):
        self.g.go('https://www.studentagency.cz/data/wc/ybus-form/destinations-cs.json')
        all_destination = self.g.response.json
        all_cities = []

        for destination in all_destination['destinations']:
            if destination['code'] == 'CZ':
                all_cities = destination['cities']
                break

        return all_cities

    def get_connections(self, source, destination, when):
        self.g.go('https://jizdenky.regiojet.cz')
        self.g.go(
            'https://jizdenky.regiojet.cz/Booking/from/{0}/to/{1}/tarif/REGULAR/departure/{2}/retdep/{2}/return/false'.format(
                source, destination, when.strftime('%Y%m%d')))
        self.g.go(
            'https://jizdenky.regiojet.cz/Booking/from/{0}/to/{1}/tarif/REGULAR/departure/{2}/retdep/{2}/return/false?1-1.IBehaviorListener.0-mainPanel-routesPanel&_=1480766048364'.format(
                source, destination, when.strftime('%Y%m%d')))

        connections = []
        for elem in self.g.doc.select('//div[contains(@class, "routeSummary")]'):

            try:
                departure = elem.select('.//div[contains(@class, "col_depart")]')
                arrival = elem.select('.//div[contains(@class, "col_arival")]')
                change = elem.select('.//div[contains(@class, "col_change")]')
                space = elem.select('.//div[contains(@class, "col_space")]')
                price = elem.select('.//div[contains(@class, "col_price")]')
                price = price.text().split()
            except DataNotFound:
                continue

            connections.append({
                'departure': when.strftime('%Y-%m-%d') + ' ' + departure.text(),
                'arrival': when.strftime('%Y-%m-%d') + ' ' + arrival.text(),
                'transfer': change.text(),
                'free_spaces': space.text(),
                'price': price.pop(0),
                'currency': price.pop(0)
            })

        return connections
