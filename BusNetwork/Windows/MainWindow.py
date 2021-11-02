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
from BusNetworkStations import BusNetworkStations
from Station import Station
from BusNetworkProcessing import BusNetworkProcessing

from Windows.AddStationWindow import AddStationWindow
from Windows.EditStationWindow import EditStationWindow

class MainWindow(tk.Tk):
    """description of class"""

    def import_json(self):
        print("Importer un fichier JSON")

    def export_json(self):
        print("Exporter un fichier JSON")

    def calculate_trip(self):
        print("Calculer le trajet le plus court et le plus rapide")
        
        try:
            self.listbox_trip_steps.delete(0, tk.END)
            start_station_id = self.bus_network_stations.get_station_id_by_name(self.combo_station_names_start.get())
            arrive_station_id = self.bus_network_stations.get_station_id_by_name(self.combo_station_names_arrive.get())

            self.trip = self.bus_network_processing.calculate_both_trips(start_station_id, arrive_station_id, self.bus_network_stations.get_all_stations())

            if self.trip.fastest_trip_travel_time == -1: 
                self.label_best_travel_time_tt["text"] = ""
                self.label_best_length_l["text"] = ""
                self.label_best_length_tt["text"] = ""
                self.label_best_travel_time_l["text"] = ""
                return

            self.label_best_travel_time_tt["text"] = self.trip.fastest_trip_travel_time
            self.label_best_length_l["text"] = self.trip.shortest_trip_length
            self.label_best_length_tt["text"] = self.trip.shortest_trip_travel_time
            self.label_best_travel_time_l["text"] = self.trip.fastest_trip_length
        except Exception as e:
            print("Problème dans le calcul du trajet")
            print(e)
        
    def add_station(self):
        print("Ajouter une station")
        add_station_window = AddStationWindow(self)

    def remove_station(self):
        print("Supprimer une station")

    def edit_station(self):
        print("Modifier une station")
        edit_station_window = EditStationWindow(self)

    def show_shortest_trip_steps(self):
        try:
            print("MOntrer le trjet le plus court")
            self.listbox_trip_steps.delete(0, tk.END)
            for step in self.trip.shortest_trip:
                print(self.bus_network_stations.get_all_stations()[step].nom)
                self.listbox_trip_steps.insert(self.listbox_trip_steps.size(), self.bus_network_stations.get_all_stations()[step].nom)
        except:
            print("Impossible de montrer le trajet")

    def show_fastest_trip_steps(self):
        try:
            print("Montrer le trajet le plus rapide")
            self.listbox_trip_steps.delete(0, tk.END)
            for step in self.trip.fastest_trip:
                print(self.bus_network_stations.get_all_stations()[step].nom)
                self.listbox_trip_steps.insert(self.listbox_trip_steps.size(), self.bus_network_stations.get_all_stations()[step].nom)
        except:
            print("Impossible de montrer le trajet")

    def __init__(self):
        self.bus_network_stations = BusNetworkStations()
        self.bus_network_processing = BusNetworkProcessing()



        # DEBUG ONLY
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
        
        self.bus_network_stations.set_stations(stations)

        for s in self.bus_network_stations.stations:
            print(s.to_string())

        # END OF DEBUG ONLY



        super().__init__()

        self.geometry("720x350")
        self.title("Projet Réseau de bus [Kévin DESIR] 2021")

        # configure style
        self.configure(background='#F0F0F0')

        # Top menu
        menubar = tk.Menu(self)
        menubar.add_command(label="Importer", command=self.import_json) 
        menubar.add_command(label="Exporter", command=self.export_json)
        menubar.add_command(label="Ajouter une station", command=self.add_station)
        menubar.add_command(label="Modifier une station", command=self.edit_station)
        
        # display the menu
        self.config(menu=menubar)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        label_start_station = ttk.Label(self, text="Station de départ")
        label_start_station.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        entry_username = ttk.Entry(self)
        self.combo_station_names_start = ttk.Combobox(self, state="readonly", values=self.bus_network_stations.get_all_station_names())
        self.combo_station_names_start.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        try:
            self.combo_station_names_start.current(0)
        except:
            print("Aucune station n'existe")

        label_arrive_station = ttk.Label(self, text="Station d'arrivée")
        label_arrive_station.grid(row=1, column=3, sticky=tk.E, padx=5, pady=5)

        self.combo_station_names_arrive = ttk.Combobox(self, state="readonly", values=self.bus_network_stations.get_all_station_names())
        self.combo_station_names_arrive.grid(row=1, column=4, sticky=tk.W, padx=5, pady=5)
        try:
            self.combo_station_names_arrive.current(0)
        except:
            print("Aucune station n'existe")

        button_calculate_trip = ttk.Button(self, text="Calculer trajet", command=lambda: self.calculate_trip())
        button_calculate_trip.grid(row=1, column=6, sticky=tk.NSEW, padx=5, pady=5)
        


        self.style = ttk.Style(self)
        self.style.configure("My.TFrame", background="white")
        frame_result = ttk.Frame(self, style="My.TFrame")
        frame_result.grid(row=0, column=6, sticky=tk.NSEW, padx=5, pady=5)

        # configure the frame on the right that displays the result (best travel time and best length)
        frame_result.rowconfigure(0, weight=1)
        frame_result.rowconfigure(1, weight=1)
        frame_result.rowconfigure(2, weight=1)
        frame_result.rowconfigure(3, weight=1)
        frame_result.rowconfigure(4, weight=1)
        frame_result.rowconfigure(5, weight=1)
        frame_result.rowconfigure(6, weight=1)
        frame_result.rowconfigure(7, weight=1)
        frame_result.rowconfigure(8, weight=1)
        frame_result.rowconfigure(9, weight=1)
        frame_result.rowconfigure(10, weight=1)
        frame_result.rowconfigure(11, weight=1)
        frame_result.rowconfigure(12, weight=1)
        frame_result.rowconfigure(13, weight=1)
        frame_result.rowconfigure(14, weight=1)
        frame_result.rowconfigure(15, weight=1)
        frame_result.rowconfigure(16, weight=1)
        frame_result.columnconfigure(0, weight=1)

        self.style_frame_result = ttk.Style(frame_result)
        self.style_frame_result.configure("Blue.TLabel", background="white", foreground="#1D00FF")
        self.style_frame_result.configure("Black.TLabel", background="white", foreground="black")
        self.style_frame_result.configure("Orange.TLabel", background="white", foreground="#FF8900")


        label_best_travel_time = ttk.Label(frame_result, text="Meilleur temps :", style="Blue.TLabel")
        label_best_travel_time.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        
        label_best_travel_time = ttk.Label(frame_result, text="Distance totale :", style="Black.TLabel")
        label_best_travel_time.grid(row=3, column=0, sticky=tk.SW, padx=15, pady=5)

        self.label_best_travel_time_l = ttk.Label(frame_result, style="Black.TLabel")
        self.label_best_travel_time_l.grid(row=4, column=0, sticky=tk.NW, padx=15, pady=5)

        label_best_travel_time = ttk.Label(frame_result, text="Temps total :", style="Black.TLabel")
        label_best_travel_time.grid(row=6, column=0, sticky=tk.SW, padx=15, pady=5)

        self.label_best_travel_time_tt = ttk.Label(frame_result, text="", style="Black.TLabel")
        self.label_best_travel_time_tt.grid(row=7, column=0, sticky=tk.NW, padx=15, pady=5)

        label_best_travel_time = ttk.Label(frame_result, text="Meilleur distance :", style="Orange.TLabel")
        label_best_travel_time.grid(row=9, column=0, sticky=tk.W, padx=5, pady=5)

        label_best_travel_time = ttk.Label(frame_result, text="Distance totale :", style="Black.TLabel")
        label_best_travel_time.grid(row=11, column=0, sticky=tk.SW, padx=15, pady=5)

        self.label_best_length_l = ttk.Label(frame_result, text="", style="Black.TLabel")
        self.label_best_length_l.grid(row=12, column=0, sticky=tk.NW, padx=15, pady=5)
        
        label_best_travel_time = ttk.Label(frame_result, text="Temps total :", style="Black.TLabel")
        label_best_travel_time.grid(row=14, column=0, sticky=tk.SW, padx=15, pady=5)

        self.label_best_length_tt = ttk.Label(frame_result, style="Black.TLabel")
        self.label_best_length_tt.grid(row=15, column=0, sticky=tk.NW, padx=15, pady=5)


        
        self.frame_show_trip = ttk.Frame(self, style="My.TFrame")
        self.frame_show_trip.grid(row=0, column=0, columnspan=6, sticky=tk.NSEW, padx=5, pady=5)
        self.frame_show_trip.rowconfigure(0, weight=1)
        self.frame_show_trip.rowconfigure(1, weight=1)
        self.frame_show_trip.columnconfigure(0, weight=0)
        self.frame_show_trip.columnconfigure(1, weight=1)

        self.button_shortest = ttk.Button(self.frame_show_trip, text="Afficher trajet le plus court", command=lambda: self.show_shortest_trip_steps())
        self.button_shortest.grid(row=1, column=0, sticky=tk.NSEW, padx=15, pady=15)

        self.button_fastest = ttk.Button(self.frame_show_trip, text="Afficher trajet le plus rapide", command=lambda: self.show_fastest_trip_steps())
        self.button_fastest.grid(row=0, column=0, sticky=tk.NSEW, padx=15, pady=15)
            
        self.frame_trip_steps = ttk.Frame(self.frame_show_trip)
        self.frame_trip_steps.grid(row=0, rowspan=2, column=1, sticky=tk.NSEW, padx=25,pady=25)

        self.frame_trip_steps.rowconfigure(0, weight=1)
        self.frame_trip_steps.columnconfigure(0, weight=1)
        self.frame_trip_steps.columnconfigure(1, weight=0)

        self.scrollbar_y = ttk.Scrollbar(self.frame_trip_steps, orient='vertical')
        self.scrollbar_y.grid(row=0, column=1, sticky=tk.NS)

        self.listbox_trip_steps = tk.Listbox(self.frame_trip_steps, yscrollcommand=self.scrollbar_y.set)
        self.listbox_trip_steps.grid(row=0, column=0, sticky=tk.NSEW)
        self.scrollbar_y['command'] = self.listbox_trip_steps.yview

#        label_test = ttk.Label(frame_show_trip, text="Meilleur temps :", style="Blue.TLabel")
#        label_test.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)


        # display the window
        self.mainloop()

