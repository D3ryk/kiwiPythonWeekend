from flight import Flight
from itinerary import Itinerary


class FlightsSearcherService:
    def __init__(self, flightsData):
        self._flightsData = flightsData

    def findCombination(self):
        flightCombinations = []

        for baggageCount in [0, 1, 2]:
            itineraryQueue = self.getInitializedItineraryQueue(baggageCount)

            while len(itineraryQueue) > 0:
                itinerary = itineraryQueue.pop()

                for flightLine in self._flightsData:
                    flight = Flight(self.getFlightData(flightLine))
                    if baggageCount > 0 and baggageCount != flight.getAllowedBaggage():
                        continue
                    else:
                        if itinerary.isFollowedUp(flight) and itinerary.isCreateValidPath(flight):
                            itineraryQueue.append(
                                itinerary.addNextStopToWay(flight, baggageCount)
                            )

                flightCombinations.append(itinerary)

        return flightCombinations

    def getFlightData(self, flightLine):
        return flightLine.split(',')

    def getInitializedItineraryQueue(self, baggageCount):
        itineraryQueue = []

        for flightLine in self._flightsData:
            flight = Flight(self.getFlightData(flightLine))
            if flight.getAllowedBaggage() >= baggageCount:
                itineraryQueue.append(
                    Itinerary(
                        baggageCount,
                        flight.getSource() + '->' + flight.getDestination(),
                        [flight.getFlightNumber()],
                        flight.getPrice(),
                        flight.getArrivalTime()
                    )
                )

        return itineraryQueue

    def printFlightCombination(self, combinations):
        print('numberOfBaggage,itinerary,listOfFlights,wholePriceIncludingBaggage')
        for itinerary in combinations:
            print(itinerary.toString())
