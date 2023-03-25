
print("Jakub Zlamal's Calculator")
print("Dostupné možnosti znamének: sčítání (+), odčítání (-), násobení (*), dělení (/), mocnina na druhou (^), mocnina na třetí (^3), odmocnina (!) ")

Číslo1 = float(input("Zadejte číslo: "))
Znaménko = input("zadejte znaménko: ")

if Znaménko == "^":
    result = Číslo1 * Číslo1
    print("Výsledek: " + str(result))
elif Znaménko == "^3":
    result = Číslo1 * Číslo1 * Číslo1
    print("Výsledek: " + str(result))
elif Znaménko == "!":
    result = Číslo1**0.5
    print("Výsledek: " + str(result))
elif Znaménko == "+," or "-" or "*" or "/":
    Číslo2 = float(input("Zadejte druhé číslo: "))
    if Znaménko == "+":
        result = Číslo1 + Číslo2
        print("Výsledek: " + str(result))
    elif Znaménko == "-":
        result = Číslo1 - Číslo2
        print("Výsledek: " + str(result))
    elif Znaménko == "*":
        result = Číslo1 * Číslo2
        print("Výsledek: " + str(result))
    elif Znaménko == "/":
        result = Číslo1 / Číslo2
        print("Výsledek: " + str(result))
    else:
        print("Špatné znaménko!")
