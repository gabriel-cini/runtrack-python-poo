def calcule(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return calcule(x * x, n // 2)
    else:
        return x * calcule(x, n - 1)

x = int(input("Entrez un nombre entier : "))
n = int(input("Entrez un exposant entier : "))

resultat = calcule(x, n)

print(f"{x}^{n} = {resultat}")
