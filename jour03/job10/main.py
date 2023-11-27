def pair_ou_impair(nombre):
    if isinstance(nombre, int) and nombre >=0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else :
        print(f"{nombre} n'est pas un nombre entier positif")

pair_ou_impair(5)
pair_ou_impair(10)
pair_ou_impair(8)
pair_ou_impair(7)
pair_ou_impair(2.5)
pair_ou_impair(-10)