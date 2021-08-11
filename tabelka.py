szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| %6.1f | %-16s | %-10s |" % (9.58, "Usain Bolt", "16.08.2009"))
print("| %06.1f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.2f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %6.3f | %16s | %10s |" % (9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

szer = 42
print('-' * szer)
print('|  Czas  |     Zawodnik     |    Data    |')
print('*' * szer)
print('| {:06.3f} | {:16s} | {:10s} |' .format(9.58, "aaa", "bbb"))
print('| {:16.3f} | {:16s} | {:10s} |' .format(9.67, "ccc", "FF"))
