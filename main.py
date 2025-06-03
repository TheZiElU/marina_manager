from tkinter import *
from popups import show_error_popup
import tkintermapview


users:list = []

class User:
    def __init__(self, marina_name, owner_surname, location, workers):
        self.marina_name =  marina_name
        self.owner_surname = owner_surname
        self.location = location
        self.workers= workers
        self.coordinates= self.get_coordinates()
        self.marker= map_widget.set_marker(self.coordinates[0], self.coordinates[1])


    def get_coordinates(self,) -> list:
        import requests
        from bs4 import BeautifulSoup
        address_url: str = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(address_url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude: float = float(response_html.select(".longitude")[1].text.replace(",", "."))
        #    print(longitude)
        latitude: float = float(response_html.select(".latitude")[1].text.replace(",", "."))
        #    print(latitude)
        return [latitude, longitude]



def add_users():
    nazwa_portu = entry_marina_name.get()
    nazwisko = entry_owner_surname.get()
    pracownicy= entry_workers.get()
    miejscowosc = entry_location.get()
    if not (nazwa_portu and nazwisko and pracownicy and miejscowosc):
        show_error_popup()
        return
    try:
        tmp_user = (User(marina_name=nazwa_portu, owner_surname=nazwisko, location=miejscowosc, workers=pracownicy))
    except Exception as e:
        show_error_popup()
        return
    users.append(tmp_user)
    print(users)
    entry_marina_name.delete(0, END)
    entry_owner_surname.delete(0, END)
    entry_workers.delete(0, END)
    entry_location.delete(0, END)
    entry_marina_name.focus()
    show_users()


def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f"{idx+1}. {user.marina_name} {user.owner_surname} {user.location} {user.workers} ")

def delete_user():
    idx=listbox_lista_obiektow.index(ACTIVE)
    users[idx].marker.delete()
    users.pop(idx)
    show_users()

def user_details():
    idx=listbox_lista_obiektow.index(ACTIVE)
    label_name_szczegoły_obiektu_wartosc.configure(text=users[idx].marina_name)
    label_surname_szczegoły_obiektow.configure(text=users[idx].owner_surname)
    label_location_szczegoły_obiektu.configure(text=users[idx].location)
    label_posts_szczegoły_obiektow.configure(text=users[idx].workers)
    map_widget.set_position(users[idx].coordinates[0],users[idx].coordinates[1])
    map_widget.set_zoom(17)

def edit_user():
    idx=listbox_lista_obiektow.index(ACTIVE)
    entry_marina_name.insert(0, users[idx].marina_name)
    entry_owner_surname.insert(0, users[idx].owner_surname)
    entry_location.insert(0, users[idx].location)
    entry_workers.insert(0, users[idx].workers)

    Button_dodaj_obiekt.configure(text="Zapisz", command=lambda: update_users(idx))


def update_users(idx):
    nazwa_portu = entry_marina_name.get()
    nazwisko = entry_owner_surname.get()
    miejscowosc = entry_location.get()
    pracownicy = entry_workers.get()

    if not (nazwa_portu and nazwisko and pracownicy and miejscowosc):
        show_error_popup()
        return

    try:
        # Pobierz nowe współrzędne (sprawdź poprawność danych)
        import requests
        from bs4 import BeautifulSoup
        address_url = f"https://pl.wikipedia.org/wiki/{miejscowosc}"
        response = requests.get(address_url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    except Exception:
        show_error_popup()
        return

    # Usuń stary marker z mapy
    try:
        users[idx].marker.delete()
    except:
        pass

    # Zaktualizuj dane użytkownika
    users[idx].marina_name = nazwa_portu
    users[idx].owner_surname = nazwisko
    users[idx].location = miejscowosc
    users[idx].workers = pracownicy
    users[idx].coordinates = [latitude, longitude]
    users[idx].marker = map_widget.set_marker(latitude, longitude)

    # Wyczyść pola formularza i przywróć przycisk
    Button_dodaj_obiekt.configure(text="Dodaj", command=add_users)
    entry_marina_name.delete(0, END)
    entry_owner_surname.delete(0, END)
    entry_workers.delete(0, END)
    entry_location.delete(0, END)
    show_users()



root = Tk()
root.title("MapBook_IZ")
root.geometry("1920x1080")

# RAMKI
Ramka_lista_obiektów=Frame(root)
Ramka_formularz=Frame(root)
Ramka_szczeguly_obiektow=Frame(root)
Ramka_mapa=Frame(root)


Ramka_lista_obiektów.grid(row=0, column=0, padx=10, pady=10, sticky=W)
Ramka_formularz.grid(row=0, column=1, padx=10, pady=10, sticky=W)
Ramka_szczeguly_obiektow.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=W)
Ramka_mapa.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#Pady służą do tego aby był odstę liczpny w pixelach
#a sticky do "przyklejania obiektów go górnej czy prawej stony ekranu

