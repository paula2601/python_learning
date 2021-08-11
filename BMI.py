# -*- coding: utf-8 -*-
imie = input("Hej, jak masz na imie?\n") 

waga = input( "podaj mi prosze swoja wage\n")

waga = int(waga)
wzrost = input("a teraz poprosze o wzrost w m\n")
wzrost = float(wzrost)
BMI = waga / (wzrost**2)
print("Twoje BMI wynosi", BMI)

wz = wzrost * 100

wiek = input("Ile masz lat?\n")
wiek = int(wiek) 
S = -161

z = 10*waga + 6.25 * wz - 5*wiek +S
aktive = input("jak aktywnie zyjesz? Jeśli masz aktywny tryb życia wybierz 1.4\n")
aktive = float(aktive)

zz = aktive * z

print('Twoje zapotrzebowanei wynosi:', zz, "kcal")
