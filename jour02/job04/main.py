N=int(input("Entrer un entier supérieur à 0 :"))

for i in range(1, N + 1):
    print(f"Table de multiplication de {i} :")
    for j in range (1, 11):
        print (f"{i} x {j} = {i*j}")