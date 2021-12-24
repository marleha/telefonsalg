#Oppgave 3: Kjede av sirkler

##Forst lagret jeg ezgraphics nedlastningen i samme mappe som sirkeler.py. Deretter impoterer jeg det grafiske vinduet fra ezgraphics. På neste linje
#bestemmer jeg at det grafiske vinduet skal ha en bredde og en hoyde paa 400 pixler og 200 pixler og blir lagret i variabelen win.
#Jeg setter teller til aa vaere 0. x_pos variabelen til aa vaere 10 og stoerrelse til aa vaere 10. 

from ezgraphics import GraphicsWindow
win = GraphicsWindow(400,200)






teller=0
x_pos=10
stoerrelse=10

#Jeg lager en while-lokke som bestemmer at naar teller er mindre enn 9, skal jeg faa tilgang til canvas innholdet i det grafiske vinduet. 
#Jeg ber programmet om a tegne en sirkel for meg, x koordinatet skal være x_pos verdien, og y koordinatet skal være 100 (det overste-venstre 
#hjornet til boksen sirkelen er inni) og bredden og hoyden skal begge vaere verdien til stoerrelse variabelen. Telleren skal for hver gang
#while lokken plusses med 1 til den ikke er mindre enn 9 lenger og while-lokken sluttes. x_pos skal hver gang plusses med 10 og lagres i 
#x_pos-variablene og stoerrelse skal hver gang plusses med 5 og lagres i stoerrelses variabalen.

while teller < 9: 
    canvas= win.canvas()
    canvas.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    teller +=1
    x_pos= x_pos + 10
    stoerrelse= stoerrelse + 5



#srkiver win.wait() fordi programmet maa stoppe eller pause og vente for at brukeren skal lukke vinduet, ellers vil det grafiske vinduet forsvinne 
#og man får ingen tid til å se tegningen sin. Jeg kjorer programmet og en kjede av sirkler dukker opp som for hver gang while-lokken gaar endrer
#y-koordinat, bredde og hoyde.
win.wait()


