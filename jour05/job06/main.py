def distance_parcouru (nombre_marche, hauteur_marche_cm):
    #nombre_marche = 200
    #hauteur_marche_cm = 30
    aller_retour_toilettes = 5
    nombre_jour_travail = 7
    distance_totale_m = ((nombre_marche * hauteur_marche_cm) * 2) / 100
    distance_jour_m = distance_totale_m * aller_retour_toilettes
    distance_semaine_m = distance_jour_m * nombre_jour_travail

    resultat = f"Pour {nombre_marche} marches de {hauteur_marche_cm}cm, le gardien parcourt {distance_semaine_m:.2f}m par semaine."
    print(resultat)

distance_parcouru(167, 30)
distance_parcouru(280, 40)
distance_parcouru(248, 32)
distance_parcouru(200, 35)
