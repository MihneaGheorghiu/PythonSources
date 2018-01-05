SIMULAREA ACTIVITATII DIN PARLAMENT


Acest program simuleaza activitatea din parlament pe decursul a 3 zile.

Am folosit python pentru implementare sub windows.

Codul a fost scris in notepad++ pentru aurmari mai usor identarea.

Pentru al rula si testa am folosit run->cmd

comanda: python tema1.py n m > out.txt

Am folosit in general 50 ptr n si 20 ptr cabine (5 cabine doar la unul din subpuncte).
Deasemnea 50-2*20 = 10 parlamentari care nu numara, usor de identificat
out.txt-> redirectarea  intrun fisier ptr a putea urmari intreg outputul care are 50KB si ptr a putea folosi find in urmarirea parlamentarilor/cabineleor

	Ideea de implementare: threaduri ptr fiecare parlamentar (o clasa ce extinde thread), lock ptr fiecare cabina (clasa definita), o bariera reentranta de fiecare data cand era necesara asteptarea tuturor parlamentarilor pentru a trece la pasul urmator( similar ca cea din little book o semaphores).
	Codul este usor de urmarit data fiind impartirea in 5 etape ce contin printurile cu efectul fiecarui pas, de aceea am si putine comentarii. Programul are un bloc de intructiuni in care se preaiua valorile de pornire si se creeaza o lista deparlamentari si una de cabine. Apoi fiecare thread merge prin cele 5 etape dea lungul a 3 zile (in fctia run()).

*la etapa 4 nu prea mergea si am sters merge doar ptr aia care nu numara
	