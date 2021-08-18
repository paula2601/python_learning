# -*- coding: utf8 -*-

"""
Wskaż najwyższą wartość z 3 liczb
i posortuj je od największej do najmniejszej.
"""

a = 1
b = 7
c = 5.65

if a > b and a > c:
    maximum = a
elif b > a and b > c:
    maximum = b
elif c > a and c > b:
    maximum = c

print(maximum)

if a < b:
    temp = a 
    a = b  # a wynosi teraz 7
    b = temp # b wynosi teraz 1 
if a < c: # teraz sprawdza czy 7 jest mniejsze od 5.65
    temp = a
    a = c
    c = temp
if b < c: # teraz sprawdza czy b czyli 1 jest mniejsze od c czyli 5.65 
    temp = b 
    b = c # zamieniamy b na c czyli b wynos 5.65 
    c = temp # c wynosi 1 
print (a , b, c)

