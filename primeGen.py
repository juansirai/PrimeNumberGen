# -*- coding: utf-8 -*-
"""
Considera los divisores de 30: 1, 2, 3, 5, 6, 10, 15, 30. Puede verse que para cada divisor d de 30, d + 30 / d es primo.

Encuentre la suma de todos los números enteros positivos n que no excedan 100.000.000 tal que para cada divisor d de n, d + n / d es primo.
"""

def isDiv(num, x):
    if(num%x)==0:
        return True
    else:
        return False

def operation(num, div):
    aux = num / div + div
    return aux

def isPrime(num):
    isOK = True
    div = 2
    while(isOK) and (div <num):
       if(isDiv(num, div)):
           isOK= False
       div = div+1
    return isOK
        

def evaluateNum(num):
    isOK = True
    div = 1
    aux = 0
    while (isOK) and (div <=num):
        if isDiv(num, div):
            aux = operation(num, div)
            isOK = isPrime(aux)
        div = div+1
    return isOK
    

def  primeSum(stop):
    aux =0 #stores the sum of prime numbers
    for i in range(2,stop):
        if (evaluateNum(i)):
            aux = aux + i
    return aux

# MAIN PROGRAM #

play = True
while (play):
    print("Welcome to the program, please enter a number \
          and we will calculate the sum of all the numbers in between \
          for which n/div + div is prime")
    stop = int(input("Enter the number : "))
    print("The sum is: ")
    print(primeSum(stop))
    play = bool(input("Do you want to play again? "))
