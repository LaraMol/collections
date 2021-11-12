listOne = [1,2,3,4,5,6,7,8,9,10]
listTwo =[2,4,6,8,10,12,14,16,18,20]



def add (listOne, listTwo):
    print("---------------")
    for x in range(len(listOne)):
        resultaat = listOne[x]+ listTwo[x]
        print (f' {listOne[x]} + {listTwo[x]} = {resultaat}')
        

add(listOne, listTwo)

print ("\n")
def subtract (listOne, listTwo):
    print("---------------")
    for x in range(len(listOne)):
        resultaat = listOne[x] - listTwo[x]
        print (f' {listOne[x]} - {listTwo[x]} = {resultaat}')
        

subtract(listOne, listTwo)

print ("\n")

def multiply (listOne, listTwo):
    print("---------------")
    for x in range(len(listOne)):
        resultaat = listOne[x] * listTwo[x]
        print (f' {listOne[x]} x {listTwo[x]} = {resultaat}')
        

multiply(listOne, listTwo)

print ("\n")

def divide (listOne, listTwo):
    print("---------------")
    for x in range(len(listOne)):
        resultaat = listOne[x] / listTwo[x]
        print (f' {listOne[x]} : {listTwo[x]} = {resultaat}')
        

divide(listOne, listTwo)