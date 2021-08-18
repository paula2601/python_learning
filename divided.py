"""Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony"""

ile_razy = int(input("Ile razy mam wykonac petle?\n"))


for i in range(0,ile_razy):
    liczba = int(input("Podaj dowolna liczbe\n"))
    if liczba % 3 == 0 and liczba % 4 == 0:
        print("Hurra!")
    elif liczba % 3 == 0:
        print("Liczba jest wielkokrotnoscia 3")
    elif liczba % 4 == 0:
        print("Liczba jest wielkotnoscia 4")
    elif liczba % 3 != 0 and liczba % 4 != 0:
        print("*")
    
    