#RAMKA LISTA OBIEKTÓW
label_lista_obiektow= Label(Ramka_lista_obiektów,text="Lista obiektów: ")
label_lista_obiektow.grid(row=0, column=0, columnspan=4)
listbox_lista_obiektow=Listbox(Ramka_lista_obiektów, width=35, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=4)
button_pokaz_szczegoly= Button(Ramka_lista_obiektów, text="Pokaż Szczegóły: ", command=user_details)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt= Button(Ramka_lista_obiektów, text="Edytuj dane: ", command=edit_user)
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt= Button(Ramka_lista_obiektów, text="Usuń obiekt: ", command=delete_user)
button_usun_obiekt.grid(row=2, column=2)



#RAMKA FORMULARZ
label_formularz= Label(Ramka_formularz,text="Formularz zgłoszeniowy: ")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name= Label(Ramka_formularz,text="Nazwa Mariny/Portu: ")
label_name.grid(row=1, column=0, sticky=W)
label_surname= Label(Ramka_formularz,text="Nazwisko Właściciela: ")
label_surname.grid(row=2, column=0,sticky=W)
label_posts= Label(Ramka_formularz,text="Liczba pracowników: ")
label_posts.grid(row=3, column=0, sticky=W)
label_location= Label(Ramka_formularz,text="Miejscowość: ")
label_location.grid(row=4, column=0, sticky=W)


#pad X/Y ma tu zwiększyć odstęp i przejrzystość
entry_marina_name = Entry(Ramka_formularz, width=30)
entry_marina_name.grid(row=1, column=1, padx=5, pady=3)
entry_owner_surname = Entry(Ramka_formularz, width=30)
entry_owner_surname.grid(row=2, column=1, padx=5, pady=3)
entry_workers = Entry(Ramka_formularz, width=30)
entry_workers.grid(row=3, column=1, padx=5, pady=3)
entry_location = Entry(Ramka_formularz, width=30)
entry_location.grid(row=4, column=1, padx=5, pady=3)


Button_dodaj_obiekt= Button(Ramka_formularz,text="Dodaj" ,command=add_users)
Button_dodaj_obiekt.grid(row=5, column=1,columnspan=2)


#RAMKA SZCZEGÓŁY OBIEKTÓW
label_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Szczegóły użytkownika: ")
label_szczegoły_obiektu.grid(row=0, column=0)

label_name_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Nazwa Mariny/Portu:")
label_name_szczegoły_obiektu.grid(row=1, column=0)

label_name_szczegoły_obiektu_wartosc= Label(Ramka_szczeguly_obiektow, text="....")
label_name_szczegoły_obiektu_wartosc.grid(row=1, column=1)

label_surname_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="Nazwisko właściciela:")
label_surname_szczegoły_obiektow.grid(row=1, column=3)

label_surname_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="....")
label_surname_szczegoły_obiektow.grid(row=1, column=4)

label_posts_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text=" Liczba pracowników:")
label_posts_szczegoły_obiektow.grid(row=1, column=6)

label_posts_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="....")
label_posts_szczegoły_obiektow.grid(row=1, column=7)

label_location_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Miejscowość:")
label_location_szczegoły_obiektu.grid(row=1, column=9)

label_location_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="....")
label_location_szczegoły_obiektu.grid(row=1, column=10)


# #RAMKA MAPA
map_widget= tkintermapview.TkinterMapView(Ramka_mapa, width=1700, height=450)
map_widget.set_position(52.23, 21)
map_widget.set_zoom(6.5)
map_widget.grid(row=0, column=0, columnspan=8)




root.mainloop()