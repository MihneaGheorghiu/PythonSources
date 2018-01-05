import threading
import time
import random


bariera = threading.Semaphore(value=0)
regcritica = threading.Semaphore(value=1)
threads = 5
n=threads
threadlist = []

def folosire(x):
    for i in range(3):
        print "Thread:",i
        
        print "intrare in bariera: ",x
        barrier()
        print "iesire din bariera: ",x

def barrier():
    global bariera,regcritica,n,threads
    regcritica.acquire();
    n-=1;
    if n==0:
        for i in range(threads):
            bariera.release();
        n = threads
    regcritica.release();
    bariera.acquire();
            

random.seed()            

            
for i in range(threads):
    thread = threading.Thread(target=folosire, args=(i,))
    thread.start()
    threadlist.append(thread)
                    
for i in range(len(threadlist)):
    threadlist[i].join()
