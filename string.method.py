imie = input("hej, jak masz na imie?\n")
nazwisko = input("A jak masz na nazwisko?\n")
telefon = input("Podaj prosze numer telefonu.\n")

print("********************")

print("zadanie nr 1")

print("Czy imię składa się tylko z liter?", imie.isalpha())
print("Czy nazwisko składa się tylko z liter?", nazwisko.isalpha())
print("Czy numer telefonu składa się z cyfr", telefon.isdigit())

print("*******************")

print("zadanie nr 2")

print(imie, nazwisko)
imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print(imie, nazwisko)

print("******************")

print("zadanie nr 3")

print(telefon)
telefon = telefon.replace(" ","").replace("-","")
print(telefon)

print("******************")

print("zadanie nr 4")
print("Imie kobiece:", imie.endswith("a"))

print("******************")

print("zadanie nr 5,6 i 7")

personal = imie + " " + nazwisko + " " + telefon
print(len(personal))

liczba_liter = len(personal) - 9 - personal.count(" ")
print(liczba_liter)
print(len(imie + nazwisko)) #sprawdzenie
