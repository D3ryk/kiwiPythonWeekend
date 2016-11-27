class Itinerary:
	
	TRANSFER_LOWER_TIME_BOUNDARY = 60 * 60  # 1 hour
	TRANSFER_UPPER_TIME_BOUNDARY = 60 * 60 * 4 # 4 hours

	def __init__(self, baggage, way, flightsNumbers, price, arrivalTime):
		self.baggage = int(baggage)
		self.way = str(way)
		self.flightsNumbers = flightsNumbers
		self.price = int(price)
		self.arrivalTime = arrivalTime

	def toString(self):
		return str(self.baggage) + ',' + self.way + ',[' + ','.join(self.flightsNumbers) + '],' + str(self.price)

	def addNextStopToWay(self, flight, baggage):		
		return Itinerary(
			self.baggage, 
			self.way + '->' + flight.getDestination(), 
			self.flightsNumbers + [flight.getFlightNumber()], 
			self.price + flight.getPrice() + baggage * flight.getBagPrice(), 
			flight.getArrivalTime()
		)

	def isFollowedUp(self, flight):
		transferTimeDelta = flight.getDepartureTime() - self.arrivalTime
		return self.TRANSFER_LOWER_TIME_BOUNDARY <= transferTimeDelta.seconds <= self.TRANSFER_UPPER_TIME_BOUNDARY

	def isCreateValidPath(self, flight):
		return (self.way[-3::] + '->' + flight.getDestination() not in self.way) and self.way[-3::] == flight.getSource() and self.way[-3::] != flight.getDestination()