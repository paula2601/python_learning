waga = float(input("Podaj swija wage\n"))
wzrost = float(input("Podaj swoj wzrost w metrach\n"))

BMI = waga / (wzrost **2)
print("Twoje BMI wynosi: {:.2f}" .format(BMI))

if BMI < 18.5:
    print("Niedowaga") 
elif 18.5 < BMI < 24:
    print("Waga normalna")
elif 24 < BMI < 26.5:
    print("Lekka nadwaga")
else: 
    print("Nadwaga")
    if 30 < BMI < 35:
        print("Otylosc I stopnia")
    elif 30 < BMI < 40:
        print("Otylosc II stopnia")
    else:
        print("Otylosc III stopnia")

