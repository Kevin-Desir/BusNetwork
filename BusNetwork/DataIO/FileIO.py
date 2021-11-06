import json
import jsonpickle

def read_bus_network_from_json():
    with open('bus_network.json', 'r') as openfile:
        # Reading from json file
        #json_object = json.load(openfile)
        json_object = jsonpickle.decode(openfile.read())

    print(json_object)

    for o in json_object.stations:
        copy = o.next_stations.copy()
        for n in copy:
            #print(n)
            o.next_stations[int(n)] = [o.next_stations[n][0], o.next_stations[n][1]]
            o.next_stations.pop(n)

    return json_object
    
def write_bus_network_to_json(bus_network_stations):
    # Serializing json 
    json_object = jsonpickle.encode(bus_network_stations)
    #json_object = json.dumps(bus_network_stations, indent = 4)
    
    # Writing to sample.json
    with open("bus_network.json", "w") as outfile:
        outfile.write(json_object)
