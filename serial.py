

serial = {
    'hehe' : 8.2,
    "haha" : 7.3}
print(list(serial.keys()))
print("*****************************")
nazwa = input("Jaki serial chcesz obejrzec?\n")
print("serial %s otrzymal ocene %.1f" %(nazwa, serial[nazwa]))
new = input("Jaki serial chcesz dodac do bazy?\n")
rating = input("Jaką ocenę otrzymał ten serial?\n")
serial[new] = float(rating)
print("*****************************")
print(list(serial.keys()))


