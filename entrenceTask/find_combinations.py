from flightsSearcherService import FlightsSearcherService
import sys

flights = sys.stdin.read().split()

flightsSearcherService = FlightsSearcherService(flights[1::])
flightsSearcherService.printFlightCombination(
    flightsSearcherService.findCombination()
)
