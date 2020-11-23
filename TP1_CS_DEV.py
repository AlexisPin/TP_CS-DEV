year = int(input("Entrez l'année:"))
strYear = str(year)


def bissextile(year):
    if year % 4 == 0 and strYear[2] != "0" or strYear[3] != "0" or year % 400 == 0:
        return True
    else:
        return False


bissextile(year)
