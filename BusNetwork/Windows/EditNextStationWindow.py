import tkinter as tk
from tkinter import ttk

class EditNextStationWindow(object):
    """description of class"""

    def update_next_station_pressed(self):
        print("Mettre à jour la prochaine station")
        try:
            self.root.next_stations_names[self.station_editing_name] = [int(self.entry_distance.get()), int(self.entry_travel_time.get())]
        except:
            self.root.next_stations[self.station_editing_id] = [int(self.entry_distance.get()), int(self.entry_travel_time.get())]
            
    def close_window_pressed(self):
        self.window.destroy()

    def delete_next_station_pressed(self):
        print("Supprimer la station")

    def __init__(self, root, station_editing_id, station_editing_name):
        self.root = root
        self.station_editing_id = station_editing_id
        self.station_editing_name = station_editing_name

        self.window = tk.Toplevel(self.root.root)

        self.window.title("Modification de station suivante")

        self.window.grab_set() # rendre la fenêtre modale

        self.window.geometry("320x250")

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=0)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)

        self.label_station_editing = ttk.Label(self.window, text=self.station_editing_name)
        self.label_station_editing.grid(column=0, row=0, columnspan=3, padx=15, pady=25, sticky=tk.NSEW)
        
        self.label_distance = ttk.Label(self.window, text="Distance")
        self.label_distance.grid(row=1, column=0, sticky=tk.SE, padx=5, pady=5)

        self.entry_distance = ttk.Entry(self.window)
        self.entry_distance.grid(row=1, column=1, sticky=tk.S, padx=5, pady=5)
        try:
            self.entry_distance.insert(0, self.root.next_stations_names[station_editing_name][0])
        except Exception as e:
            self.entry_distance.insert(0, self.root.next_stations[station_editing_id][0])
            print(e)

        self.label_distance_meters = ttk.Label(self.window, text="mètres")
        self.label_distance_meters.grid(row=1, column=2, sticky=tk.SW, padx=5, pady=5)

        self.label_travel_time = ttk.Label(self.window, text="Durée trajet")
        self.label_travel_time.grid(row=2, column=0, sticky=tk.NE, padx=5, pady=5)

        self.entry_travel_time = ttk.Entry(self.window)
        self.entry_travel_time.grid(row=2, column=1, sticky=tk.N, padx=5, pady=5)
        try:
            self.entry_travel_time.insert(0, self.root.next_stations_names[station_editing_name][1])
        except:
            self.entry_travel_time.insert(0, self.root.next_stations[station_editing_id][1])

        self.label_travel_time_minutes = ttk.Label(self.window, text="minutes")
        self.label_travel_time_minutes.grid(row=2, column=2, sticky=tk.NW, padx=5, pady=5)

        self.button_add = ttk.Button(self.window, text="Appliquer", command=lambda: self.update_next_station_pressed())
        self.button_add.grid(row=3, column=0, columnspan=1, sticky=tk.E, padx=15, pady=15)

        self.button_delete = ttk.Button(self.window, text="Supprimer", command=lambda: self.delete_next_station_pressed())
        self.button_delete.grid(row=3, column=1, sticky=tk.NS, padx=15, pady=15)

        self.button_close = ttk.Button(self.window, text="Fermer", command=lambda: self.close_window_pressed())
        self.button_close.grid(row=3, column=2, columnspan=1, sticky=tk.W, padx=15, pady=15)

