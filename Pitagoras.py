"""a) Poproś użytkownika o podanie długości boków A, B i C i sprawdź czy w ogóle możliwe jest utworzenie z nich trójkąta 🙂

b) Odpowiedz czy trójkąt jest trójkątem pitagorejskim.

c) Szczególnym przypadkiem jest trójkąt egipski o stosunkach długości 3:4:5. Sprawdź czy trójkąt pitagorejski jest trójkątem egipskim.

d) Uwzględnij, że kolejność danych nie musi mieć znaczenia! Tzn. długość C użytkownik może podać jako pierwszą wartość.
"""

a = int(input("Podaj boki: a"))
b = int(input("Podaj boki: b"))
c = int(input("Podaj boki: c"))

if  a > b:
    temp = b #wartosc temp to wart. tymczasowa, wstawiam tam nizsza wartosc b 
    b = a   # pod zmienna b wstawiam wyzsza wartosc a, teraz b > a 
    a = temp #pod zmienna a wstawiam nizsza wartosc b
if  a > c:
    temp = c
    c = a
    a = temp
if  b > c:
    temp = c
    c = b
    b = temp

print(a,b,c)

if a**2 + b**2 == c**2:
    print("Mozna utworzyc z nich trojkat pitagorejski")
    if a/3 == b/4 ==c/5:
        print("Trójkąt jest trójkątem egipskim")
elif (a + b) <= c:
    print("Mozna utworzyc trojkat ale nie jest on pitagorejski")
else:
    print("Nie mozna utworzyc trojkata")


    

