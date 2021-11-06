from Business.Trip import Trip

# Contains all the processing methods.
# Not in a function to be called without needing to instanciate (like a static class).

class BusNetworkProcessing(object):
    def __init__(self):
        self.trip = Trip()

    def initialize_vector(self, stations, v_list, v_list_2, start_station_id, type_of_search, o_dict):
        """ This method is used to initialize the v_list vector 
        with the start_station's next_stations travel-time 
        or length depending on the type_of_search parameter. """

        n = len(stations)

        for i in range(0, n):
            try:
                v_list.append(stations[start_station_id].next_stations[i][type_of_search])
                v_list_2.append(stations[start_station_id].next_stations[i][self.i_type_of_search])
                o_dict[i] = start_station_id
            except:
                # the use of try except here is not to handle errors:
                # if the station does not have a next_station, set it's value to inf
                v_list.append(float('inf'))
                v_list_2.append(float('inf'))



    def calculate_trip(self, start_station_id, arrive_station_id, stations, type_of_search):
        """ returns a Trip object.
    
        Calculate the fastest or shortest trip from the start_station_id 
        to the arrive_station_id depending on the type_of_search parameters.
    
        type_of_search : 0 for shortest | 1 for fastest """
       
        if (type_of_search == 0):
            self.i_type_of_search = 1
        else:
            self.i_type_of_search = 0

        n = len(stations) # number of stations

        o_dict = dict() # dictionary for the solution of the algorithm
        o_dict[start_station_id] = start_station_id
        v_list = list() # list of total travel times or lengths
        v_list_2 = list()
        self.initialize_vector(stations, v_list, v_list_2, start_station_id, type_of_search, o_dict)
        e_list = list() # list of already used station indexes
        e_list.append(start_station_id)

        self.result = -1
        self.result_2 = -1

        print(v_list) # debug only
        print("v_list_2:")
        print(v_list_2)
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
            #print(min_val, min_val_id) # debug only
            e_list.append(min_val_id)

            if self.result == -1:
                self.result = v_list[arrive_station_id]
                self.result_2 = v_list_2[arrive_station_id]

            # apply min between V[s] and V[t] + C(t,s) for each summit
            for j in range(0, n):
                if e_list.count(j) == 0:
                    try:
                        if (stations[min_val_id].next_stations[j][type_of_search] + v_list[min_val_id]) < v_list[j]:
                            v_list[j] = (stations[min_val_id].next_stations[j][type_of_search] + v_list[min_val_id])
                            v_list_2[j] = (stations[min_val_id].next_stations[j][self.i_type_of_search] + v_list_2[min_val_id])
                            o_dict[j] = min_val_id
                            if j == arrive_station_id:
                                self.result = v_list[j]
                                self.result_2 = v_list_2[j]
                    except:
                        # means we keep the actual v_list[j]
                        do_nothing = 0 # todo: find a better way to just do nothing
            print("v_list")
            print(v_list) # debug only
            print("v_list_2")
            print(v_list_2)
            print(e_list) # debug only

        

        print(o_dict) # debug only
        print(self.result)
        print("result_2: ")
        print(self.result_2)

        self.trip_steps = list()
        val = arrive_station_id
        for i in range(0, n):
            self.trip_steps.append(val)
            if (val == o_dict[val]):
                val = o_dict[val]
                break;
            val = o_dict[val]

        self.trip_steps.reverse()
        print(self.trip_steps)

    def calculate_both_trips(self, start_station_id, arrive_station_id, stations):
        self.calculate_trip(start_station_id, arrive_station_id, stations, 0)
        self.trip.shortest_trip_length = self.result
        self.trip.shortest_trip = self.trip_steps
        self.trip.shortest_trip_travel_time = self.result_2

        self.calculate_trip(start_station_id, arrive_station_id, stations, 1)
        self.trip.fastest_trip_travel_time = self.result
        self.trip.fastest_trip = self.trip_steps
        self.trip.fastest_trip_length = self.result_2

        print("\n\n\n\n")
        print(self.trip.to_string())

        return self.trip