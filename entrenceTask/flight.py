from datetime import datetime


class Flight:
    def __init__(self, flightData):
        self._source = str(flightData[0])
        self._destination = str(flightData[1])
        self._departure = datetime.strptime(flightData[2], '%Y-%m-%dT%H:%M:%S')
        self._arrival = datetime.strptime(flightData[3], '%Y-%m-%dT%H:%M:%S')
        self._flight_number = str(flightData[4])
        self._price = int(flightData[5])
        self._bags_allowed = int(flightData[6])
        self._bag_price = int(flightData[7])

    def getAllowedBaggage(self):
        return self._bags_allowed

    def getSource(self):
        return self._source

    def getDestination(self):
        return self._destination

    def getFlightNumber(self):
        return self._flight_number

    def getPrice(self):
        return self._price

    def getBagPrice(self):
        return self._bag_price

    def getArrivalTime(self):
        return self._arrival

    def getDepartureTime(self):
        return self._departure
