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
turtle.speed(1)


testfall = [100,200,230,0,2,4,5,0,1,1,0,0,1]



#print(vans)
def star(lists,rad):
	for l in lists:
		act = (lists[-1] / rad ) * l
		print(act)
		turtle.left(45)
		turtle.forward(act)
		#turtle.left(45)
		turtle.backward(act)




def falldown(lists):
	fall = 0
	turtle.penup()
	turtle.goto(-300,-0)
	turtle.pendown()
	for x in range(len(testfall)-1):
		#print(test,"is at pos",x)
		last = testfall[x]
		hello = testfall[x+1]

		if hello < last:
			turtle.forward(100)
			turtle.left(-85)
			turtle.forward(100)
			turtle.left(170)
			turtle.forward(100)
			turtle.left(-85)
			turtle.forward(100)
			#time.sleep(2)
			turtle.backward(100)

			fall += 1
		else:
			turtle.forward(100)
			turtle.backward(100)
			continue

	print("falls :",fall)









#star(vans,120)
falldown(testfall)


"""

turtle.forward(50)
turtle.left(-90)
turtle.forward(50)
turtle.right(-180)
turtle.left(180)
#turtle.left(89)
turtle.forward(50)
time.sleep(1)
turtle.backward(100)


turtle.forward(100)
turtle.left(-85)
turtle.forward(100)
turtle.left(170)
turtle.forward(100)
turtle.left(-85)
turtle.forward(100)




"""








done()

