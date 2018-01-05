import math # import modulul math
from sys import argv # din modulul sys import lista argv (argumente in linia de comanda)

 
def isPrime(x): # definesc o functie care decide daca x e prim
    for i in range(2, int(math.sqrt(x)+1)): # range(a, b) => lista [a, ..., b-1]
        if x % i == 0: # nu uita de ':' !
            return 0

    return 1

 

def buildPrimes(max = 100): # se poate da o valoare implicita pentru parametru
    result = [] # initializez lista
    for i in range(1, max+1):
        if isPrime(i):
            result.append(i) # adaug la sfarsitul ei un nou element

    return result

# pentru ca parametrul are o valoare implicita, vom putea apela si asa: buildPrimes()

 

if len(argv) == 2: # argv[0]=nume script; len(argv)==2 inseamna un argument in plus
    n = int(argv[1])
    print buildPrimes(n)
else: # daca nu am un parametru
    try:
        n=int(raw_input("Dati N= ")) # raw_input citeste un string de la tastatura

      # daca a fost "prinsa" o exceptie:
    except(ValueError):
        print "Asteptam un numar intreg."
    else:
        for k in buildPrimes(n): # tiparesc fiecare numar din lista
            print k,
        print # print simplu inseamna de fapt newline
