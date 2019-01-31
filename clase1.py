
import random
import datetime

#v1 = input("2+3=")
#v2 = input("6+12=")
#v3 = input("7+9=")
#v4 = input("4+9=")
#v5 = input("5 + 4 =")
cont = 0
operacion=("+","-","*")
t1 = datetime.datetime.utcnow()
for i in range(9):
	v1 = random.randint(0,9)
	v2 = random.randint(0,9)
	op = random.randint(0,2)
	v = input('{} {} {} ='.format(v1,operacion[op],v2))
	#print(v1+v2)
	if op == 0:
		vt = v1+v2
	if op == 1:
		vt = v1-v2
	if op == 2:
		vt = v1*v2 

	if vt == int(v):
		cont+=1
t2 = datetime.datetime.utcnow()
print(cont)
print(t2 - t1)