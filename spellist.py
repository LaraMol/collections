spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList:list, minimum = 3, maximun = 10):
    import random
    listKeuzes = []
    hoevaak = random.randint(minimum,maximun)
    for x in range(hoevaak):
        maakKeuze = random.choices(spelList)
        listKeuzes.append(maakKeuze)
    return listKeuzes

print(spelProgramma(spelList,1,7))
