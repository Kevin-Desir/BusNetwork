import os
import sys

""" Add the business folder path to the sys path to be able to use the files 
    from this file, which is in a different directory. """
script_dir = os.path.dirname( __file__ )
busnetworkprocessing_dir = os.path.join( script_dir, '..', 'Business' )
sys.path.append( busnetworkprocessing_dir )

import BusNetworkProcessing 

""" File used to test the methods from the BusNetworkProcessing file. """

class Station:
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
        return "{0} : {1} ({2};{3}){4}".format(self.id, self.nom, self.x_position, self.y_position, self.next_stations)

next_stations_0 = {
        3: [35, 35],
        2: [42, 42],
        8: [40, 40]
    }
next_stations_1 = {
        9: [40, 40],
        7: [35, 35],
        4: [32, 32],
        5: [27, 27]
    }
next_stations_2 = {
        3: [43, 43],
        0: [42, 42],
        6: [9, 9],
        9: [32, 32]
    }
next_stations_3 = {
        2: [43, 43],
        0: [35, 35]
    }
next_stations_4 = {
        1: [32, 32]
    }
next_stations_5 = {
        1: [27, 27],
        9: [69, 69]
    }
next_stations_6 = {
        2: [9, 9],
        8: [19, 19]
    }
next_stations_7 = {
        1: [35, 35],
        9: [76, 76]
    }
next_stations_8 = {
        0: [40, 40],
        6: [19, 19],
        9: [29, 29]
    }
next_stations_9 = {
        7: [76, 76],
        1: [40, 40],
        5: [69, 69],
        2: [32, 32],
        8: [29, 29]
    }

stations = [
    Station(0, "Les Andelys", 0, 0, next_stations_0),
    Station(1, "Bolbec", 0, 0, next_stations_1),
    Station(2, "Elbeuf", 0, 0, next_stations_2),
    Station(3, "Evreux", 0, 0, next_stations_3),
    Station(4, "Etretat", 0, 0, next_stations_4),
    Station(5, "Fécamp", 0, 0, next_stations_5),
    Station(6, "Grand-Couronne", 0, 0, next_stations_6),
    Station(7, "Le Havre", 0, 0, next_stations_7),
    Station(8, "Rouen", 0, 0, next_stations_8),
    Station(9, "Jumièges", 0, 0, next_stations_9)
]

BusNetworkProcessing.calculate_trip(8, 5, stations, 1)
# Expected results: 
# from 8 to 5: 8 9 1 5
# from 8 to 3: 8 6 2 3