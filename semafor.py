import threading
import time
import random

# vor fi maxim 3 thread-uri active la un moment dat
maxconnections = 3

semafor = threading.Semaphore(value=maxconnections)

def folosire(x):
	global semafor
	
	semafor.acquire()
	print "thread ",x," : enter"
	time.sleep(random.random()*5)
	print "thread ",x," : exit"
	semafor.release()

threads = 10
threadlist = []

random.seed()

print "starting threads"

for i in range(10):
	thread = threading.Thread(target=folosire, args=(i,))
	thread.start()
	threadlist.append(thread)

for i in range(len(threadlist)):
	threadlist[i].join()

print "program finished"

