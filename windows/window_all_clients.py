from tkinter import *
from popups import show_error_popup
import tkintermapview
from windows.window01 import open_window01


def open_window_all_clients():
    users: list = []

    class User:
        def __init__(self, client_name, client_surname, location, marinas_name):
            self.client_name = client_name
            self.client_surname = client_surname
            self.location = location
            self.marinas_name = marinas_name
            self.coordinates = self.get_coordinates()
            self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1])

        def get_coordinates(self) -> list:
            import requests
            from bs4 import BeautifulSoup
            address_url: str = f"https://pl.wikipedia.org/wiki/{self.location}"
            response = requests.get(address_url).text
            response_html = BeautifulSoup(response, "html.parser")
            longitude: float = float(response_html.select(".longitude")[1].text.replace(",", "."))
            latitude: float = float(response_html.select(".latitude")[1].text.replace(",", "."))
            return [latitude, longitude]

    def add_users():
        client_name = entry_client_name.get()
        client_surname = entry_client_surname.get()
        marinas_name = entry_marinas_name.get()
        location = entry_location.get()
        if not (client_name and client_surname and marinas_name and location):
            show_error_popup()
            return
        try:
            tmp_user = User(client_name=client_name, client_surname=client_surname, location=location,
                            marinas_name=marinas_name)
        except Exception as e:
            show_error_popup()
            return
        users.append(tmp_user)
        print(users)
        entry_client_name.delete(0, END)
        entry_client_surname.delete(0, END)
        entry_marinas_name.delete(0, END)
        entry_location.delete(0, END)
        entry_client_name.focus()
        show_users()

    def show_users():
        listbox_lista_obiektow.delete(0, END)
        for idx, user in enumerate(users):
            listbox_lista_obiektow.insert(idx,
                                          f"{idx + 1}. {user.client_name} {user.client_surname} {user.location} {user.marinas_name} ")

    def delete_user():
        idx = listbox_lista_obiektow.index(ACTIVE)
        users[idx].marker.delete()
        users.pop(idx)
        show_users()

    def user_details():
        idx = listbox_lista_obiektow.index(ACTIVE)
        label_name_szczegoły_obiektu_wartosc.configure(text=users[idx].client_name)
        label_surname_szczegoły_obiektow.configure(text=users[idx].client_surname)
        label_location_szczegoły_obiektu.configure(text=users[idx].location)
        label_posts_szczegoły_obiektow.configure(text=users[idx].marinas_name)
        map_widget.set_position(users[idx].coordinates[0], users[idx].coordinates[1])
        map_widget.set_zoom(17)
        open_window01()

    def edit_user():
        idx = listbox_lista_obiektow.index(ACTIVE)
        entry_client_name.insert(0, users[idx].client_name)
        entry_client_surname.insert(0, users[idx].client_surname)
        entry_location.insert(0, users[idx].location)
        entry_marinas_name.insert(0, users[idx].marinas_name)
        Button_dodaj_obiekt.configure(text="Zapisz", command=lambda: update_users(idx))

    def update_users(idx):
        client_name = entry_client_name.get()
        client_surname = entry_client_surname.get()
        location = entry_location.get()
        marinas_name = entry_marinas_name.get()
        if not (client_name and client_surname and marinas_name and location):
            show_error_popup()
            return
        try:
            import requests
            from bs4 import BeautifulSoup
            address_url = f"https://pl.wikipedia.org/wiki/{location}"
            response = requests.get(address_url).text
            response_html = BeautifulSoup(response, "html.parser")
            longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
            latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        except Exception:
            show_error_popup()
            return
        try:
            users[idx].marker.delete()
        except:
            pass
        users[idx].client_name = client_name
        users[idx].client_surname = client_surname
        users[idx].location = location
        users[idx].marinas_name = marinas_name
        users[idx].coordinates = [latitude, longitude]
        users[idx].marker = map_widget.set_marker(latitude, longitude)
        Button_dodaj_obiekt.configure(text="Dodaj",bg="#FFEFDE",font=("Lucida Sans Unicode", 10), command=add_users)
        entry_client_name.delete(0, END)
        entry_client_surname.delete(0, END)
        entry_marinas_name.delete(0, END)
        entry_location.delete(0, END)
        show_users()

    root = Toplevel()
    root.title("Wszyscy klienci")
    root.geometry("1024x768")

    Ramka_lista_obiektów = Frame(root)
    Ramka_formularz = Frame(root)
    Ramka_szczeguly_obiektow = Frame(root)
    Ramka_mapa = Frame(root)

    Ramka_lista_obiektów.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    Ramka_formularz.grid(row=0, column=1, padx=10, pady=10, sticky=W)
    Ramka_szczeguly_obiektow.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=W)
    Ramka_mapa.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    label_lista_obiektow = Label(Ramka_lista_obiektów, text="Lista wszystkich klientów: ")
    label_lista_obiektow.grid(row=0, column=0, columnspan=4)
    listbox_lista_obiektow = Listbox(Ramka_lista_obiektów, width=35, height=10)
    listbox_lista_obiektow.grid(row=1, column=0, columnspan=4)
    button_pokaz_szczegoly = Button(Ramka_lista_obiektów, text="Pokaż Szczegóły: ",bg="#FFEFDE",font=("Lucida Sans Unicode", 10), command=user_details)
    button_pokaz_szczegoly.grid(row=2, column=0)
    button_edytuj_obiekt = Button(Ramka_lista_obiektów, text="Edytuj dane: ",bg="#FFEFDE",font=("Lucida Sans Unicode", 10), command=edit_user)
    button_edytuj_obiekt.grid(row=2, column=1)
    button_usun_obiekt = Button(Ramka_lista_obiektów, text="Usuń obiekt: ",bg="#FFEFDE",font=("Lucida Sans Unicode", 10), command=delete_user)
    button_usun_obiekt.grid(row=2, column=2)

    label_formularz = Label(Ramka_formularz, text="Formularz zgłoszeniowy: ")
    label_formularz.grid(row=0, column=0, columnspan=2)
    label_name = Label(Ramka_formularz, text=" Imię klienta: ")
    label_name.grid(row=1, column=0, sticky=W)
    label_surname = Label(Ramka_formularz, text=" Nazwisko klienta: ")
    label_surname.grid(row=2, column=0, sticky=W)
    label_posts = Label(Ramka_formularz, text=" Nazwa mariny: ")
    label_posts.grid(row=3, column=0, sticky=W)
    label_location = Label(Ramka_formularz, text=" Miejscowość: ")
    label_location.grid(row=4, column=0, sticky=W)

    entry_client_name = Entry(Ramka_formularz, width=30)
    entry_client_name.grid(row=1, column=1, padx=5, pady=3)
    entry_client_surname = Entry(Ramka_formularz, width=30)
    entry_client_surname.grid(row=2, column=1, padx=5, pady=3)
    entry_marinas_name = Entry(Ramka_formularz, width=30)
    entry_marinas_name.grid(row=3, column=1, padx=5, pady=3)
    entry_location = Entry(Ramka_formularz, width=30)
    entry_location.grid(row=4, column=1, padx=5, pady=3)

    Button_dodaj_obiekt = Button(Ramka_formularz, text="Dodaj",bg="#FFEFDE",font=("Lucida Sans Unicode", 10), command=add_users)
    Button_dodaj_obiekt.grid(row=5, column=1, columnspan=2)

    label_szczegoły_obiektu = Label(Ramka_szczeguly_obiektow, text="Szczegóły klienta: ")
    label_szczegoły_obiektu.grid(row=0, column=0)

    label_name_szczegoły_obiektu = Label(Ramka_szczeguly_obiektow, text="Imię klienta:")
    label_name_szczegoły_obiektu.grid(row=1, column=0)
    label_name_szczegoły_obiektu_wartosc = Label(Ramka_szczeguly_obiektow, text="....")
    label_name_szczegoły_obiektu_wartosc.grid(row=1, column=1)

    label_surname_szczegoły_obiektow = Label(Ramka_szczeguly_obiektow, text="Nazwisko klienta:")
    label_surname_szczegoły_obiektow.grid(row=1, column=3)
    label_surname_szczegoły_obiektow = Label(Ramka_szczeguly_obiektow, text="....")
    label_surname_szczegoły_obiektow.grid(row=1, column=4)

    label_posts_szczegoły_obiektow = Label(Ramka_szczeguly_obiektow, text=" Członkostwo w marinie/porcie:")
    label_posts_szczegoły_obiektow.grid(row=1, column=6)
    label_posts_szczegoły_obiektow = Label(Ramka_szczeguly_obiektow, text="....")
    label_posts_szczegoły_obiektow.grid(row=1, column=7)

    label_location_szczegoły_obiektu = Label(Ramka_szczeguly_obiektow, text="Miejscowość:")
    label_location_szczegoły_obiektu.grid(row=1, column=9)
    label_location_szczegoły_obiektu = Label(Ramka_szczeguly_obiektow, text="....")
    label_location_szczegoły_obiektu.grid(row=1, column=10)

    map_widget = tkintermapview.TkinterMapView(Ramka_mapa, width=1000, height=350)
    map_widget.set_position(52.23, 21)
    map_widget.set_zoom(6.5)
    map_widget.grid(row=0, column=0, columnspan=8)

    root.mainloop()