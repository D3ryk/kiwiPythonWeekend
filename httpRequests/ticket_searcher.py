from grab import Grab


class TicketSearcher:
    def __init__(self):
        self.g = Grab()
        self.g.go('https://www.studentagency.cz/data/wc/ybus-form/destinations-cs.json')
        self.all_destination = self.g.response.json

        for destination in self.all_destination['destinations']:
            if destination['code'] == 'CZ':
                self.all_cities = destination['cities']
                break

    def show_last_response_in_browser(self):
        self.g.response.browse()

    def get_connections(self, source, destination, when):
        self.g.go('https://jizdenky.regiojet.cz')
        self.g.go('https://jizdenky.regiojet.cz/Booking/from/{0}/to/{1}/tarif/REGULAR/departure/{2}/retdep/{2}/return/false'.format(source, destination, when))
        self.g.go('https://jizdenky.regiojet.cz/Booking/from/{0}/to/{1}/tarif/REGULAR/departure/{2}/retdep/{2}/return/false?1-1.IBehaviorListener.0-mainPanel-routesPanel&_=1480766048364'.format(source, destination, when))

        connections = []
        for elem in self.g.doc.select('//div[contains(@class, "routeSummary")]'):
            departure = elem.select('//div[contains(@class, "col_depart")]')
            arrival = elem.select('//div[contains(@class, "col_arival")]')
            change = elem.select('//div[contains(@class, "col_change")]')
            space = elem.select('//div[contains(@class, "col_space")]')
            price = elem.select('//div[contains(@class, "col_price")]')
            price = price.text().split()

            connections.append({
                'departure': departure.text(),
                'arrival': arrival.text(),
                'transfer': change.text(),
                'free_spaces': space.text(),
                'price': price.pop(0),
                'currency': price.pop(0)
            })

        return connections

    def get_city_id(self, name):
        city_id = [city['id'] for city in self.all_cities if city['name'] == name]

        if not city_id:
            exit('City ' + name + ' wasn\'t found in city dictionary')

        return city_id.pop(0)

