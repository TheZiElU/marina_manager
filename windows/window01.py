from tkinter import *
import tkintermapview
#Ramki i inne

root = Tk()
root.title("Szczegóły portu")
root.geometry("1024x768")
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
label_lista_obiektow= Label(Ramka_lista_obiektów,text="Lista pracowników: ")
label_lista_obiektow.grid(row=0, column=0, columnspan=4)
listbox_lista_obiektow=Listbox(Ramka_lista_obiektów, width=35, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=4)
button_pokaz_szczegoly= Button(Ramka_lista_obiektów, text="Pokaż Szczegóły: ",) #command=user_details)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt= Button(Ramka_lista_obiektów, text="Edytuj dane: ",) #command=edit_user)
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt= Button(Ramka_lista_obiektów, text="Usuń obiekt: ",) #command=delete_user)
button_usun_obiekt.grid(row=2, column=2)



#RAMKA FORMULARZ
label_formularz= Label(Ramka_formularz,text="Dane pracowników: ")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name= Label(Ramka_formularz,text="Imię pracownika: ")
label_name.grid(row=1, column=0, sticky=W)
label_surname= Label(Ramka_formularz,text="Nazwisko pracownika: ")
label_surname.grid(row=2, column=0,sticky=W)
label_posts= Label(Ramka_formularz,text="Stanowisko: ")
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


Button_dodaj_obiekt= Button(Ramka_formularz,text="Dodaj" ,)#command=add_users)
Button_dodaj_obiekt.grid(row=5, column=1,columnspan=2)


#RAMKA SZCZEGÓŁY OBIEKTÓW
label_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Szczegóły pracownika: ")
label_szczegoły_obiektu.grid(row=0, column=0)

label_name_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Imię pracownika: ")
label_name_szczegoły_obiektu.grid(row=1, column=0)

label_name_szczegoły_obiektu_wartosc= Label(Ramka_szczeguly_obiektow, text="....")
label_name_szczegoły_obiektu_wartosc.grid(row=1, column=1)

label_surname_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="Nazwisko pracownika: ")
label_surname_szczegoły_obiektow.grid(row=1, column=3)

label_surname_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="....")
label_surname_szczegoły_obiektow.grid(row=1, column=4)

label_posts_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="Stanowisko: ")
label_posts_szczegoły_obiektow.grid(row=1, column=6)

label_posts_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="....")
label_posts_szczegoły_obiektow.grid(row=1, column=7)

label_location_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Miejscowość: ")
label_location_szczegoły_obiektu.grid(row=1, column=9)

label_location_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="....")
label_location_szczegoły_obiektu.grid(row=1, column=10)


# #RAMKA MAPA
map_widget= tkintermapview.TkinterMapView(Ramka_mapa, width=1024, height=400)
map_widget.set_position(52.23, 21)
map_widget.set_zoom(6.5)
map_widget.grid(row=0, column=0, columnspan=8)




root.mainloop()