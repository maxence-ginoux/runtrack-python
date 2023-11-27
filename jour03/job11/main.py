def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    
    if heures == 1:
        heures_affiche = "1 heure"
    else:
        heures_affiche = f"{heures} heures"

    if minutes_restantes == 1:
        minutes_affiche = "1 minute"
    else:
        minutes_affiche = f"{minutes_restantes} minutes"

    if heures == 0:
        print(f"{minutes_affiche}")
    elif minutes_restantes == 0:
        print(f"{heures_affiche}")
    else:
        print(f"{heures_affiche} et {minutes_affiche}")


time_to_text(60)
time_to_text(120)
time_to_text(74)
time_to_text(284)
time_to_text(13)