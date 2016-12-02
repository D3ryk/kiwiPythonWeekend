from flight import Flight
from itinerary import Itinerary


class FlightsSearcherService:
    def __init__(self, flights_data):
        self._flightsData = flights_data

    def find_combination(self):
        flight_combinations = []

        for baggageCount in [0, 1, 2]:
            itinerary_queue = self.get_initialized_itinerary_queue(baggageCount)

            while len(itinerary_queue) > 0:
                itinerary = itinerary_queue.pop()

                for flightLine in self._flightsData:
                    flight = Flight(self.get_flight_data(flightLine))
                    if baggageCount > 0 and baggageCount != flight.bags_allowed:
                        continue
                    else:
                        if itinerary.is_followed_up(flight) and itinerary.is_create_valid_path(flight):
                            itinerary_queue.append(
                                itinerary.add_next_stop_to_way(flight, baggageCount)
                            )

                flight_combinations.append(itinerary)

        return flight_combinations

    def get_flight_data(self, flight_line):
        return flight_line.split(',')

    def get_initialized_itinerary_queue(self, baggage_count):
        itinerary_queue = []

        for flightLine in self._flightsData:
            flight = Flight(self.get_flight_data(flightLine))
            if flight.bags_allowed >= baggage_count:
                itinerary_queue.append(
                    Itinerary(
                        baggage_count,
                        flight.source + '->' + flight.destination,
                        [flight.flight_number],
                        flight.price,
                        flight.arrival
                    )
                )

        return itinerary_queue

    def print_flight_combination(self, combinations):
        print('numberOfBaggage,itinerary,listOfFlights,wholePriceIncludingBaggage')
        for itinerary in combinations:
            print(itinerary)
