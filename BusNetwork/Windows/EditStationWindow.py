import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

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
from Windows.EditNextStationWindow import EditNextStationWindow

class EditStationWindow(object):
    """description of class"""

    def update_station_button_pressed(self):
        try:
            s_id = self.station_editing.id

            n_stations = dict()
            n_keys = self.next_stations.keys()

            for k in n_keys:
                n_id = self.root.bus_network_stations.get_station_id_by_name(k)
                n_distance = self.next_stations[k][0]
                n_travel_time = self.next_stations[k][0]

                n_stations[n_id] = [n_distance, n_travel_time]

            self.station_editing.next_stations = self.next_stations
#            s = Station(s_id, self.entry_station_name.get(), 0, 0, self.next_stations)

            
        except Exception as e:
            print(e)

    def delete_station_button_pressed(self):
        print("Supprimer dernière station")
        
        confirmation = askyesno(title="Attention", message="Attention : Vous-êtes vous assuré qu'aucune station n'a pour direction suivante la dernière station qui est sur le point d'être supprimée définitivement ?")
        if not confirmation: return;

        self.root.bus_network_stations.delete_last_station()
        self.root.set_mainwindow_combobox()
        self.window.destroy()

    def on_arrive_station_selected(self, event):
        try :
            selection = event.widget.curselection()
            index = selection[0]
            data = event.widget.get(index)
        
            print(str(index) + " -> " + data)    

            edit_next_station_window = EditNextStationWindow(self, self.root.bus_network_stations.get_station_id_by_name(data), data)
        except:
            print("Problème avec la station sélectionnée dans la liste")

    def add_arrive_station_pressed(self):
        add_next_station_window = AddNextStationWindow(self)

    def on_close_window_pressed(self):
        print("close window")
        self.window.destroy()

    def on_combobox_item_changed(self):
        print(self.combo_station_name.get())

        self.station_editing = self.root.bus_network_stations.get_station_by_name(self.combo_station_name.get())
        print(self.station_editing.to_string())
        
        self.label_station_id['text'] = self.station_editing.id
        self.next_stations = self.station_editing.next_stations
        self.listbox_arrive_stations.delete(0,tk.END)
        for s in self.next_stations:
            try:
                self.listbox_arrive_stations.insert(self.listbox_arrive_stations.size(), self.root.bus_network_stations.get_all_stations()[s].nom)
            except:
                print("Impossible de récupérer la station suivante")

    def __init__(self, root):
        self.root = root

        self.window = tk.Toplevel(root)

        self.window.title("Modification de station")
    
        self.window.grab_set() # rendre la fenêtre modale

        self.window.geometry("330x350")

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        self.window.rowconfigure(3, weight=1)
        self.window.rowconfigure(4, weight=0)

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        
        self.label_station_name = ttk.Label(self.window, text="Nom de la Station")
        self.label_station_name.grid(row=0, column=0, sticky=tk.NS, padx=5, pady=5)

        self.combo_station_name = ttk.Combobox(self.window, state="readonly", values=self.root.bus_network_stations.get_all_station_names())
        self.combo_station_name.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.combo_station_name.bind("<<ComboboxSelected>>", lambda _: self.on_combobox_item_changed())

        self.label_station_id = ttk.Label(self.window, text="ID de station")
        self.label_station_id.grid(row=1, column=0, sticky=tk.NS, padx=5, pady=5)

        #self.entry_station_id = ttk.Entry(self.window)
        #self.entry_station_id.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.label_station_id = ttk.Label(self.window)
        self.label_station_id.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

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

        #self.button_update_station = ttk.Button(self.window, text="Appliquer", command=lambda: self.update_station_button_pressed())
        #self.button_update_station.grid(row=4, column=0, sticky=tk.NSEW, padx=15, pady=15)
        
        #self.style_delete_button = ttk.Style(self.window)
        #self.style_delete_button.configure("Red.TButton", background="red", foreground="red")
        #self.button_delete_station = ttk.Button(self.window, text="Supprimer dernière station", style="Red.TButton", command=lambda: self.delete_station_button_pressed())
        self.button_delete_station = tk.Button(self.window, text="Supprimer dernière station", bg="red", fg="white", command=lambda: self.delete_station_button_pressed())
        self.button_delete_station.grid(row=4, column=0, sticky=tk.NSEW, padx=15, pady=15)

        self.button_close_window = ttk.Button(self.window, text="Fermer", command=lambda: self.on_close_window_pressed())
        self.button_close_window.grid(row=4, column=1, sticky=tk.NSEW, padx=15, pady=15)

