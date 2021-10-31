import Station

class BusNetworkStations(object):
    """description of class"""

    def __init__(self):
        self.stations = list()

    def __init__(self, stations):
        self.stations = stations
    
    def create_station(self, id, nom, x_position, y_position, next_stations):
        s = Station(id, nom, x_position, y_position, next_stations)
        self.stations.append(s)

    def add_station(self, station):
        self.stations.append(station)

    def print_all_stations(self):
        for s in self.stations:
            print(s.to_string())