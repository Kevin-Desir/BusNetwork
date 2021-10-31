import tkinter as tk
from tkinter import ttk

import os
import sys

""" Add the tests folder path to the sys path to be able to use the files 
    from this file, which is in a different directory. """
script_dir = os.path.dirname( __file__ )

#tests_dir = os.path.join( script_dir, '..', 'Tests' )
#sys.path.append( tests_dir )
#import BusNetworkProcessingTests 

business_dir = os.path.join( script_dir, '..', 'Business' )
sys.path.append( business_dir )
from Station import Station


class AddStationWindow(object):
    def add_station_button_pressed(self):
        next_stations_10 = {
                7: [76, 76],
                1: [40, 40],
                5: [69, 69],
                2: [32, 32],
                8: [29, 29]
            }
        s_1 = Station(10, "Nouvelle station", 0, 0, next_stations_10)

        self.root.bus_network_stations.add_station(s_1)
        self.root.bus_network_stations.print_all_stations()

    def on_arrive_station_selected(self, event):
        selection = event.widget.curselection()
        index = selection[0]
        data = event.widget.get(index)
        
        print(str(index) + " -> " + data)    

    def __init__(self, root):
        self.root = root

        self.window = tk.Toplevel(root)

        self.window.title("Ajout de station")
    
        self.window.grab_set() # rendre la fenêtre modale

        self.window.geometry("300x300")

        
        label_station_name = ttk.Label(self.window, text="Nom de la Station")
        label_station_name.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        entry_station_name = ttk.Entry(self.window)
        entry_station_name.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        label_station_id = ttk.Label(self.window, text="ID de station")
        label_station_id.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        entry_station_id = ttk.Entry(self.window)
        entry_station_id.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        label_arrive_stations = ttk.Label(self.window, text="Stations d'arrivée")
        label_arrive_stations.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        button_create_arrive_station = ttk.Button(self.window, text="+")
        button_create_arrive_station.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

        frame_arrive_stations = ttk.Frame(self.window)
        frame_arrive_stations.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

        frame_arrive_stations.rowconfigure(0, weight=1)
        frame_arrive_stations.columnconfigure(0, weight=1)
        frame_arrive_stations.columnconfigure(1, weight=0)

        scrollbar_y = ttk.Scrollbar(frame_arrive_stations, orient='vertical')
        scrollbar_y.grid(row=0, column=1, sticky=tk.NS)

        listbox_arrive_stations = tk.Listbox(frame_arrive_stations, yscrollcommand=scrollbar_y.set)
        listbox_arrive_stations.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar_y['command'] = listbox_arrive_stations.yview

        listbox_arrive_stations.bind('<<ListboxSelect>>', self.on_arrive_station_selected)

        listbox_arrive_stations.insert("0", "1", "2", "3")

        