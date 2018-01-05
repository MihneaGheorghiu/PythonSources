#SIMULAREA ACTIVITATII DIN PARLAMENT
#Gheorghiu Mihnea, 346CB

import threading
import time
import random
import sys

from threading import Thread
from threading import Lock


#definim barierele ptr bariera reentranta
turnstile = threading.Semaphore(0)
turnstile2 = threading.Semaphore(1)
mutex = threading.Semaphore(1)

#bariera reentranta,
def barrier():
	global count
	mutex.acquire()
	count += 1
	if count == n:
		turnstile2.acquire() # lock the second
		
		turnstile.release() # unlock the first
	mutex.release()

	turnstile.acquire() # first turnstile
	
	turnstile.release()
 
 #critical point

	mutex.acquire()
	count -= 1
	if count == 0:
		turnstile.acquire() # lock the first
		
		turnstile2.release() # unlock the second
	mutex.release()

	turnstile2.acquire() # second turnstile
	
	turnstile2.release()

#definim tipul de date ptr cabine
class Cabina:

	#constructorul clasei cabina
	def __init__(self,numar_cabina):
		self.lock = Lock()
		self.id = numar_cabina
		self.urnaNeagraBileNegre = 0
		self.urnaNeagraBileAlbe = 0

#clasa folositaptr parlamentari
class MyThread(Thread):

	#contructorul clasei parlamentari
	def __init__(self,numar_ordine):
		Thread.__init__(self)
		self.id=numar_ordine
		contor =0

	#functia principala run
	def run(self):
		global contor
		contor += 1
		for ziua in range(3):

			#etapa 1 - prezenta
			print "ziua %d, parlamentarul %d, prezent\n" %(ziua,self.id)
			barrier()

			#etapa 2
			stare = random.randint(0,3)
			if stare == 0:
				print "ziua %d, parlamentarul %d, activitate: sunt atent\n" %(ziua,self.id)
			elif stare ==1:
				print "ziua %d, parlamentarul %d, activitate: citesc\n" %(ziua,self.id)
			elif stare ==2:
				print "ziua %d, parlamentarul %d, activitate: mananc\n" %(ziua,self.id)
			else:
				print "ziua %d, parlamentarul %d, activitate: dorm\n" %(ziua,self.id)
				time.sleep(random.random()*0.5)
			barrier()
			
			#etapa 3.1
			print "ziua %d, parlamentarul %d, am luat bilele\n" %(ziua,self.id)
			#am adaptat timpul astfel incat outputul si intercalarea dintr cei care iau bile si 
			#cei care semneaza sa fie cat de cat realiste, data fiind viteza mare a executiei
			time.sleep(random.random()*0.01) 
			print "ziua %d, parlamentarul %d, am semnat\n" %(ziua,self.id)


			#etapa 3.2
			cabina_vot = random.randint(0,m-1)
			print "ziua %d, parlamentarul %d, aleg cabina %d \n" %(ziua,self.id, cabina_vot)
			cabine[cabina_vot].lock.acquire()
			time.sleep(random.random()*0.01)
			print "ziua %d, parlamentarul %d, sunt in cabina %d\n" %(ziua,self.id, cabina_vot)

			#etapa 3.3
			time.sleep(random.random()*0.01)
			optiune = random.randint(0,2)
			if optiune == 0:
				print "ziua %d, parlamentarul %d, cabina %d, am decis vot: nul \n" %(ziua,self.id, cabina_vot)
				cabine[cabina_vot].urnaNeagraBileNegre = cabine[cabina_vot].urnaNeagraBileNegre + 1
				cabine[cabina_vot].urnaNeagraBileAlbe = cabine[cabina_vot].urnaNeagraBileAlbe + 1
			elif optiune == 1:
				print "ziua %d, parlamentarul %d, cabina %d,  am decis vot: pentru\n" %(ziua,self.id, cabina_vot)
				cabine[cabina_vot].urnaNeagraBileNegre = cabine[cabina_vot].urnaNeagraBileNegre + 1
			else:
				print "ziua %d, parlamentarul %d, cabina %d,  am decis vot: contra \n" %(ziua,self.id, cabina_vot)
				cabine[cabina_vot].urnaNeagraBileAlbe = cabine[cabina_vot].urnaNeagraBileAlbe + 1

			cabine[cabina_vot].lock.release()
			barrier()
			
			# etapa4
			
			# pentru cei care nu trebuie sa numere si care asteapta
			if self.id > 2*m - 1 :
				laNumarat= random.randint(0,3)
				if laNumarat == 0:
					print "ziua %d, parlamentarul %d, la numarare: sunt atent\n" %(ziua,self.id)
				elif laNumarat ==1:
					print "ziua %d, parlamentarul %d, la numarare: citesc\n" %(ziua,self.id)
				elif laNumarat ==2:
					print "ziua %d, parlamentarul %d, la numarare: mananc\n" %(ziua,self.id)
				else:
					print "ziua %d, parlamentarul %d, la numarare: dorm\n" %(ziua,self.id)
					time.sleep(random.random()*0.5)

			# pentru cei care numara
			
			barrier()


			#etapa5
			print "ziua %d, parlamentarul %d, am parasit sala\n" %(ziua,self.id)
			barrier()

random.seed()
contor=0
count = 0
#z=int(1)
#citire argumente
if len(sys.argv)== 3:
	n=int(sys.argv[1])
	m=int(sys.argv[2])
	#print n
	#print m
	#listele de parlamentari si de cabine
	threadlist = []
	cabine = []
	#umplu lista de cabine
	for i in range(m):
		cab = Cabina(i)
		cabine.append(cab)
	#generare threaduri - unul ptr fiecare parlamentar
	for i in range(n):
		thread = MyThread(i)
		thread.start()
		threadlist.append(thread)
	for i in range(len(threadlist)):
		threadlist[i].join()
	
#mesaj de eroare pentru  utilizare incorecta
else:
	print "Format corect: tema1.py nr_parlamentari nr_cabine"



