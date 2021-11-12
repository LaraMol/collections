import random
Kleuren = ['oranje' , 'blauw' , 'groen', 'bruin']


def MMM():
    zak = {}
    while True:
        vraag = int(input("Hoeveel MM'S wilt u hebben: "))
        if vraag <= 50:
            for i in range(vraag):
                kleurMM = random.choice(Kleuren)
                if kleurMM in zak:
                    zak[kleurMM] += 1
                else:
                    zak.update({kleurMM:1})
            return zak
        elif vraag >= 50:
            print ("Sorry kies een lager getal het liefst onder 50")
        
            
print(MMM())