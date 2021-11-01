class Trip(object):
    """description of class"""

    #def __init__(self, shortest_trip, fastest_trip, shortest_trip_length, shortest_trip_travel_time, fastest_trip_length, fastest_trip_travel_time):
    def __init__(self):
        self.shortest_trip = dict()
        self.fastest_trip = dict()
        self.shortest_trip_length =  -1
        self.fastest_trip_travel_time = -1

    def to_string(self):
        return "Shortest trip: {0}\nShortest trip length: {1}\nFastest trip: {2}\nFastest trip travel time: {3}".format(self.shortest_trip, self.shortest_trip_length, self.fastest_trip, self.fastest_trip_travel_time)