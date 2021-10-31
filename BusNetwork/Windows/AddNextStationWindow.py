import tkinter as tk
from tkinter import ttk

class AddNextStationWindow(object):
    """description of class"""

    def add_next_station_pressed(self):
        try:
            #print(self.combo_station_names.current(), self.combo_station_names.get())
            #print(self.entry_distance.get())
            #print(self.entry_travel_time.get())

            n_name = self.combo_station_names.get()
            n_id = self.root.root.bus_network_stations.get_station_by_name(self.combo_station_names.get())
            n_distance = int(self.entry_distance.get())
            n_travel_time = int(self.entry_travel_time.get())

            if n_name in self.root.next_stations:
                print("Cette destination existe déjà")
            else:
                self.root.next_stations[n_name] = [n_distance, n_travel_time]
                self.root.listbox_arrive_stations.insert(self.root.listbox_arrive_stations.size(), self.combo_station_names.get())

                print(self.root.next_stations)


        except Exception as e:
            print("Fromat des nombres invalide")
            print(e)
        

    def close_window_pressed(self):
        print("Fermer la fenêtre d'ajout de station suivante.")
        self.window.destroy()

    def __init__(self, root):

        self.root = root

        self.window = tk.Toplevel(self.root.root)

        self.window.title("Ajout de prochaines stations")
    
        self.window.grab_set() # rendre la fenêtre modale

        self.window.geometry("320x250")

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=0)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)

        print(self.root.root.bus_network_stations.get_all_station_names())

        self.combo_station_names = ttk.Combobox(self.window, values=self.root.root.bus_network_stations.get_all_station_names())
        self.combo_station_names.grid(column=0, row=0, columnspan=3, padx=15, pady=25, sticky=tk.EW)
        self.combo_station_names.current(0)

        self.label_distance = ttk.Label(self.window, text="Distance")
        self.label_distance.grid(row=1, column=0, sticky=tk.SE, padx=5, pady=5)

        self.entry_distance = ttk.Entry(self.window)
        self.entry_distance.grid(row=1, column=1, sticky=tk.S, padx=5, pady=5)

        self.label_distance_meters = ttk.Label(self.window, text="mètres")
        self.label_distance_meters.grid(row=1, column=2, sticky=tk.SW, padx=5, pady=5)

        self.label_travel_time = ttk.Label(self.window, text="Durée trajet")
        self.label_travel_time.grid(row=2, column=0, sticky=tk.NE, padx=5, pady=5)

        self.entry_travel_time = ttk.Entry(self.window)
        self.entry_travel_time.grid(row=2, column=1, sticky=tk.N, padx=5, pady=5)

        self.label_travel_time_minutes = ttk.Label(self.window, text="minutes")
        self.label_travel_time_minutes.grid(row=2, column=2, sticky=tk.NW, padx=5, pady=5)

        self.button_add = ttk.Button(self.window, text="Ajouter", command=lambda: self.add_next_station_pressed())
        self.button_add.grid(row=3, column=0, columnspan=1, sticky=tk.E, padx=25, pady=15)

        self.button_close = ttk.Button(self.window, text="Fermer", command=lambda: self.close_window_pressed())
        self.button_close.grid(row=3, column=2, columnspan=1, sticky=tk.W, padx=25, pady=15)





