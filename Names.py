
#Utwórz zbiór imion męskich i żeńskich.Poproś użytkownika o podanie imienia. Sprawdź czy imię jest męskie czy żeńskie i wyświetl na ten temat informację. Jeżeli imienia nie ma na liście wyświetl komunikat „Nie znamy tego imienia.” Następnie użytkownik poda informację czy imię jest męskie czy żeńskie. Dodaj imię do listy.

lista_damskie = { 1: "Paula",
                  2: "Ola",
                  3: "Kinga",
                  4: "Marta" }
lista_meskie = { 1: "Adam",
                 2:"Tomek",
                 3:"Bartek",
                 4:"Andrzej" }

imie = input("Podaj dowolne imie\n")

if imie in list(lista_damskie.values()):
    print("Jest to imie damskie")
elif imie in list(lista_meskie.values()):
    print("Jest to imie meskie")
else:
    print("Nie znamy takiego imienia")
    gender = input("czy to jest imie meskie czy damskie?")
    if gender == "damskie":   #pamietaj o znaku == jako rownosci
        lista_damskie[5] = imie
    elif gender == "meskie":
        lista_meskie[5] = imie

print(list(lista_damskie.values()))
print(list(lista_meskie.values()))
