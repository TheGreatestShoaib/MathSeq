from turtle import *
import time


lists = [x*x for x in range(100,400)][::2]

radius = 120

turtle = Turtle()
speed(3)

for l in lists:
	act = l // radius
	print(act)
	turtle.left(45)
	time.sleep(0.5)
	turtle.forward(act)
	time.sleep(0.5)
	turtle.left(45)
	time.sleep(0.5)
	turtle.backward(act)
	time.sleep(0.5)



