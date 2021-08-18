"""Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście."""

names = input("Podaj dowolna ilosc imion ciagiem ze spacja\n")


for i in names.split():
    print("Hello", i)
