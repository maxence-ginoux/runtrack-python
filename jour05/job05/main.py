def chiffrage_message(message="", decalage=0):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_decale = ''
    if not message or decalage == 0:
        raise ValueError("")

    print(f"-> Le message original est :\n=> {message}\n")

    for lettre in message:
        if lettre.lower() in alphabet:
            index = (alphabet.index(lettre.lower()) + decalage) % len(alphabet)
            if lettre.isupper():
                message_decale += alphabet[index].upper()
            else:
                message_decale += alphabet[index]
        else:
            message_decale += lettre

    print(f"-> Le message chiffré est :\n=> {message_decale}")
    return message_decale

message_original = "Veni Vidi Vici !"
decalage = 3
resultat = chiffrage_message(message_original, decalage)