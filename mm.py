import random
Kleuren = ['oranje' , 'blauw' , 'groen', 'bruin']
kleurMM = random.choices(Kleuren)


def MMM():
    while True:
        vraag = int(input("Hoeveel MM'S wilt u hebben: "))
        if vraag <= 50:
            for i in range(vraag):
                print(random.choices(Kleuren))
            break
        elif vraag >= 50:
            print ("Sorry kies een lager getal het liefst onder 50")
            

MMM()