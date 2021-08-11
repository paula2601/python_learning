# -*- coding: utf-8 -*- 
print("Ile masz lat?")
age = int(input())

if age > 100:
    print("To naprawde Twoj wiek?")
if age >= 18:
    print("Jestes doroslym czlowiekiem")
else:
    print("Jestes niepelnoletni")

dorosly = 18 - age
print("Do pelnoletnosci zostalo Ci: %d lat" %(dorosly))


