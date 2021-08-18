age = int(input("Ile masz lat?\n"))

if age >= 100:
    print("200 lat")
if age < 18:
    print("Uzytkownik niepelnoletni, do plenoletnosci zostalo:", 18 - age)
else:
    print("Uzytkownik pelnoletni")
    
