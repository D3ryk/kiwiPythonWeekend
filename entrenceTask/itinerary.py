class Itinerary:
    TRANSFER_LOWER_TIME_BOUNDARY = 60 * 60  # 1 hour
    TRANSFER_UPPER_TIME_BOUNDARY = 60 * 60 * 4  # 4 hours

    def __init__(self, baggage, way, flights_numbers, price, arrival_time):
        self.baggage = int(baggage)
        self.way = str(way)
        self.flightsNumbers = flights_numbers
        self.price = int(price)
        self.arrivalTime = arrival_time

    def toString(self):
        return str(self.baggage) + ',' + self.way + ',[' + ','.join(self.flightsNumbers) + '],' + str(self.price)

    def add_next_stop_to_way(self, flight, baggage):
        return Itinerary(
            self.baggage,
            self.way + '->' + flight.destination,
            self.flightsNumbers + [flight.flight_number],
            self.price + flight.price + baggage * flight.bag_price,
            flight.arrival
        )

    def is_followed_up(self, flight):
        transfer_time_delta = flight.departure - self.arrivalTime
        return self.TRANSFER_LOWER_TIME_BOUNDARY <= transfer_time_delta.seconds <= self.TRANSFER_UPPER_TIME_BOUNDARY

    def is_create_valid_path(self, flight):
        return (self.way[-3::] + '->' + flight.destination not in self.way) and self.way[-3::] == flight.source and self.way[-3::] != flight.destination
