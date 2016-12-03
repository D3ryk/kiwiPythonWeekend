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
        self.g.go(
            'https://jizdenky.regiojet.cz/Booking/from/10202002/to/10202003/tarif/REGULAR/departure/20161203/retdep/20161203/return/false')
        self.g.go(
            'https://jizdenky.regiojet.cz/Booking/from/10202002/to/10202003/tarif/REGULAR/departure/20161203/retdep/20161203/return/false?1-1.IBehaviorListener.0-mainPanel-routesPanel&_=1480766048364')
        self.g.response.browse()

        connections = []
        for elem in self.g.doc.select('//div[contains(@class, "item_blue")]'):
            connection = elem.text().split()
            connections.append({
                'departure': connection[0],
                'arrival': connection[1],
                'transfer': connection[2],
                'free_spaces': connection[3],
                'price': connection[4],
                'currency': connection[5]
            })

        return connections

    def get_best_connections(self, connections):
        return {}
