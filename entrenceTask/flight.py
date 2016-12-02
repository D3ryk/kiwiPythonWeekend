from datetime import datetime


class Flight:
    def __init__(self, flight_data):
        self.source = str(flight_data[0])
        self.destination = str(flight_data[1])
        self.departure = datetime.strptime(flight_data[2], '%Y-%m-%dT%H:%M:%S')
        self.arrival = datetime.strptime(flight_data[3], '%Y-%m-%dT%H:%M:%S')
        self.flight_number = str(flight_data[4])
        self.price = int(flight_data[5])
        self.bags_allowed = int(flight_data[6])
        self.bag_price = int(flight_data[7])
