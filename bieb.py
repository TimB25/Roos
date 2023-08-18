
Vraag de gebruiker om 2 getallen

Tel deze getallen bij elkaar op en geef het antwoord terug aan de gebruiker


getal1 = int(input("Type hierachter het eerste getal van de berekening en druk op enter:  "))
getal2 = int(input("Type hierachter het tweede getal van de berekening en druk op enter:  "))

totaal = getal1 + getal2

print(totaal)

------
naam1 = input("Type hierachter je naam en druk op enter: ")
verhaal = " loopt naar de boekwinkel met Jantje, terwijl ze aan het kletsen zijn."

totaal = naam1 + verhaal

print(totaal)


##Tim
i = 1
y = 5
h = -2
if((i > (y + h))):
    print("if is gedaan")

elif():
    print("Else if")

else:
    print("else")




WACHTWOORD = "GeheimWachtwoord"





    


def Authenticatie():
    ingevuldeWachtwoord = input("Type hier het wachtwoord en druk op enter: ")


    if (ingevuldeWachtwoord == WACHTWOORD):
        print("Een paard liep vrolijk in de wei te grazen.")

    else:
        print("Fout")
        Authenticatie()




Authenticatie()


import random
i = 100

while(i > 0):

    print(random.randint(1,6))
    i -= 1
    







""""

Vraag gebruiker om getal
Genereer een random aantal (tussen de 10 en 1000) 
en genereer daarna zoveel random getallen tussen de 0 en 1000001
Het hoogste getal van deze getallen is het geheime getal van de computer. 
vertel een verhaal waarbij je de gebruiker bij naam aanspreekt 
en verteld hoeveel hij of zij er naast zat met de gok .
Dit spel moet doorgaan totdat de gebruiker aangeeft te willen stoppen. 
"""
import random

i = True

naam = input("Type hier je naam en druk op enter: ")

while(i):

    ingevuldGetal = int(input("Type hier het getal en druk op enter: "))

    aantalGetallen = (random.randint(11,999))


    hoogsteGetal = 0

    while(aantalGetallen > 0):



        Paard = (random.randint(1,1000000))

        if(Paard > hoogsteGetal):
            hoogsteGetal = Paard

        aantalGetallen -= 1


    if (hoogsteGetal == ingevuldGetal):
        print ("Geweldig gedaan " + naam + "!")

    else:
        if(hoogsteGetal > ingevuldGetal):
            verschil =  hoogsteGetal - ingevuldGetal 
        else:
            verschil =  ingevuldGetal - hoogsteGetal 
        print ("Helaas " + naam + ". Je zat er met " + str(verschil) + " naast. Het getal was "+ str(hoogsteGetal)+" Volgende keer beter!")

    stoppen = input("Vul hier stoppen in om te stoppen en iets anders om door te gaan: ")

    if (stoppen == "stoppen"):
        i = False

    else:
        i = True


mijnLijst = [23, 3, 25]
randomIndex = random.randint(0, len(mijnLijst)-1)

randomItemUitLijst = mijnLijst[randomIndex]

print(mijnLijst[3])
mijnLijst.append(567)
print(mijnLijst)
mijnLijst.sort()
print(mijnLijst)
mijnLijst.insert(1, 999)
print(mijnLijst)

intiger = 375457
for item in intiger:
    print(item)

        
        




