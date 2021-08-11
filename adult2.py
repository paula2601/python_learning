age = int(input("Ile masz lat?"))
responsible = input("Czy jestes odpowiedzialny? T/N")

if age > 100:
    print("To naprawde twoj wiek?")
elif age >= 18 and responsible == "T":
    print("Jestes doroslym czlowiekiem")
elif responsible != "T":
    print("Pracuj nad odpowiedzialnoscia")
else :
    print("Troche ci zostalo do doroslosci")
    
