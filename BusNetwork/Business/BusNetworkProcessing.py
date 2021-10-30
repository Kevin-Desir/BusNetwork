# Contains all the processing methods.
# Not in a function to be called without needing to instanciate (like a static class).

 
def initialize_vector(stations, v_list, start_station_id, type_of_search, o_dict):
    """ This method is used to initialize the v_list vector 
    with the start_station's next_stations travel-time 
    or length depending on the type_of_search parameter. """

    n = len(stations)

    for i in range(0, n):
        try:
            v_list.append(stations[start_station_id].next_stations[i][type_of_search])
            o_dict[i] = start_station_id
        except: 
            # the use of try except here is not to handle errors:
            # if the station does not have a next_station, set it's value to inf
            v_list.append(float('inf'))


def calculate_trip(start_station_id, arrive_station_id, stations, type_of_search):
    """ returns a Trip object.
    
    Calculate the fastest or shortest trip from the start_station_id 
    to the arrive_station_id depending on the type_of_search parameters.
    
    type_of_search : 0 for shortest | 1 for fastest """


    n = len(stations) # number of stations

    o_dict = dict() # dictionary for the solution of the algorithm
    o_dict[start_station_id] = start_station_id
    v_list = list() # list of total travel times or lengths
    initialize_vector(stations, v_list, start_station_id, type_of_search, o_dict)
    e_list = list() # list of already used station indexes
    e_list.append(start_station_id)

    print(v_list) # debug only
    print(e_list) # debug only
    print(o_dict) # debug only

    for i in range(0, n-1):
        # Search from smallest but not in e_list
        min_val = float('inf')
        min_val_id = -1
        for j in range(0, n):
            if e_list.count(j) == 0:
                if v_list[j] < min_val:
                    min_val = v_list[j]
                    min_val_id = j
        print(min_val, min_val_id) # debug only
        e_list.append(min_val_id)

        # apply min between V[s] and V[t] + C(t,s) for each summit
        for j in range(0, n):
            if e_list.count(j) == 0:
                try:
                    if (stations[min_val_id].next_stations[j][type_of_search] + v_list[min_val_id]) < v_list[j]:
                        v_list[j] = (stations[min_val_id].next_stations[j][type_of_search] + v_list[min_val_id])
                        o_dict[j] = min_val_id
                except:
                    # means we keep the actual v_list[j]
                    do_nothing = 0 # todo: find a better way to just do nothing
        print(v_list) # debug only
        print(e_list) # debug only
    print(o_dict) # debug only
