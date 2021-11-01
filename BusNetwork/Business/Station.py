class Station(object):
    """ Station class to test the BusNetworkProcessing methods.
    Will be replace by the real Station class when it will be created."""
    
    def __init__(self, id, nom, x_position, y_position, next_stations):
        """ Constructor. """
        self.id = id
        self.nom = nom
        self.x_position = x_position
        self.y_position = y_position
        self.next_stations = next_stations

    def to_string(self):
        """ To easily print the state of the station. """
        return "{0} : {1} ({2};{3}) {4}".format(self.id, self.nom, self.x_position, self.y_position, self.next_stations)