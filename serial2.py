serials = {"hurra" : 7.8,
           "blabla" : 8.2,
           "incognito" : 5.5,
           "wiedzmin" : 9.2 }
print(list(serials.keys()))
print("**************************************")
name = input("Jaki serial chcesz obejrzeć?\n")
print("Serial {} otrzymal ocene {}" .format(name, serials[name]))
print("***************************************")
nowy = input("Jaki serial chcesz dodac do listy?\n")
rate = input("Jaką ocenę otrzymał" + nowy + "?")
serials[nowy] = float(rate)
print("*****************************************")
print(list(serials.keys()))
