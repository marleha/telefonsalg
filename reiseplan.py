#Oppgave 4: Reiseplan

#Forst lager jeg en liste steder. Deretter lager jeg en for-lokke, som bes om aa gjore noe 5 ganger. 
# Paa neste linje, inne i for-lokken, ber jeg bruker skrive inn et reisemaal og dette lagres 
#listen steder. Deretter printer jeg listen. Dette skjer 5 ganger. Det samme gjoer jeg naar jeg lager
#klesplagg og avreisedatoer listene. 
steder=[]

for i in range(5):
        steder.append(input("Skriv inn et reisemaal: "))
        print(steder)

klesplagg=[]

for i in range(5):
        klesplagg.append(input("Skriv inn et klesplagg: "))
        print(klesplagg)

avreisedatoer=[]

for i in range(5):
        avreisedatoer.append(input("Skriv inn en avreisedato: "))
        print(avreisedatoer)

#Jeg lagrer deretter en reiseplan liste som listene steder, klesplagg og
#avreisedatoer blir lagret inni. Deretter printer jeg reiseplan listen. 

reiseplan=[steder]+[klesplagg]+[avreisedatoer]
print(reiseplan)

#Jeg ber for-lokken om aa printe hvert element i reiseplan listen.

for h in reiseplan:
        print(h)

#Forst ber jeg bruker taste inn hvilken listen han eller hun vil ha i reiseplan listen 
# og lagrer tallet i i1. Deretter Hvilket element brukeren vil ha i den valgte listen og lagrer tallet
#i i2. Deretter setter jeg inn en if-setning for aa sjekke om det bruker taster inn
#er gyldig. Hvis i1 er lik eller hoeyere enn 0 og i1 er mindre enn eller er lik antall 
#elementer i liste minus 1, og i2 er lik eller stoerre enn 0 og i2 er lik eller mindre antall listen
#som naa er i1 minus 1, vil elementet i listen brukeren soeker etter bli printet.
#Hvis ikke blir ugyldig input printet.

i1= int(input("Hvilken liste vil du ha?"))
i2= int(input("Hvilket element i listen vil du ha?")) 
if (i1 >= 0 and i1 <= len(reiseplan)-1) and (i2 >= 0 and i2 <= len(reiseplan[i1])-1):
        print(reiseplan[i1][i2])
else:
        print("Ugyldig input!")
