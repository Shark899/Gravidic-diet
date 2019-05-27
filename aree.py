count = ""
exit = ""


def areaTriangolo():
    base = input("Inserire la base: ")
    altezza = input("Inserire l'altezza")
    base = float(base)
    altezza = float(altezza)
    area = (base * altezza) / 2
    print(area)


def areaRettangolo():
    base = input("Inserire la base: ")
    altezza = input("Inserire l'altezza")
    base = float(base)
    altezza = float(altezza)
    area = base * altezza
    print(area)


while (exit == ""):
    print("1. Area triangolo")
    print("2. Area rettangolo")
    count = input("Inserire il numero della calcolazione da effettuare: ")
    if (count == "1"):
        areaTriangolo()
    if (count == "2"):
        areaRettangolo()
    exit = input("Schiacciare un tasto per uscire")

