#Oppgave 5: Egen oppgave

#Oppgave: Lag en liste over naar vennene dine har bursdag!
#Lag to tomme lister du velger navn paa selv. Spoer 5 ganger bruker hvem han eller hun vil lagre i bursdagslisten sin og
#naar han eller hun har bursdag. Lagre begge svarene i hver sin liste og print listene. Deretter skal bruker kunne sooke
#opp personen og naar personen har bursdag. Hvis navnet ikke finnes i listen skal du gi beskjed om dette. Deretter skal du be
#bruker aa legge til en person og naar personen har bursdag. Print listene. Til slutt skal brukerigjen finne en person
#og naar personen har bursdag. Hvis navnet ikke finnes i listen gi beskjed om dette. 

#Kommentar: Forst lager jeg en tom liste jeg kaller bursdagsliste og en tom liste jeg kaller bursdagsdato. Deretter lager jeg 
#en for-lokke som bes om aa gjoere noe 5 ganger. Jeg ber brukeren skrive inn navnet til en venn han eller hun vil lagre i listen
#og lagrer svaret i variabelen navn. Deretter lagrer jeg navnet i listen bursdagsliste. På neste linje spoer jeg bruker naar
#vennen har bursdag og lagrer det i variabelen dato. Dato variabelen blir lagt inn i bursdagsdato listen. Dette skjer 5 ganger.
#Naar det inne i for-lokken er ferdig kjoert, 5 ganger, printer jeg listene bursdagsliste og bursdagsdato for aa faa en oversikt.

bursdagsliste= []
bursdagsdato=[]

for c in range(5):
    navn=input("Hva heter vennen din du vil lagre i bursdagslisten din? ")
    bursdagsliste.append(navn)
    dato=input("Naar har vennen din bursdag? ")
    bursdagsdato.append(dato)

print(bursdagsliste)
print(bursdagsdato)

#Jeg ber bruker om hvem han eller hun vil soeke opp i bursdagsliste, og lagrer svaret i variabelen finneut. I en if setning,
#hvis navnet, eller finnetut variabelen er paa indeks 0 i bursdagsliste, blir navnet og bursdagsdatoen som også befinner seg på indeks 0 i listen 
#bursdagsdato printet. Videre gjor jeg det sammen, bare at jeg bruker elif og oker indeksen med en for hver gang. Indeks 4 er den siste, fordi 
#det er 5 elemeneter i listene (Indeksene gaar da fra 0 til 4 i begge listene). Hvis programmet ikke finner navnet i listen, blir det printet
#at personen ikke finnes i bursdagslisten. 

finneut= input("Hvem du vil sooke opp i bursdagslisten din? ")
if finneut == bursdagsliste[0]:
    print(bursdagsliste[0],"har bursdag", bursdagsdato[0],"!")
elif finneut == bursdagsliste[1]:
    print(bursdagsliste[1],"har bursdag", bursdagsdato[1],"!")
elif finneut == bursdagsliste[2]:
    print(bursdagsliste[2],"har bursdag", bursdagsdato[2],"!")
elif finneut == bursdagsliste[3]:
    print(bursdagsliste[3],"har bursdag", bursdagsdato[3],"!")
elif finneut == bursdagsliste[4]:
    print(bursdagsliste[4],"har bursdag", bursdagsdato[4],"!")
else:
    print("Denne personen finnes ikke i bursdagslisten din!")

#Jeg ber bruker legge til et navn i bursdagslisten og lagrer svaret i variabelen leggetilnavn. Paa neste linje blir navnet lagret i bursdagsliste.
#Jeg spoer naar vennen har bursdag og lagrer svaret i variabelen legetildato. leggetildato blir deretter lagret i bursdagsdato listen. Bursdagslisten
#og bursdagsdato listen blir printet for aa faa en oversikt. Etterpaa spoer programmet om hvem bruker vil soeke opp. Det som tidligere skjedde,
#naar bruker skulle soeke opp en venn, skjer igjen. 

leggetilnavn= input("Hvem vil du legge til i bursdagslisten din? ")
bursdagsliste.append(leggetilnavn)
leggetildato= input("Naar har vennen din bursdag? ")
bursdagsdato.append(leggetildato)

print(bursdagsliste)
print(bursdagsdato)

finneut= input("Hvem du vil sooke opp i bursdagslisten din? ")
if finneut == bursdagsliste[0]:
    print(bursdagsliste[0],"har bursdag", bursdagsdato[0],"!")
elif finneut == bursdagsliste[1]:
    print(bursdagsliste[1],"har bursdag", bursdagsdato[1],"!")
elif finneut == bursdagsliste[2]:
    print(bursdagsliste[2],"har bursdag", bursdagsdato[2],"!")
elif finneut == bursdagsliste[3]:
    print(bursdagsliste[3],"har bursdag", bursdagsdato[3],"!")
elif finneut == bursdagsliste[4]:
    print(bursdagsliste[4],"har bursdag", bursdagsdato[4],"!")
elif finneut == bursdagsliste[5]:
    print(bursdagsliste[5],"har bursdag", bursdagsdato[5],"!")
else:
    print("Denne personen finnes ikke i bursdagslisten din!")
