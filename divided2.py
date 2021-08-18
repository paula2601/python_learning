j=2
for i in range(0,j):
       i=int(input("podaj liczbę do spr: "))
       if i%3==0:
             print("podzielna przez 3")
       if i%4==0:
              print("podzielna przez 4")
       if i%3==0 and i%4==0:
              print("Hurra")
       if i%3!=0 and i%4!=0:
              print("*")
       print("Jeśli chcesz zakończyć wpisz 0, jeśli chcesz sprawdzać dalej - wpisz 1.")
       k=int(input())
       if k==0:
              print("Koniec")
              j=2

       else:
              j=j+1
