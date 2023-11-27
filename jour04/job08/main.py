L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme_nombres_paires = 0
for nombre in L:
    if nombre % 2 == 0:  
        somme_nombres_paires += nombre  

print("La somme des nombres paires de la liste est :", somme_nombres_paires)
