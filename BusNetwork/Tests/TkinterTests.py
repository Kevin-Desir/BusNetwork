import tkinter as tk
from tkinter import ttk


def login(name) :
    print("You have logged in", name)

root = tk.Tk()

root.geometry('720x500')
root.title("Projet Réseau de bus [Kévin DESIR] 2021")

label_username = ttk.Label(root, text='Username: ')
#label_username.pack()
label_username.grid(row=0, column=0)

entry_username = ttk.Entry(root)
entry_username.grid(row=0, column=1)

label_password = ttk.Label(root, text='Password: ')
label_password.grid(row = 1, column = 0)

entry_password = ttk.Entry(root)
entry_password.grid(row=1, column = 1)

#button_login = ttk.Button(root, text='Log in', command=lambda: login("Kevin"))
button_login = ttk.Button(root, text='Log in', command=lambda: login(entry_username.get()))
button_login.grid(row = 2, column = 0)

root.mainloop()