import Station

class BusNetworkStations(object):
    """description of class"""

    def __init__(self):
        stations = list()

    def __init__(self, stations):
        self.stations = stations
    
    def create_station(self, id, nom, x_position, y_position, next_stations):
        s = Station(id, nom, x_position, y_position, next_stations)
        stations.append(s)

    