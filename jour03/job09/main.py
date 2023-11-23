def moyenne(note1, note2, note3):
    cumul_note = note1 + note2 + note3
    moyenne = cumul_note / 3
    if moyenne >= 15:
        print (f"Votre moyenne est de : {moyenne}, vous êtes un très bon élève !")
    elif moyenne >= 11:
        print (f"Votre moyenne est de : {moyenne}, vous êtes un bon élève !")
    elif moyenne >= 8:
        print (f"Votre moyenne est de : {moyenne}, vous êtes un élève moyen !")
    else:
        print (f"Votre moyenne est de : {moyenne}, vous êtes un élève devant faire des efforts !")
    return moyenne
    

note1 = int(input("entrez votre première note : "))
note2 = int(input("entrez votre deuxième note : "))
note3 = int(input("entrez votre troisième note : "))

resultat_moyenne = moyenne(note1, note2, note3)


