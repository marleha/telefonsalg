#Oppgave 1:Parametere og returverdier

#Forst skiver jeg en funksjon og taster inn to heltall som parametere. Programmet
# hopper til def, og det forste parameterert lagrer seg i tall1 og det andre i tall2. 
# Paa neste linje summerer jeg tallene og lagrer den i variabelen resultat. 
#Etterpaa printer jeg resultat, variabelen resultat, og så returnerer jeg
#resultatet til funksjonen: adder(2,3). Naa er resultat lagret i adder(2,3).
#En ny funksjon kalles på og det samme skjer igjen, men denne gangen har paramteret
# andre verdier og resultatet returnerer til funksjonen: adder(4,5).

#1.
def adder(tall1,tall2):
    resultat=tall1+tall2
    print("Tallet ble:", resultat)
    return resultat 

adder(2, 3)
adder(4, 5)


#Jeg spoer bruker hva han eller hun heter og lagrer svaret i variabelen tekst. Deretter spoer 
#jeg bruker om en bokstav og lagrer svaret i variabelen bokstav. Paa neste linje printer jeg
#hvor mange ganger bokstaven forekommer i navnet. 

#2. 
tekst= input("Hva heter du?")
bokstav= input("Skriv en bokstav!")
print(tekst.count(bokstav),"ganger forekommer bokstaven i navnet ditt!")

#Programmet hopper ned til tellForekomst. Prosedyren blir kalt på, teksten i tellForekomst blir lagret i minTekst,
#og bokstaven blir lagret i minBokstav. Inni prosedyren printes det hvor mange ganger bokstaven forekommer i 
#teksten.

#3.
def tellForekomst(minTekst, minBokstav):
    print(minTekst.count(minBokstav), "ganger forekommer bokstaven!")


tellForekomst("Marlene heter jeg!", "e")
tellForekomst("Rhea heter jeg!", "e")