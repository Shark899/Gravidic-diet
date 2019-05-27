index = 0
uscire = ""
def sum (num_1, num_2):
    somma = num_1 + num_2
    return somma
def moltiplication (num_1, num_2):
    moltiplication = num_1 * num_2
    return moltiplication
def divisione (num_1, num_2):
    divisione = num_1 / num_2
    return divisione
def sottrazione (num_1, num_2):
    sottrazione = num_1 - num_2
    return sottrazione


while(uscire == ""):
    first = input("Inserisci il primo numero: ");
    sign = input("Inserisci il segno: ")
    second = input("Inserisci il secondo numero: ")
    first = float(first)
    second = float(second)
    if (sign == "-"):
        print(sottrazione(first, second))
    elif (sign == "+"):
        print(sum(first, second))
    elif (sign == "*"):
        print(moltiplication(first, second))
    elif (sign == "/"):
        print(divisione(first, second))
    uscire = input("Schiacciare un tasto se vuoi uscire")

