wiek = int(input("Ile masz lat?"))

if wiek < 18:
    print("Uzytkownik niepelnoletni, do pelnoletnosci zostali Ci: {}" .format(18-wiek))
elif wiek >= 100:
    print("200 lat!")
else:
    print("Uzytkownik pelnoletni")
    
