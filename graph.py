from turtle import *
import time
from mathseq import *

seq = Sequences(0)
#vanseq = seq.VanEck_seq()

#vanseq = seq.fibonacci()

#vanseq = seq.even_seq()

#vanseq = seq.xibonacci(3)


vanseq = seq.prime_generator(100000)






vans = []

for _ in range(1000):
	vans.append(next(vanseq))

lists = [x*x for x in range(300,400)][::2]

radius = 12

turtle = Turtle()
turtle.speed(0)


print(vans)
def star(lists,rad):
	for l in lists:
		act = (lists[-1] / rad ) * l
		print(act)
		turtle.left(45)
		#time.sleep(0.5)
		turtle.forward(act)
		#time.sleep(0.5)
		turtle.left(45)
		#time.sleep(0.5)
		turtle.backward(act)
		#time.sleep(0.5)





star(vans,120)

done()