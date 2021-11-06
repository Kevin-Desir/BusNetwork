import Station

class BusNetworkStations(object):
    """description of class"""

    def __init__(self):
        self.stations = list()

    def set_stations(self, stations):
        self.stations = stations
    
    def create_station(self, id, nom, x_position, y_position, next_stations):
        s = Station(id, nom, x_position, y_position, next_stations)
        self.stations.append(s)

    def add_station(self, station):
        self.stations.append(station)

    def print_all_stations(self):
        for s in self.stations:
            print(s.to_string())

    def get_all_station_names(self):
        station_names = list()

        for s in self.stations:
            station_names.append(s.nom)

        return station_names

    def get_station_id_by_name(self, name):
        for s in self.stations:
            if name == s.nom:
                return int(s.id)

    def get_all_stations(self):
        return self.stations

    def get_station_by_name(self, name):
        for s in self.stations:
            if name == s.nom:
                return s

    def get_count(self):
        return len(self.stations)

    def delete_last_station(self):
        self.stations.pop()