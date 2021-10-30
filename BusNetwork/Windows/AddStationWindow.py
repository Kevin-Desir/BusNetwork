import tkinter as tk
from tkinter import ttk

class AddStationWindow(object):
    def __init__(self, root):
        self.window = tk.Toplevel(root)

        self.window.title("Détection des contours")
    
        self.window.grab_set() # rendre la fenêtre modale

        self.window.geometry("300x200")

        self.intensitelabel = ttk.Label(self.window, text="Intensité du filtre (1, 2 ou 3) : ")
        self.intensitelabel.grid(row = 0, column = 0)

        self.intensiteentry = ttk.Entry(self.window)
        self.intensiteentry.grid(row = 0, column = 1)

        self.okbutton = ttk.Button(self.window, text="Détecter des contours !")
        self.okbutton.grid(row = 2, column = 1)