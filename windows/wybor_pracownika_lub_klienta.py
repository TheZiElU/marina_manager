from tkinter import *
from windows.window_active_clients import open_window_active_clients
from windows.window01 import open_window01

def open_wybor_pracownika_lub_klienta():
    root = Tk()
    root.title("Wybór opcji")
    root.geometry("300x200")
    root.config(bg="#FFFFFF")

    button_wybierz_pracownika= Button(root, text="Wybierz Pracownika",bg="#DC143C",font=("Impact", 20), command=open_window01)
    button_wybierz_pracownika.grid(row=1, column=1)
    button_wybierz_klienta= Button(root, text="Wybierz Klienta" ,bg="#FFD700", font=("Impact", 10), command= open_window_active_clients)
    button_wybierz_klienta.grid(row=2, column=1)

    root.mainloop()
