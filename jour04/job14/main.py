def my_long_word(number, chaine):
    mots_longs = []
    mots = ""
    nombre = 0

    for lettre in chaine:
        if lettre != " ":
            mots += lettre
            nombre += 1
        else:
            if nombre > number:
                mots_longs.append(mots)
            mots = ""
            nombre = 0

    if nombre > number:
        mots_longs.append(mots)

    return mots_longs

chiffres_entiers = 3
caracteres = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(chiffres_entiers, caracteres)

print(str(chiffres_entiers) + " : " + " ".join(resultat))