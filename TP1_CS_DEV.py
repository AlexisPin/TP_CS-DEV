year = int(input("Entrez l'année:"))
strYear = str(year)
if year % 4 == 0 and strYear[2] != 0 and strYear[3] != 0 or year % 400 == 0:
    year = str(year)
    print("L'année {} est une année bissextile!" .format(year))
else:
    print("L'année {} n'est pas une année bissextile!" .format(year))

dffbbffbbbffb