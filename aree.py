count = ""
exit = ""

def areaCerchio():
    PI = 3.1415
    raggio = input("Inserire il raggio: ")
    raggio = float(raggio)
    area = PI * pow(raggio,2)
    print(area)
def areaTriangolo():
    base = input("Inserire la base: ")
    altezza = input("Inserire l'altezza")
    base = float(base)
    altezza = float(altezza)
    area = (base * altezza) / 2
    print(area)

def areaQuadrato():
    lato = input("Inserire il lato: ")
    lato = float(lato)
    area = lato * lato
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
    print("3. Area quadrato")
    print("4. Area cerchio")

    count = input("Inserire il numero della calcolazione da effettuare: ")
    if (count == "1"):
        print("L'area del triangolo e' base x altezza tutto diviso 2!")
        areaTriangolo()
    if (count == "2"):
        print("L'area del rettangolo e' base x altezza!")
        areaRettangolo()
    if (count == "3"):
        print("L'area del quadrato e' lato x lato")
        areaQuadrato()
    if (count == "4"):
        print("L'area del cerchio e' pi greco é raggio elevato al quadrato")
        areaCerchio()
    exit = input("Schiacciare un tasto per uscire")

