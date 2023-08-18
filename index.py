import random

opnieuw = True

woordenLijst = ["paard", "ballon", "fantasie", "klok", "celwand"]

randomIndex = random.randint(0, len(woordenLijst)-1)

randomItemUitLijst = woordenLijst[randomIndex]

while(opnieuw):

    ingevuldeLetter = input("Vul hier een letter in: ")

    woordBevatLetter = False

    for letter in randomItemUitLijst:
    

        if (ingevuldeLetter == letter):
        
            woordBevatLetter = True

        

    if (woordBevatLetter == True):
        print ("Goed gedaan")

    else:
        print ("Niet goed")


    stoppen = input("Vul hier stoppen in om te stoppen en iets anders om door te gaan: ")

    if (stoppen == "stoppen"):
        opnieuw = False

    else:
        opnieuw = True





