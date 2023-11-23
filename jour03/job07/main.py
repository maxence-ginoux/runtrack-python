def salut (language):
    if language == "JavaScript":
        return "tu es un développeur web"
    elif language == "Python":
        return "tu es un développeur IA"
    elif language == "Java":
        return "tu es un développeur logiciel"
    elif language == "Reactjs":
        return "tu es un développeur mobile"
    else :
        return "un jour, je serai le meilleur développeur..."

print (salut("JavaScript"))
print (salut("Python"))
print (salut("Java"))
print (salut("Reactjs"))