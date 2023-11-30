def evaluation_eleve():
    note = float(input("Entrez votre note sur 100 : "))

    if note >= 40:
        multiple_de_5 = ((note // 5) + 1) * 5
        difference = multiple_de_5 - note

        if difference < 3:
            note_arrondie = multiple_de_5
        else:
            note_arrondie = note

        print("Félicitations, vous avez réussi le test!")
        print("La note est arrondie à", note_arrondie)
    else:
        print("Désolé, vous avez échoué au test.")

evaluation_eleve()