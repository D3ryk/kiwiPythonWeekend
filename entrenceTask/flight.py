from datetime import datetime


class Flight:
    def __init__(self, flightData):
        self.source = str(flightData[0])
        self.destination = str(flightData[1])
        self.departure = datetime.strptime(flightData[2], '%Y-%m-%dT%H:%M:%S')
        self.arrival = datetime.strptime(flightData[3], '%Y-%m-%dT%H:%M:%S')
        self.flight_number = str(flightData[4])
        self.price = int(flightData[5])
        self.bags_allowed = int(flightData[6])
        self.bag_price = int(flightData[7])
