#Oppgave 2: Rening med lokker

#Forst lager jeg en liste. Deretter leser programmet et tall fra bruker. Tallet blir lagt inn i listen.
#Deretter printes "Naa er listen" i tekst og deretter listen. 
liste=[] 
innlest=int(input("Skriv inn et tall:"))
liste.append(innlest)
print("Naa er listen:")
print(liste)

#while lokken sjekker om den innleste variabelen ikke er 0, hvis den ikke er 0 printes det at bruker skal taste
#inn et nytt tall og tallet blir lagret som tall. tallet blir lagret i listen og listen blir printet. Hvis tallet
#brukeren taster inn er 0, hopper programmet ned til for-lokken.
while innlest != 0:
    innlest=int(input("Skriv inn et nytt tall:"))
    liste.append(innlest)
    print(liste)

#for-lokken ber programmet å gaa gjennom hvert element i listen og deretter printe hvert element.
for i in liste:
    print(i)
    
#Jeg lager en variabel som jeg setter til 0. for-lokken gaar gjennom hvert tall i listen. Deretter plusser variabelen
#MinSum med hvert element og lagrer den i variabelen MinSum. Deretter printer MinSum.
MinSum = 0
for tallet in liste:
    # MinSum += tallet
    MinSum = MinSum + tallet
print("Summen av listen er:", MinSum)

#Jeg setter en variabel "storste "til å vaere 0. Deretter ber programmet "for hvert element i listen". for lokken sjekker paa neste linje om et element er storre enn variabelen
# storste, som er satt til aa vaere 0, lagrer hvis elementet er storre, og gaar videre og sjekker hvert element til den har lagret det storste elementet.
#Det storste elementet blir lagret i variabelen "storste" og etterpaa printes denne variabelen.
storste=0
for s in liste:
    if s > storste:
        storste= s
print("Det storste tallet er:", storste)

#Jeg setter en variabel "minste" til å vaere 0. Deretter ber programmet "for hvert element i listen". for lokken sjekker paa neste linje om et element er mindre enn variabelen
#minste, som er satt til aa vaere 0, lagrer hvis elementet er mindre, og gaar videre og sjekker hvert element til den har lagret det minste elementet. 
#Det minste elementet blir lagret i variabelen "minste" og etterpaa printes denne variabelen.
minste=0 
for m in liste:
    if m < minste:
        minste= m
print("Det minste tallet er:", minste)



