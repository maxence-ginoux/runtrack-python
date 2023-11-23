def coucou (type , saison):
    if type == "fruits" and saison == "hiver":
        print ("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print ("poire, fraise, cassis")
    elif type == "légumes" and saison =="hiver":
        print ("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été":
        print ("artichaut, aubergine, navet")


coucou("fruits" , "hiver")
coucou("fruits", "été")
coucou("légumes", "hiver")
coucou("légumes", "été")