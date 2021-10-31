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

from Windows.AddNextStationWindow import AddNextStationWindow

class AddStationWindow(object):
    def add_station_button_pressed(self):
        try:
            s_id = int(self.entry_station_id.get())

            next_stations_10 = {
                    7: [76, 76],
                    1: [40, 40],
                    5: [69, 69],
                    2: [32, 32],
                    8: [29, 29]
                }
            s = Station(s_id, self.entry_station_name.get(), 0, 0, next_stations_10)

            self.root.bus_network_stations.add_station(s)
            self.root.bus_network_stations.print_all_stations()
        except:
            print("Format du nombre invalide : ID de la station.")

    def on_arrive_station_selected(self, event):
        selection = event.widget.curselection()
        index = selection[0]
        data = event.widget.get(index)
        
        print(str(index) + " -> " + data)    

    def add_arrive_station_pressed(self):
        add_next_station_window = AddNextStationWindow(self)

    def on_close_window_pressed(self):
        print("close window")
        self.window.destroy()

    def __init__(self, root):
        self.root = root

        self.window = tk.Toplevel(root)

        self.window.title("Ajout de station")
    
        self.window.grab_set() # rendre la fenêtre modale

        self.window.geometry("300x350")

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=0)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        
        self.label_station_name = ttk.Label(self.window, text="Nom de la Station")
        self.label_station_name.grid(row=0, column=0, sticky=tk.NS, padx=5, pady=5)

        self.entry_station_name = ttk.Entry(self.window)
        self.entry_station_name.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        self.label_station_id = ttk.Label(self.window, text="ID de station")
        self.label_station_id.grid(row=1, column=0, sticky=tk.NS, padx=5, pady=5)

        self.entry_station_id = ttk.Entry(self.window)
        self.entry_station_id.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.label_arrive_stations = ttk.Label(self.window, text="Stations d'arrivée")
        self.label_arrive_stations.grid(row=2, column=0, sticky=tk.S, padx=5, pady=15)

        self.button_create_arrive_station = ttk.Button(self.window, text="+", command=lambda: self.add_arrive_station_pressed())
        self.button_create_arrive_station.grid(row=2, column=1, sticky=tk.S, padx=5, pady=15)

        self.frame_arrive_stations = ttk.Frame(self.window)
        self.frame_arrive_stations.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW, padx=25, pady=5)

        self.frame_arrive_stations.rowconfigure(0, weight=1)
        self.frame_arrive_stations.columnconfigure(0, weight=1)
        self.frame_arrive_stations.columnconfigure(1, weight=0)

        self.scrollbar_y = ttk.Scrollbar(self.frame_arrive_stations, orient='vertical')
        self.scrollbar_y.grid(row=0, column=1, sticky=tk.NS)

        self.listbox_arrive_stations = tk.Listbox(self.frame_arrive_stations, yscrollcommand=self.scrollbar_y.set)
        self.listbox_arrive_stations.grid(row=0, column=0, sticky=tk.NSEW)
        self.scrollbar_y['command'] = self.listbox_arrive_stations.yview

        self.next_stations = dict()

        self.listbox_arrive_stations.bind('<<ListboxSelect>>', self.on_arrive_station_selected)

        self.button_add_station = ttk.Button(self.window, text="Ajouter", command=lambda: self.add_station_button_pressed())
        self.button_add_station.grid(row=4, column=0, sticky=tk.NSEW, padx=15, pady=15)

        self.button_close_window = ttk.Button(self.window, text="Fermer", command=lambda: self.on_close_window_pressed())
        self.button_close_window.grid(row=4, column=1, sticky=tk.NSEW, padx=15, pady=15)

