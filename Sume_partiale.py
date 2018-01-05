# definim o functie care afiseaza numerele pana la n si calculeaza suma lor
def calc_suma(n):
	# virgula de la print suprima aparitia lui \n dupa 1
	print 1,
	suma = 1
	i = 2
	# nu uitati de ':' de la sfarsitul liniilor care preced sub-blocuri, adica
	# dupa for, while, if, def etc.
	while i <= n:
		print "+", i,
		suma += i
		i += 1
	print "=", suma

# raw_input citeste un string de la tastatura afisand promptul dat
# acest string se converteste la un intreg cu int(..)
n = int(raw_input("Dati n="))

# range(a, b) intoarce o lista ce contine [a, a+1, ..., b-1]
for i in range(1, n+1):
	calc_suma(i)