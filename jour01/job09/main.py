nom = "montre"
prix_unitaire = "1000€"
quantité_en_stock = "20"
print("informations sur le produit")
print("nom :", nom,"| prix unitaire :", prix_unitaire, "| quantité en stock :", quantité_en_stock)

achat = int(input("Combien de produits souhaitez-vous acheter ? "))

if achat < quantité_en_stock:
    quantité_en_stock -= achat
    print("\nVous avez acheté {achat} {nom}.")
    print("Nouvelle quantité en stock de {nom} : {quantité_en_stock}")
else:
    print("\nDésolé, la quantité demandée n'est pas disponible en stock.")